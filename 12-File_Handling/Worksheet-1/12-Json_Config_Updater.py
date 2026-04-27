"""
Task 8: JSON Configuration Updater
• Concepts: File I/O, JSON processing, dictionary manipulation, and exception handling.
• Description:
Create a script that loads a JSON configuration file, updates specific keys based on given
conditions (for example, updating a version number or toggling a feature flag), and writes
the modified configuration back to disk.
• Validation:
Test the script with a sample JSON file and ensure only the intended keys are modified
while the rest of the configuration remains intact.
"""

import json

def update_config(config, key, value):
    try:
        config[key] = value
    except KeyError:
        raise ValueError(f"Invalid key: {key}")

    return config

config_file = "config.json"
with open(config_file, "r") as file:
    config = json.load(file)

updated_config = update_config(config, "version", "1.2.3")
updated_config = update_config(updated_config, "feature_flag", True)

with open(config_file, "w") as file:
    json.dump(updated_config, file, indent=4)
