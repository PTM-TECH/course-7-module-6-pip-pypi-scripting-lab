# generate_log.py

from datetime import datetime


def generate_log(log_entries):

    if not isinstance(log_entries, list):
        raise ValueError("log_entries must be a list")

    # Create filename ONLY (no directory logic)
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # Write file in current directory
    with open(filename, "w") as file:
        for entry in log_entries:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")

    return filename