"""
Task 11: Nested Data Structure Flattener
• Concepts: Handling nested dictionaries/lists, recursion or iterative approaches, and data
transformation using comprehensions.
• Description:
Create a script that accepts a nested dictionary (for example, loaded from a JSON file) and
flattens it into a single-level dictionary. Use a separator (like an underscore) to concatenate
nested keys into new single keys.
• Validation:
Use a sample nested structure to verify that the output dictionary correctly maps all nested
values to single-level keys.
"""

import json


def flatten_dict(data, parent_key="", sep="_"):
    flat_dict = {}

    if isinstance(data, dict):
        for key, value in data.items():
            new_key = f"{parent_key}{sep}{key}" if parent_key else key
            flat_dict.update(flatten_dict(value, new_key, sep))

    elif isinstance(data, list):
        for i, item in enumerate(data):
            new_key = f"{parent_key}{sep}{i}"
            flat_dict.update(flatten_dict(item, new_key, sep))

    else:
        flat_dict[parent_key] = data

    return flat_dict


with open("data.json", "r") as f:
    nested_data = json.load(f)

flattened_data = flatten_dict(nested_data)

with open("flat.json", "w") as f:
    json.dump(flattened_data, f, indent=4)

print("Nested JSON successfully flattened")
