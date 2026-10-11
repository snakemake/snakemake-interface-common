"""Valid plugin with optional settings class."""

from snakemake_interface_common.plugin_registry.plugin import SettingsBase


example_string = "valid 1"


class ExampleSettings(SettingsBase):
    pass  # TODO: add attributes
