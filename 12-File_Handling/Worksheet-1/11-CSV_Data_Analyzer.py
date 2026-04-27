"""
Task 7: CSV Data Analyzer
• Concepts: File I/O, data structures (lists and dictionaries), list comprehensions, and basic
data analysis.
• Description:
Develop a script that reads a CSV file containing columns such as "TestCase," "Status," and
"ExecutionTime." The script should produce a summary report showing counts for each
status (e.g., Passed, Failed) and compute the average execution time.
• Validation:
Use a sample CSV file and compare the output summary with expected statistics.
"""

import csv


def analyze_csv(file_name):
    status_count = {}
    execution_times = []

    with open(file_name, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            status = row["Status"]
            time = float(row["ExecutionTime"])
            status_count[status] = status_count.get(status, 0) + 1

            execution_times.append(time)

    avg_time = sum(execution_times) / len(execution_times)

    print("Summary Report")
    print()

    for status, count in status_count.items():
        print(f"{status}: {count}")

    print(f"\nAverage Execution Time: {avg_time:.3f} seconds")



# Main
analyze_csv("test.csv")
