"""
Log Level Counter
Write a script that reads the provided log file and counts the number of occurrences of each
log level (INFO, DEBUG, WARNING, ERROR) using file I/O and dictionaries. Avoid using
regular expressions for this task.
Challenge: Ensure your code gracefully handles lines that do not follow the expected
format.
"""


def count_log_levels(file_name):
    log_counts = {"INFO": 0, "DEBUG": 0, "WARNING": 0, "ERROR": 0}

    try:
        with open(file_name, "r") as file:
            for line in file:
                for level in log_counts:
                    if level in line:
                        log_counts[level] += 1

        print("Log Level Count:")
        for level, count in log_counts.items():
            print(f"{level}:{count}")

    except FileNotFoundError:
        print("Error: Log file not found")
    except Exception as e:
        print(f"An error occurred: {e}")


count_log_levels("mixed_logs.log")
