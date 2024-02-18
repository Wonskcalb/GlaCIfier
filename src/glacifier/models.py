from pydantic import BaseModel


class RunTime(BaseModel):
    """Represent the environemnt in which a job is run"""

    image: str
    tag: str = "latest"


class Job(BaseModel):
    runtime: RunTime
    name: str

    before: list[str] = []
    script: list[str]
    after: list[str] = []


class Stage(BaseModel):
    name: str
    jobs: list[Job] = []


class Pipeline(BaseModel):
    name: str
    stages: list[Stage] = [Stage(name="lint"), Stage(name="test"), Stage(name="build")]
