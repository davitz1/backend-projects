# Tasker: CLI Task Tracker App

  Tasker is a simple Command Line Interface application for task management written in python.
  
  (Solution for [task-tracker project](https://roadmap.sh/projects/task-tracker))

## Features

  • Add tasks and store in a json file.
  
  • Delete tasks by their ID.

  • Update the description of an existing task.

  • List tasks, with the option of filtering by their status (to-do, in-progress, done).
  
  • Change the task status to in-progress or done.
  

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/davitz1/backend-projects.git
   cd backend-projects/taskTracker
   ```
   
2. Add executable symlink (optional):
   ```bash
   ln -s /full/path/to/tasker ~/.local/bin/tasker
   chmod +x /full/path/to/tasker
   ```
   
3. Run:
   ```bash
   tasker add "Buy groceries"
   ```

## Command Reference


| Command                  | Description                       |
|--------------------------|-----------------------------------|
| `tasker add "desc"`      | Add new task                      |
| `tasker delete <id>`     | Delete task                       |
|`tasker update <id> "newdesc"` | Update the description of a task|
| `tasker list`            | List all tasks                    |
| `tasker done <id>` `tasker inprog <id>`       | Change the task status                 |

Use `tasker --help` or `tasker <command> --help` for more details.
