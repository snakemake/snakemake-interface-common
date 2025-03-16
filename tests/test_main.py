from dataclasses import dataclass

import pytest

from snakemake_interface_common.exceptions import ApiError, WorkflowError
from snakemake_interface_common.plugin_registry.attribute_types import (
    AttributeKind,
    AttributeMode,
    AttributeType,
)
from snakemake_interface_common.plugin_registry.plugin import TaggedSettings
from snakemake_interface_common.rules import RuleInterface
from snakemake_interface_common.settings import SettingsEnumBase

# mypy: ignore-errors
@dataclass
class DummyRule(RuleInterface):
    lineno: int = 1
    name: str = "dummy_rule"
    snakefile: str = "dummy_snakefile"


def test_workflow_error():
    with pytest.raises(WorkflowError):
        raise WorkflowError("This is a test error")


def test_workflow_error_with_rule():
    with pytest.raises(WorkflowError):
        raise WorkflowError("This is a test error", rule=DummyRule())


def test_workflow_error_with_rule_and_snakefile():
    with pytest.raises(WorkflowError):
        raise WorkflowError(
            "This is a test error", rule=DummyRule(), snakefile="test_snakefile"
        )


def test_workflow_error_with_rule_and_snakefile_and_lineno():
    with pytest.raises(WorkflowError):
        raise WorkflowError(
            "This is a test error",
            rule=DummyRule(),
            snakefile="test_snakefile",
            lineno=1,
        )


def test_api_error():
    with pytest.raises(ApiError):
        raise ApiError("This is a test error")


class DummyEnum(SettingsEnumBase):
    FOO = 0
    BAR = 1


def test_settings_enum():
    assert DummyEnum.FOO == DummyEnum.parse_choice("foo")
    assert DummyEnum.BAR == DummyEnum.parse_choice("bar")
    assert "foo" == DummyEnum.FOO.item_to_choice()
    assert "bar" == DummyEnum.BAR.item_to_choice()
    assert ["bar", "foo"] == DummyEnum.choices()
    assert {DummyEnum.FOO, DummyEnum.BAR} == DummyEnum.all()
    assert [DummyEnum.FOO, DummyEnum.BAR] == DummyEnum.parse_choices_list(
        ["foo", "bar"]
    )
    assert {DummyEnum.FOO, DummyEnum.BAR} == DummyEnum.parse_choices_set(["foo", "bar"])


def test_tagged_settings():
    ts = TaggedSettings()
    ts.register_settings(object())
    ts.register_settings(object(), tag="foo")
    ts.get_settings(tag="foo")
    ts.get_settings()


def test_attribute_type_defaults():
    """Test that AttributeType initializes with default values correctly."""
    attr = AttributeType(cls=int)
    assert attr.cls is int
    assert attr.mode == AttributeMode.REQUIRED
    assert attr.kind == AttributeKind.OBJECT
    assert not attr.is_optional
    assert not attr.is_class


def test_attribute_type_optional():
    """Test that AttributeType can be optional."""
    attr = AttributeType(cls=str, mode=AttributeMode.OPTIONAL)
    assert attr.cls is str
    assert attr.mode == AttributeMode.OPTIONAL
    assert attr.is_optional
    assert not attr.is_class


def test_attribute_type_class_kind():
    """Test that AttributeType can be of class kind."""
    attr = AttributeType(cls=dict, kind=AttributeKind.CLASS)
    assert attr.cls is dict
    assert attr.kind == AttributeKind.CLASS
    assert attr.is_class
    assert not attr.is_optional


def test_attribute_type_into_required():
    """Test that into_required converts an optional AttributeType to required."""
    attr = AttributeType(cls=list, mode=AttributeMode.OPTIONAL)
    required_attr = attr.into_required()

    assert required_attr.cls is list
    assert required_attr.mode == AttributeMode.REQUIRED
    assert not required_attr.is_optional
    assert required_attr.kind == attr.kind  # Should retain kind
