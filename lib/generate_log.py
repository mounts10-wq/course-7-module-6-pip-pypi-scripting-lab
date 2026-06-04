from datetime import datetime
import os

def generate_log(data):
    """
    Creates a log file with today's date in the filename and writes
    each entry from the input list to the file.

    Args:
        data (list): A list of log entry strings.

    Returns:
        str: The name of the generated log file.

    Raises:
        ValueError: If data is not a list.
    """
    # STEP 1: Validate input
    if not isinstance(data, list):
        raise ValueError("Input must be a list.")

    # STEP 2: Generate filename with today's date
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # STEP 3: Write log entries to the file
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # STEP 4: Print confirmation message
    print(f"Log written to {filename}")

    return filename
