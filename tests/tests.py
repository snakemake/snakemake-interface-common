from dataclasses import dataclass
import pytest

from snakemake_interface_common.exceptions import ApiError, WorkflowError
from snakemake_interface_common.rules import RuleInterface


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
        raise WorkflowError("This is a test error", rule=DummyRule(), snakefile="test_snakefile")


def test_workflow_error_with_rule_and_snakefile_and_lineno():
    with pytest.raises(WorkflowError):
        raise WorkflowError("This is a test error", rule=DummyRule(), snakefile="test_snakefile", lineno=1)


def test_api_error():
    with pytest.raises(ApiError):
        raise ApiError("This is a test error")
