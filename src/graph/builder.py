from dataclasses import dataclass, field

from src.models.pipeline import Pipeline
from src.models.stage import Stage


@dataclass
class Builder:
    pipelines: list[Pipeline] = field(default_factory=list)

    def create_pipeline(self, name: str, stages: list[Stage] | None = None):
        """Create a new pipeline, add it to the builder."""

        pipeline = Pipeline(name=name, stages=stages)

        self.pipelines.append(pipeline)

        return pipeline
