"""
3. String Manipulation
• Concepts: String methods, slicing, formatting, and parsing.
• Task:
• Develop a script that processes log entries by extracting the timestamp, severity, and
message from each line.
• Validation: Ensure that the parsed elements match the expected values for sample
log entries.
"""

import re

with open("log.log", "r") as file:
    lines = file.readlines()

pattern = r"(\d{2}:\d{2}:\d{2}) (INFO|WARNING|ERROR) (.*)"

for line in lines:
    match = re.search(pattern, line)
    
    if match:
        time = match.group(1)
        severity = match.group(2)
        message = match.group(3)
        
        print("Time:", time)
        print("Severity:", severity)
        print("Message:", message)
        print()
    else:
        print("No match:", line) 