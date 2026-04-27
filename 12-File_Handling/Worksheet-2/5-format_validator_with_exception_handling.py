"""
Format Validator with Exception Handling
Create a script that reads the log file and identifies lines that do not match the expected log
format. For each misformatted line, log a warning with its line number while continuing to
process the rest of the file.
Challenge: Ensure that your solution uses try-except blocks to catch and handle exceptions
without crashing.
"""

import re

def find_misformatted_logs(file_name):
    log_pattern = re.compile(
        r"^\d{4}-\d{2}-\d{2}"
        r"\d{2}:\d{2}:\d{2},\d{3}"
        r"(INFO|DEBUG|ERROR|WARNING):"
        r"\[w+\] - "
        r".+$"
    )

    try:
        with open(file_name,"r") as file:
            for line_number, line in enumerate(file,start=1):
                if not log_pattern.match(line.strip()):
                    print(f"Warning: Line {line_number} is misformatted")
                    print(f" {line.strip()}")
    except FileNotFoundError:
        print("Error: Log file not found")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

find_misformatted_logs("app.log")