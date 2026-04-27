"""
Task 12: Custom Log Filter with Criteria
• Concepts: Advanced string manipulation, regular expressions, file I/O, and dictionary
usage.
• Description:
Write a script that reads a log file and filters entries based on custom criteria—such as logs
within a specific time range or containing a particular keyword pattern. Employ regex to
accurately extract and process these elements.
• Validation:
Run the script on sample log data and confirm that the filtered output matches the specified criteria.
"""

import re


def import_logs_with_pattern(log_file, pattern):
    matched_logs = []

    data = re.compile(pattern)

    with open(log_file, "r") as file:
        for line in file:
            if data.search(line):
                matched_logs.append(line.strip())

    return matched_logs


log_file = "moderate_log.log"
pattern = r"ERROR"

res = import_logs_with_pattern(log_file, pattern)

print("Matched logs: ")
for log in res:
    print(log)
