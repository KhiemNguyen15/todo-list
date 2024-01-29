from pathlib import Path
import os
import sqlite3


DIR_PATH = os.path.join(os.path.expanduser("~"), ".todo", "data")
DB_PATH = Path(os.path.join(DIR_PATH, "tasks.db"))


def init_database():
    os.makedirs(DIR_PATH, exist_ok=True)
    DB_PATH.touch()

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            due TEXT
        )
        """
    )

    conn.commit()
    conn.close()


def add_task(task, due):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("INSERT INTO tasks (task, due) VALUES (?, ?)", (task, due))

    conn.commit()
    conn.close()


def update_task(task_id, new_task, due):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if not due:
        c.execute(
            """
            UPDATE tasks
            SET task = ?
            WHERE id = ?
            """,
            (new_task, task_id),
        )
    else:
        c.execute(
            """
            UPDATE tasks
            SET task = ?, due = ?
            WHERE id = ?
            """,
            (new_task, due, task_id),
        )

    conn.commit()
    conn.close()


def get_tasks():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()

    conn.close()

    return tasks


def remove_task(task_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("DELETE FROM tasks WHERE id = ?", (task_id,))

    conn.commit()
    conn.close()
