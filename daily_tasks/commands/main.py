import click as ck
from daily_tasks.commands.main_commands import create_tasks_file, add_task


@ck.group
def daily_tasks() -> None:
    """A tasks manager for those who like work from shell."""

daily_tasks.add_command(create_tasks_file)
daily_tasks.add_command(add_task)
