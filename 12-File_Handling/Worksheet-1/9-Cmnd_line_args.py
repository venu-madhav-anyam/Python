"""
9. Command-line Argument Parsing (Optional)
• Concepts: Utilizing modules like argparse for handling command-line arguments.
• Task:
• Develop a script that accepts a file name and a search term as command-line
arguments, processes the file, and prints matching lines.
• Validation: Run the script with various arguments to ensure that the output changes
as expected.
"""

import sys

file_name = sys.argv[1]
search_term = sys.argv[2]

with open(file_name, "r") as file:
    for line in file:
        if search_term in line:
            print(line.strip())
