import pytest
from pydantic import ValidationError

from glacifier.models import Job, RunTime


def test_job_no_args():
    with pytest.raises(ValidationError) as ctx:
        Job()  # type: ignore

    errors = [(error["type"], error["loc"]) for error in ctx.value.errors()]

    assert errors == [
        ("missing", ("runtime",)),
        ("missing", ("name",)),
        ("missing", ("script",)),
    ]


def test_job_definition():
    """
    GIVEN a runtime
    WHEN creating a job with correct data
    THEN the job is created
    AND no exception is raised
    """
    runtime = RunTime(image="python", tag="latest")

    script = ["poetry run pytest"]

    job = Job(name="test", runtime=runtime, script=script)

    assert job.model_dump() == {
        "runtime": runtime.model_dump(),
        "name": "test",
        "before": [],
        "script": script,
        "after": [],
    }
