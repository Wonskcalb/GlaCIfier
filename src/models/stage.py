from pydantic import BaseModel
from src.exceptions import InvalidJobName

from src.models.job import Job


class Stage(BaseModel):
    """Definition for a Gitlab stage."""

    name: str

    jobs: list[Job] = []
    _job_names = []

    def add_job(self, job: Job):
        """Add a job to an existing stage of the pipeline."""

        if job.name in self._job_names:
            raise InvalidJobName(
                f"Cannot add job {job.name} to stage {self.name} because a job with that name already exists."
            )

        self._job_names.append(job.name)
        self.jobs.append(job)


    def explain(self):
        print(f"Stage named {self.name}, containing {len(self.jobs)} jobs")

        for job in self.jobs:
            job.explain()
