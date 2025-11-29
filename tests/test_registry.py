"""Test the PluginRegistry class."""

from typing import Iterable
from pathlib import Path
from importlib.metadata import EntryPoints, EntryPoint

import pytest

import snakemake_interface_common.plugin_registry
from snakemake_interface_common.plugin_registry.plugin import SettingsBase
from snakemake_interface_common.exceptions import InvalidPluginException
from .example_plugin import ExamplePlugin, ExamplePluginRegistry


# Directory containing importable example plugins
PLUGIN_DIR = Path(__file__).parent / "plugins"


def patch_entry_points(
    monkeypatch: pytest.MonkeyPatch, entry_points: Iterable[EntryPoint]
) -> None:
    """
    Monkeypatch the ``importlib.metadata.entry_points()`` function (as imported in the module that
    defines ``PluginRegistryBase``) to return the given entry points.
    """
    entry_points_obj = EntryPoints(entry_points)

    def entry_points_mocked(**kw):
        return entry_points_obj.select(**kw)

    monkeypatch.setattr(
        snakemake_interface_common.plugin_registry, "entry_points", entry_points_mocked
    )


def test_basic():
    """Test basic attributes and behavior."""
    registry = ExamplePluginRegistry()
    assert registry.get_plugin_type() == "example"

    # Check singleton
    assert ExamplePluginRegistry() is registry

    # Check plugin not found
    assert not registry.is_installed("foo")
    with pytest.raises(InvalidPluginException):
        registry.get_plugin("foo")


def test_discovery(monkeypatch: pytest.MonkeyPatch):
    """Test plugin discovery and initialization."""

    # Add directory of valid plugins to import path so they can be discovered by module name
    monkeypatch.syspath_prepend(str(PLUGIN_DIR / "valid"))

    # Mock entry points
    patch_entry_points(
        monkeypatch,
        [
            # Example plugin
            EntryPoint(
                "entrypoint",
                "entrypoint_example_plugin.submodule",
                "snakemake.example_plugins",
            ),
            # Also add a couple entry points that shouldn't be matched
            EntryPoint("my-logger", "my_snakemake_logger.logger", "snakemake.loggers"),
            EntryPoint("some-tool", "some_tool.cli:cli", "console_scripts"),
        ],
    )

    # Now instantiate the registry and check discovery
    registry = ExamplePluginRegistry.new()

    expected_plugins = {"valid-1", "valid-2", "entrypoint"}
    plugins: dict[str, ExamplePlugin] = {}

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

    # Entrypoint plugin
    assert plugins["entrypoint"].string_attr == "entrypoint"
    assert plugins["entrypoint"].settings_cls is None


def test_missing_attr(monkeypatch: pytest.MonkeyPatch):
    """Test plugin with missing required attribute."""

    monkeypatch.syspath_prepend(str(PLUGIN_DIR / "missing-attr"))

    with pytest.raises(InvalidPluginException) as exc_info:
        ExamplePluginRegistry.new()

    errmsg = str(exc_info.value)
    assert "missing-attr" in errmsg
    assert "plugin does not define example_string" in errmsg


def test_invalid_object(monkeypatch: pytest.MonkeyPatch):
    """Test plugin with invalid object attribute."""

    monkeypatch.syspath_prepend(str(PLUGIN_DIR / "invalid-object"))

    with pytest.raises(InvalidPluginException) as exc_info:
        ExamplePluginRegistry.new()

    errmsg = str(exc_info.value)
    assert "invalid-object" in errmsg
    assert "example_string must be of type str" in errmsg


def test_invalid_class(monkeypatch: pytest.MonkeyPatch):
    """Test plugin with invalid class attribute."""

    monkeypatch.syspath_prepend(str(PLUGIN_DIR / "invalid-class"))

    with pytest.raises(InvalidPluginException) as exc_info:
        ExamplePluginRegistry.new()

    errmsg = str(exc_info.value)
    assert "invalid-class" in errmsg
    assert "ExampleSettings must be a subclass of" in errmsg
    assert "SettingsBase" in errmsg


def test_invalid_entry_point(monkeypatch):
    """Test invalid entry points."""

    # Colon in entry point value
    with monkeypatch.context() as ctx:
        patch_entry_points(
            ctx,
            [
                EntryPoint(
                    "non-module", "my_example_plugin:foo", "snakemake.example_plugins"
                )
            ],
        )

        with pytest.raises(InvalidPluginException) as exc_info:
            ExamplePluginRegistry.new()

    errmsg = str(exc_info.value)
    assert "non-module" in errmsg
    assert "my_example_plugin:foo" in errmsg

    # Not importable
    with monkeypatch.context() as ctx:
        patch_entry_points(
            ctx,
            [
                EntryPoint(
                    "unimportable", "my_example_plugin.foo", "snakemake.example_plugins"
                )
            ],
        )

        with pytest.raises(InvalidPluginException) as exc_info:
            ExamplePluginRegistry.new()

    errmsg = str(exc_info.value)
    assert "unimportable" in errmsg
    assert "unable to import my_example_plugin.foo" in errmsg
