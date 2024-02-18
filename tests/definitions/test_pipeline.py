import pytest
from pydantic import ValidationError

from glacifier.models.pipeline import Pipeline


def test_pipeline_no_args():
    """
    GIVEN nothing
    WHEN creating a pipeline with no data
    THEN an exception is raised
    """
    with pytest.raises(ValidationError) as ctx:
        Pipeline()  # type: ignore

    errors = [(error["type"], error["loc"]) for error in ctx.value.errors()]

    assert errors == [
        ("missing", ("name",)),
    ]
