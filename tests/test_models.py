import pytest
from src.exceptions import InvalidJobName

from src.models import *


@pytest.fixture
def stage() -> Stage:
    return Stage(name="lint")


@pytest.fixture
def job() -> Job:
    return Job(
        name="black",
        image="python:3.11-slim",
        job_init=JobInit(name="Install black", tasks=["pip install black"]),
        job_tasks=["black . --check --diff"],
    )


def test_pipeline_has_default_jobs():
    pipeline = Pipeline(name="Test pipeline")
    names = [s.name for s in pipeline.stages]

    assert len(names) == 3, "The pipeline should have 3 default stages"
    assert names == ["lint", "test", "build"], "The names should not have changed."


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
