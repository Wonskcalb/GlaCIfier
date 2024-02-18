import pytest
from pydantic import ValidationError

from glacifier.models import Job, RunTime, Stage


def test_stage_no_args():
    with pytest.raises(ValidationError) as ctx:
        Stage()  # type: ignore

    errors = [(error["type"], error["loc"]) for error in ctx.value.errors()]

    assert errors == [
        ("missing", ("name",)),
    ]


def test_stage_definition():
    """
    GIVEN a runtime
    WHEN creating a stage with correct data
    THEN the stage is created
    AND no exception is raised
    """
    runtime = RunTime(image="docker", tag="latest")
    job = Job(runtime=runtime, name="build", script=["docker build"])
    stage = Stage(name="build", jobs=[job])

    assert stage.model_dump() == {
        "name": "build",
        "jobs": [job.model_dump()],
    }
