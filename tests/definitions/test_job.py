import pytest
from pydantic import ValidationError

from glacifier.models.job import Job, JobEnv


def test_job_no_args():
    with pytest.raises(ValidationError) as ctx:
        Job()  # type: ignore

    errors = [(error["type"], error["loc"]) for error in ctx.value.errors()]

    assert errors == [
        ("missing", ("name",)),
        ("missing", ("env",)),
        ("missing", ("tasks",)),
    ]


def test_job_definition():
    """
    GIVEN a runtime
    WHEN creating a job with correct data
    THEN the job is created
    AND no exception is raised
    """
    env = JobEnv(image="python", tag="latest")

    script = ["poetry run pytest"]

    job = Job(name="test", env=env, tasks=script)

    assert job.model_dump() == {
        "env": env.model_dump(),
        "name": "test",
        "before": [],
        "tasks": script,
        "after": [],
    }
