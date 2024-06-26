import click
from tabulate import tabulate

from todo.database import init_database, add_task, update_task, get_tasks, remove_task


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
@click.argument("task_id", type=int)
@click.argument("new_task")
@click.option("--due", help="Due date for the task.")
def update(task_id, new_task, due):
    """Update an existing task."""
    num_tasks = len(get_tasks())
    if task_id < 1 or task_id > num_tasks:
        click.echo("Invalid task ID.")
        return

    tasks = get_tasks()
    id_to_update = tasks[task_id - 1][0]

    update_task(id_to_update, new_task, due)
    click.echo(f"Task with ID {task_id} updated successfully.")


@main.command()
def list():
    """List all tasks."""
    tasks = get_tasks()

    if not tasks:
        click.echo("No tasks to display.")
        return

    display = [(i + 1, task[1], task[2]) for i, task in enumerate(tasks)]

    headers = ["ID", "Task", "Due"]
    click.echo(tabulate(display, headers=headers, tablefmt="grid"))


@main.command()
@click.argument("task_id", type=int)
def remove(task_id):
    """Remove a task."""
    num_tasks = len(get_tasks())
    if task_id < 1 or task_id > num_tasks:
        click.echo("Invalid task ID.")
        return

    tasks = get_tasks()
    id_to_remove = tasks[task_id - 1][0]

    remove_task(id_to_remove)
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
