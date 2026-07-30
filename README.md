# Trellomize

A Trello-style team task manager that runs entirely in the terminal, built in Python with [rich](https://github.com/Textualize/rich) for the UI. Users sign up, create projects, invite members, and manage tasks on a Kanban-style board — with roles, comments, per-task history, and an admin CLI.

**Web demo:** https://soroush83faraz.github.io/trellomize/ — an interactive browser demo of the same data model (statuses, priorities, roles, comments, history) as a drag-and-drop kanban board. The CLI remains the full product.

## Features

- **Accounts and authentication**
  - Sign-up with email validation, username rules (alphanumeric only), and password checks.
  - Passwords are hashed with **bcrypt** (never stored in plain text).
  - Banned (deactivated) users are blocked at login.
- **Admin CLI** (`manager.py`)
  - `create-admin` — create the admin account.
  - `change-field` — toggle a user's active status (ban/unban).
  - `purge-data` — wipe all stored data (with confirmation).
- **Projects**
  - Create a project with a title, a unique ID, and members (added by username).
  - Two roles: the **leader** (creator) and **members**; the project list marks which one you are in each project.
  - Leaders can add/remove members; members see the same board with restricted powers.
- **Tasks**
  - Kanban statuses: `BACKLOG`, `TODO`, `DOING`, `DONE`, `ARCHIVED` — tasks are shown in a status-column table and can be moved between columns.
  - Priorities: `CRITICAL`, `HIGH`, `MEDIUM`, `LOW`.
  - Each task gets a UUID, a start time, and an end time (default: 24 hours after creation).
  - Leaders assign/unassign members to tasks and change priorities.
- **Comments and history** — every task carries a comment thread (writer + timestamp) and a history of what was done, by whom, and when.
- **Activity logging** — actions across the app are logged to `mylog.log`.
- **Persistence** — all data is stored in local JSON files (created at runtime, not committed).

The interface is menu-driven: navigate options with `w`/`s`, confirm with `c`, and back out with `*`.

## Installation

Requires Python 3.12+ (the code uses nested f-string quotes).

```bash
git clone https://github.com/soroush83faraz/trellomize.git
cd trellomize
pip install -r Requirements.txt
```

## Usage

Create the admin account first, then start the app:

```bash
python manager.py create-admin --username admin --password yourpassword
python main.py
```

From the main menu you can sign up, log in, and then create projects, open their boards, and manage tasks.

The UI uses emoji; if you hit a `UnicodeEncodeError` on Windows, use a UTF-8 console (e.g. `set PYTHONIOENCODING=utf-8` before running).

Other admin commands:

```bash
python manager.py change-field --username admin --password yourpassword   # ban/unban a user
python manager.py purge-data                                              # delete all data
```

## Tests

Unit tests are written with `unittest` (including mocking) and cover the core classes (`Task`, `Projects`, `User`, `Commento`) and several global functions:

```bash
python -m unittest test_classes test_global_functios
```

Note: some tests in `test_global_functios.py` expect pre-existing sample data in the local JSON files.

## Project structure

| File | Purpose |
| --- | --- |
| `main.py` | Entry point: sign-up / log-in / exit loop |
| `manager.py` | Admin CLI (create-admin, ban/unban, purge-data) |
| `making_new_account.py` | Sign-up flow with email/username/password validation |
| `Login_section.py` | Login flow and credential checking |
| `Trellomize_space_when_Log_in.py` | Post-login menu: create/view/remove projects |
| `projects.py` | `Projects` class: members, IDs, saving, task creation |
| `tasks.py` | `Task` class, status and priority enums |
| `user.py` | `User` class and bcrypt password hashing |
| `comment.py` / `comment_and_member.py` | Comments, task assignment, priority changes |
| `history.py` | `History` class for per-task audit entries |
| `in_project_workplace.py` | Inside-a-project menus and task views |
| `go_to_project_for_leader.py` | Project board and task management for leaders |
| `go_to_project_for_member.py` | Project board and task management for members |
| `printing.py` / `printing_nocls.py` | Menu rendering and keyboard navigation |
| `test_classes.py` / `test_global_functios.py` | `unittest` test suites |
| `Reports/The_last_report.pdf` | Project report |
