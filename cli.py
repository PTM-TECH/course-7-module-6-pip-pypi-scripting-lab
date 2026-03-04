# cli.py

import argparse
from generate_log import generate_log


# Sample in-memory task list
tasks = [
    "User logged in",
    "User updated profile",
    "Report exported"
]


def main():
    parser = argparse.ArgumentParser(description="Task Automation CLI Tool")
    subparsers = parser.add_subparsers(dest="command")

    # Add task command
    parser_add = subparsers.add_parser("add-task", help="Add a new task")
    parser_add.add_argument("task", type=str, help="Task description")

    # Complete task command
    parser_complete = subparsers.add_parser("complete-task", help="Mark a task complete")
    parser_complete.add_argument("task", type=str, help="Task to complete")

    args = parser.parse_args()

    if args.command == "add-task":
        tasks.append(args.task)
        generate_log(tasks)
        print(f"Task added: {args.task}")

    elif args.command == "complete-task":
        if args.task in tasks:
            tasks.remove(args.task)
            generate_log(tasks)
            print(f"Task completed: {args.task}")
        else:
            print("Task not found.")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()