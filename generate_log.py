# generate_log.py

from datetime import datetime
import os


def generate_log(log_entries, directory="."):
    """
    Creates a timestamped log file (log_YYYYMMDD.txt)
    from a list of log entries.

    Raises:
        ValueError: If log_entries is not a list.
    """

    # Validate input
    if not isinstance(log_entries, list):
        raise ValueError("log_entries must be a list")

    # Ensure directory exists
    os.makedirs(directory, exist_ok=True)

    # Create timestamped filename
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    filepath = os.path.join(directory, filename)

    # Write entries to file
    with open(filepath, "w") as file:
        for entry in log_entries:
            file.write(f"{entry}\n")

    print(f"Log written to {filepath}")

    return filepath