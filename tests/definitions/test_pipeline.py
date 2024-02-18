import pytest
from pydantic import ValidationError

from glacifier.models import Pipeline


def test_pipeline_no_args():
    with pytest.raises(ValidationError) as ctx:
        Pipeline()  # type: ignore

    errors = [(error["type"], error["loc"]) for error in ctx.value.errors()]

    assert errors == [
        ("missing", ("name",)),
    ]


def test_pipeline_definition():
    """
    GIVEN noting
    WHEN creating a pipeline with no data
    THEN the pipline is created
    AND contains 3 default stages
    AND no exception is raised
    """
    pipeline = Pipeline(name="main")

    assert pipeline.model_dump() == {
        "name": "main",
        "stages": [
            {
                "name": "lint",
                "jobs": [],
            },
            {
                "name": "test",
                "jobs": [],
            },
            {
                "name": "build",
                "jobs": [],
            },
        ],
    }
