import pytest

from snakemake_interface_common.exceptions import WorkflowError


def test_workflow_error():
    with pytest.raises(WorkflowError):
        raise WorkflowError("This is a test error")