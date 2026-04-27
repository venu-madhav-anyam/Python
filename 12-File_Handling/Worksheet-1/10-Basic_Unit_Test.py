"""
10. Basic Unit Testing (Optional)
• Concepts: Using Python's unittest or pytest modules to write and run test cases.
• Task:
• Write unit tests for one or more of the functions developed (e.g., log parsing or regex
matching).
• Validation: Ensure that all tests pass when the functions are correct and that failures
are appropriately flagged when introducing errors.
These tasks are designed to simulate everyday challenges that engineers face, such as analyzing
logs and executing simple automation scripts. By completing these worksheets, engineers can selfevaluate
their strengths and identify areas for further improvement in Python.
"""

import unittest
import re


def parse_log(line):
    pattern = r"\d{4}-\d{2}-\d{2} (\d{2}:\d{2}:\d{2}) (INFO|WARNING|ERROR) (.*)"
    match = re.search(pattern, line)

    if match:
        return {
            "time": match.group(1),
            "severity": match.group(2),
            "message": match.group(3),
        }
    return None
