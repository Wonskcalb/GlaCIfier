from invoke import task


@task()
def prepare(ctx):
    """Install required packages to fully the stack (pipx required)"""

    for package in ["pre-commit", "ggshield"]:
        ctx.run(f"pipx install {package}")

    ctx.run("ggshield auth login")


@task()
def configure(ctx):
    """Configure the dev environment."""

    for hook in ["pre-commit", "commit-msg"]:
        ctx.run(f"pre-commit install --hook-type {hook}")

    ctx.run("pdm install")


@task(pre=[prepare, configure])
def init(_):
    """Create a fully working environement"""

    pass
