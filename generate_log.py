# generate_log.py

from datetime import datetime
import os


def generate_log(log_entries, directory="."):


    if not isinstance(log_entries, list):
        raise ValueError("log_entries must be a list")

    # Create filename
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # If default directory ".", don't prefix it
    if directory == ".":
        filepath = filename
    else:
        os.makedirs(directory, exist_ok=True)
        filepath = os.path.join(directory, filename)

    # Write file
    with open(filepath, "w") as file:
        for entry in log_entries:
            file.write(f"{entry}\n")

    print(f"Log written to {filepath}")

    return filepath