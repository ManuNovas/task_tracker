# Task Tracker CLI

This project implements hexagonal architecture inside a pure python project

## Requirements

- Python 3.13

## Installation

Clone the project and set up a virtual environment

```shell
git clone https://github.com/ManuNovas/task_tracker
python3 -venv .venv
source .venv/bin/activate
```

## Usage

This package supports the following operations

```shell
python main.py add "Learn hexagonal architecture" # Adds a new task
python main.py list # Displays all tasks
python main.py update 1 "Learn python basis" # Updates one task
python main.py list todo # Displays all to-do tasks
python main.py mark-in-progress 1 # Mark one task in progress
python main.py list in-progress # Displays all in progress tasks
python main.py mark-done 1 # Mark one task done
python main.py list done # Display all done tasks
python main.py delete 1 # Deletes one task
```

## Test

You can test the application with the following command

```shell
python -m unittest tests/task_tests.py
```

## Project URL

https://roadmap.sh/projects/task-tracker

