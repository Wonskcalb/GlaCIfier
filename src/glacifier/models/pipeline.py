from pydantic import BaseModel

from .stage import Stage


class Pipeline(BaseModel):
    """
    Definition for a Gitlab pipeline.
    """

    name: str

    stages: list[Stage] = []

    def __str__(self) -> str:
        stage_names = ", ".join(map(str, self.stages))

        return f"Pipeline {self.name}: [{stage_names}]"
