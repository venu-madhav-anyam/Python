"""
7. Data Structures: Lists, Dictionaries, and Sets
• Concepts: Efficient use of lists, dictionaries, tuples, and sets to store and manipulate data.
• Task:
• Given a list of log lines, group them by severity (e.g., INFO, WARNING, ERROR)
using a dictionary.
• Validation: Verify that the dictionary keys and counts correctly reflect the
distribution of log entries.
"""

import re

with open("log.log", "r") as file:
    lines = file.readlines()

pattern = r"(\d{2}:\d{2}:\d{2}) (INFO|WARNING|ERROR) (.*)"

severity_counts = {}

for line in lines:
    match = re.search(pattern, line)

    if match:
        severity = match.group(2)

        if severity in severity_counts:
            severity_counts[severity] += 1
        else:
            severity_counts[severity] = 1

print(severity_counts)
