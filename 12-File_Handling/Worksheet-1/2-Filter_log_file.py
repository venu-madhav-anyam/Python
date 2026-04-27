"""
2. File I/O Operations
• Concepts: Reading from and writing to files, handling file paths, and using context
managers.
• Task:
• Create a script that reads a log file, filters specific lines (e.g., containing "ERROR"),
and writes the filtered content to a new file.
• Validation: Check that the output file contains only the lines that meet the filter
criteria.
"""

import re

file = open("log.log", "r")

lines = file.readlines()

filtered_lines = [line for line in lines if "ERROR" in line]

file.close()

file = open("filtered_log.log", "w")

file.writelines(filtered_lines)

file.close()
