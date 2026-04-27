"""
8. List and Dictionary Comprehensions
• Concepts: Using comprehensions for concise and efficient data transformations.
• Task:
• Write a script that filters out and transforms a list of log entries using list
comprehensions (for instance, extracting only error messages).
• Validation: Confirm that the resultant list contains only the expected entries.
"""

with open("log.log", "r") as file:
    log_entries = file.readlines()
    
s = str(input("Enter a word to search: "))

error_messages = [entry.strip() for entry in log_entries if s in entry]
print(error_messages)
