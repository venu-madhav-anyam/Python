"""
Task 9: Directory Log Aggregator
• Concepts: File I/O, directory traversal (using modules such as os or glob), string
manipulation, and aggregation using dictionaries.
• Description:
Write a script that scans a specified directory for all .log files, processes each file, and
aggregates counts of different log levels (e.g., INFO, WARNING, ERROR) into a single
summary dictionary.
• Validation:
Place several sample log files in a test directory and verify that the aggregated counts
correctly reflect the combined data from all files.
"""

import os
import re


def count_log_levels(directory):
    log_levels = {"INFO": 0, "WARNING": 0, "ERROR": 0}

    pattern = r"\b(INFO|WARNING|ERROR)\b"

    for file_name in os.listdir(directory):
        if file_name.endswith(".log"):
            with open(os.path.join(directory, file_name)) as file:
                for line in file:
                    match = re.search(pattern, line)
                    if match:
                        log_levels[match.group()] += 1

    return log_levels


print("Enter path from current directory: ")
directory = input()

if not os.path.exists(directory):
    print("Invalid path")
    exit()

log_levels = count_log_levels(directory)

for level, count in log_levels.items():
    print(f"{level}: {count}")
