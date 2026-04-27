"""
Task 10: Data Format Converter (CSV to JSON)
• Concepts: File I/O, CSV and JSON modules, data transformation, and list comprehensions.
• Description:
Develop a script that reads data from a CSV file and converts each row into a JSON object.
The final output should be a JSON file containing an array of these objects.
• Validation:
Provide a sample CSV file and confirm that the output JSON file accurately represents the
CSV content structure.
"""

import csv
import json


def csv_to_json(csv_file, json_file):
    data = []

    with open(csv_file, "r", newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:
            data.append(row)

    with open(json_file, "w") as f:
        json.dump(data, f, indent=4)

    print("csv successfully converted to json")


csv_to_json("test.csv", "data.json")
