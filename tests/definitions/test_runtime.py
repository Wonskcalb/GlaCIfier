import pytest
from pydantic import ValidationError

from glacifier.models import JobEnv


def test_runtime_no_args():
    with pytest.raises(ValidationError) as ctx:
        JobEnv()  # type: ignore

    errors = [(error["type"], error["loc"]) for error in ctx.value.errors()]

    assert errors == [
        ("missing", ("image",)),
    ]


def test_job_definition():
    """
    GIVEN Nothing
    WHEN creating a runtime with minimal data
    THEN the runtime is created
    AND no exception is raised
    """
    runtime = JobEnv(image="python", tag="weird-tag")

    assert runtime.model_dump() == {
        "image": "python",
        "tag": "weird-tag",
    }
