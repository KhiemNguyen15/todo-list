import click
from tabulate import tabulate

from todo.database import init_database, add_task, get_tasks, remove_task


__version__ = "1.0.0"


init_database()


@click.group()
@click.version_option(version=__version__)
def main():
    pass


@main.command()
@click.argument("task")
@click.option("--due", help="Due date for the task.")
def add(task, due):
    """Add a new task."""
    add_task(task, due)
    click.echo(f'Task "{task}" added successfully.')


@main.command()
def list():
    """List all tasks."""
    tasks = get_tasks()

    if not tasks:
        click.echo("No tasks to display.")
        return

    headers = ["ID", "Task", "Due"]
    click.echo(tabulate(tasks, headers=headers, tablefmt="grid"))


@main.command()
@click.argument("task_id", type=int)
def remove(task_id):
    """Remove a task."""
    num_tasks = len(get_tasks())
    if task_id < 1 or task_id > num_tasks:
        click.echo("Invalid task ID.")
        return

    remove_task(task_id)
    click.echo(f"Task with ID {task_id} removed successfully.")


@main.command(hidden=True)
@click.pass_context
def help(ctx):
    """Show this message and exit."""
    click.echo(ctx.parent.get_help())


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        list()
    else:
        main(prog_name="todo")
