"""Define example plugin type for testing."""

from dataclasses import dataclass
from types import ModuleType
from pathlib import Path
from typing import Self

from snakemake_interface_common.plugin_registry import PluginRegistryBase
from snakemake_interface_common.plugin_registry.plugin import PluginBase, SettingsBase
from snakemake_interface_common.plugin_registry.attribute_types import (
    AttributeType,
    AttributeMode,
    AttributeKind,
)


@dataclass
class ExamplePlugin(PluginBase):
    _name: str
    _settings_cls: type[SettingsBase] | None
    file: Path
    string_attr: str

    @property
    def name(self) -> str:
        return self._name

    @property
    def cli_prefix(self) -> str:
        return "example-plugin-" + self.name

    @property
    def settings_cls(self) -> type[SettingsBase] | None:
        return self._settings_cls


class ExamplePluginRegistry(PluginRegistryBase[ExamplePlugin]):
    @classmethod
    def new(cls) -> Self:
        """Create a new non-singleton instance for testing."""
        instance = object.__new__(cls)
        instance.__init__()
        return instance

    @property
    def module_prefix(self) -> str:
        return "snakemake_example_plugin_"

    @property
    def entry_point(self) -> str:
        return "example_plugins"

    def load_plugin(self, name: str, module: ModuleType) -> ExamplePlugin:
        settings_cls = getattr(module, "ExampleSettings", None)
        string_attr = module.example_string

        return ExamplePlugin(
            _name=name,
            _settings_cls=settings_cls,
            file=Path(module.__file__),
            string_attr=string_attr,
        )

    def expected_attributes(self):
        return {
            "ExampleSettings": AttributeType(
                cls=SettingsBase,
                mode=AttributeMode.OPTIONAL,
                kind=AttributeKind.CLASS,
            ),
            "example_string": AttributeType(
                cls=str,
                mode=AttributeMode.REQUIRED,
                kind=AttributeKind.OBJECT,
            ),
        }
