import textwrap
from pydantic import BaseModel


class JobInit(BaseModel):
    name: str
    tasks: list[str]


class Job(BaseModel):
    """Definition for a Gitlab Job"""

    name: str
    image: str | None

    job_init: JobInit | None = None
    job_tasks: list[str]


    def __str__(self) -> str:

        out = f"Job {self.name} (image used: {self.image}) \n"

        if self.job_init:
            out += "Pre-run tasks:\n"
            pre_run_tasks = [f"- {task}" for task in self.job_init.tasks]
            out += "\n".join(pre_run_tasks)
            out += "\n"

        out += "Job steps:\n"
        job_tasks = [f"- {task}" for task in self.job_tasks]
        out += "\n".join(job_tasks)

        return out
