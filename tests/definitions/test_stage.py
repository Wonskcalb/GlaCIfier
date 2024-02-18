import pytest
from pydantic import ValidationError

from glacifier.exceptions import InvalidJobName
from glacifier.models.job import Job, JobEnv
from glacifier.models.stage import Stage


@pytest.fixture
def stage() -> Stage:
    return Stage(name="lint")


@pytest.fixture
def job() -> Job:
    return Job(
        name="black",
        env=JobEnv(image="python", tag="4.20"),
        before=["pip install black"],
        tasks=["black . --check --diff"],
    )


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
    runtime = JobEnv(image="docker", tag="latest")
    job = Job(env=runtime, name="build", tasks=["docker build"])
    stage = Stage(name="build", jobs=[job])

    assert stage.model_dump() == {
        "name": "build",
        "jobs": [job.model_dump()],
    }


def test_add_job_to_stages(stage: Stage, job: Job):
    stage.add_job(job)
    assert stage.jobs == [job]


def test_add_duplicate_job_name_to_stages(stage: Stage, job: Job):
    stage.add_job(job)

    expected_exception_msg = (
        f"Cannot add job {job.name} to stage {stage.name} because"
        " a job with that name already exists"
    )

    with pytest.raises(InvalidJobName, match=expected_exception_msg):
        stage.add_job(job)
