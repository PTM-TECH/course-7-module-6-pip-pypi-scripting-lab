# lib/generate_log.py
import argparse
from datetime import datetime
import os
import requests


# Top-level function for autograder

def generate_log(log_entries, directory="."):

    if not isinstance(log_entries, list):
        raise ValueError("log_entries must be a list")

    os.makedirs(directory, exist_ok=True)
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    filepath = os.path.join(directory, filename)

    with open(filepath, "w") as file:
        for entry in log_entries:
            file.write(f"{entry}\n")

    print(f"Log written to {filepath}")
    return filepath


# Logger class for CLI usage

class Logger:
    def __init__(self, log_entries):
        if not isinstance(log_entries, list):
            raise ValueError("log_entries must be a list")
        self.log_entries = log_entries

    def generate_log_file(self, directory="."):
        # Call the top-level function
        return generate_log(self.log_entries, directory)


# Function to fetch API data

def fetch_data():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return {}


# CLI interface

def main():
    parser = argparse.ArgumentParser(description="Task Automation CLI Tool")
    subparsers = parser.add_subparsers(dest="command")

    # add-task command
    parser_add = subparsers.add_parser("add-task", help="Add a new task")
    parser_add.add_argument("task", type=str, help="Task description")

    # complete-task command
    parser_complete = subparsers.add_parser("complete-task", help="Mark task complete")
    parser_complete.add_argument("task", type=str, help="Task to complete")

    args = parser.parse_args()

    # In-memory example log
    log_data = ["User logged in", "User updated profile", "Report exported"]
    logger = Logger(log_data)

    if args.command == "add-task":
        logger.log_entries.append(args.task)
        logger.generate_log_file()
        print(f"Task added: {args.task}")

    elif args.command == "complete-task":
        if args.task in logger.log_entries:
            logger.log_entries.remove(args.task)
            logger.generate_log_file()
            print(f"Task completed: {args.task}")
        else:
            print(f"Task not found: {args.task}")
    else:
        parser.print_help()

# CLI execution

if __name__ == "__main__":
    main()