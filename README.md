# Todo List

A simple task tracker for the command line.

## Usage

Run `todo --help` to view the commands.

`todo` can be used as an alias for `todo list` to view the commands.

## Requirements

- python (3.10+)
- pip

## Installation


**Disclaimer:** The installation process has only been tested on Linux and results may vary on other operating systems.


1. Clone the repository onto your machine and enter the project's root directory:

```bash
git clone https://github.com/KhiemNguyen15/todo-list.git && cd todo-list
```

2. Install all the project dependencies through pip:

```bash
pip install -r requirements.txt
```

3. Build the app using PyInstaller:

```bash
pyinstaller -Fn todo main.py
```

4. Move the app to a directory that is included in your system's $PATH

All done! Now the app is ready for use.
