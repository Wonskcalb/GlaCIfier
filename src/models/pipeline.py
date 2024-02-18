from pydantic import BaseModel
from src.models.job import Job

from src.models.stage import Stage


class Pipeline(BaseModel):
    """
    Definition for a Gitlab pipeline.

    By default, when created a pipeline contains 3 jobs: lint, test and build
    """

    name: str

    stages: list[Stage] = [
        Stage(name="lint"),
        Stage(name="test"),
        Stage(name="build"),
    ]

    def __str__(self) -> str:
        stage_names = ", ".join(map(lambda stage: stage.name, self.stages))

        return f"Pipeline {self.name}: [{stage_names}]"
