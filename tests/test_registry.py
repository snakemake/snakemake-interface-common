"""Test the PluginRegistry class."""

from typing import Iterator
from contextlib import contextmanager
from pathlib import Path

import pytest

from snakemake_interface_common.plugin_registry import PluginRegistryBase
from snakemake_interface_common.plugin_registry.plugin import SettingsBase
from snakemake_interface_common.exceptions import InvalidPluginException
from .example_plugin import ExamplePlugin, ExamplePluginRegistry


# Directory containing importable example plugins
PLUGIN_DIR = Path(__file__).parent / "plugins"


@contextmanager
def patch_sys_path(path: str | Path) -> Iterator[None]:
    """Context manager to prepend to ``sys.path``."""

    with pytest.MonkeyPatch.context() as mp:
        mp.syspath_prepend(str(path))
        yield


@contextmanager
def reset_registry(cls: type[PluginRegistryBase]) -> Iterator[None]:
    """
    Context manager which temporary resets the registry class singleton to allow rerunning the
    plugin discovery process.
    """

    old_instance = cls._instance

    try:
        cls._instance = None
        yield

    finally:
        cls._instance = old_instance


def test_basic():
    """Test basic attributes and behavior."""
    registry = ExamplePluginRegistry()
    assert registry.get_plugin_type() == "example"

    # Check singleton
    assert registry is ExamplePluginRegistry()

    # Check plugin not found
    assert not registry.is_installed("foo")
    with pytest.raises(InvalidPluginException):
        registry.get_plugin("foo")


def test_discovery():
    """Test plugin discovery and initialization."""

    with reset_registry(ExamplePluginRegistry), patch_sys_path(PLUGIN_DIR / "valid"):
        registry = ExamplePluginRegistry()

        expected_plugins = {"valid-1", "valid-2"}
        plugins: dict[str, ExamplePlugin] = {}

        # Check valid plugins
        assert set(registry.get_registered_plugins()) == expected_plugins

        for name in expected_plugins:
            assert registry.is_installed(name)
            plugins[name] = registry.get_plugin(name)
            assert isinstance(plugins[name], ExamplePlugin)
            assert plugins[name].name == name
            assert plugins[name].file.is_relative_to(PLUGIN_DIR)

        # Valid plugin 1
        assert plugins["valid-1"].string_attr == "valid 1"
        assert plugins["valid-1"].settings_cls is not None
        assert issubclass(plugins["valid-1"].settings_cls, SettingsBase)

        # Valid plugin 2
        assert plugins["valid-2"].string_attr == "valid 2"
        assert plugins["valid-2"].settings_cls is None


def test_missing_attr():
    """Test plugin with missing required attribute."""

    with (
        reset_registry(ExamplePluginRegistry),
        patch_sys_path(PLUGIN_DIR / "missing-attr"),
    ):
        with pytest.raises(InvalidPluginException) as exc_info:
            ExamplePluginRegistry()

        errmsg = str(exc_info.value)
        assert "missing-attr" in errmsg
        assert "plugin does not define example_string" in errmsg


def test_invalid_object():
    """Test plugin with invalid object attribute."""

    with (
        reset_registry(ExamplePluginRegistry),
        patch_sys_path(PLUGIN_DIR / "invalid-object"),
    ):
        with pytest.raises(InvalidPluginException) as exc_info:
            ExamplePluginRegistry()

        errmsg = str(exc_info.value)
        assert "invalid-object" in errmsg
        assert "example_string must be of type str" in errmsg


def test_invalid_class():
    """Test plugin with invalid class attribute."""

    with (
        reset_registry(ExamplePluginRegistry),
        patch_sys_path(PLUGIN_DIR / "invalid-class"),
    ):
        with pytest.raises(InvalidPluginException) as exc_info:
            ExamplePluginRegistry()

        errmsg = str(exc_info.value)
        assert "invalid-class" in errmsg
        assert "ExampleSettings must be a subclass of" in errmsg
        assert "SettingsBase" in errmsg
