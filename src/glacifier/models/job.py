from pydantic import BaseModel


class JobEnv(BaseModel):
    """Represent the environemnt in which a job is run"""

    image: str
    tag: str = "latest"

    def explain(self):
        print(f"Image: {self.image}:{self.tag}")


class Job(BaseModel):
    """Definition for a Gitlab Job"""

    name: str
    env: JobEnv

    before: list[str] = []
    tasks: list[str]
    after: list[str] = []

    def __str__(self) -> str:
        return f"Job {self.name}"

    def explain(self):
        print(f"Job {self.name}")
        self.env.explain()

        if self.before:
            print("Job steps:")
            for task in self.before:
                print(f"\t- {task}")

        print("Job steps:")
        for task in self.tasks:
            print(f"\t- {task}")

        if self.after:
            print("Job steps:")
            for task in self.after:
                print(f"\t- {task}")
