"""
JSON Log Converter
Write a script that converts the log file into a JSON file. Each log entry should be a JSON
object containing the keys: timestamp, log_level, module, and message.
Challenge: Ensure that the JSON output correctly represents all valid log entries while
ignoring or flagging misformatted lines.
"""

import json


def log_to_json(log_file, json_file):
    data = []
    with open(log_file, "r") as f:
        for line in f:
            data.append(line.strip())

    with open(json_file, "w") as f:
        json.dump(data, f, indent=4)

    print("log successfully converted to json")


log_to_json("server_logs.log", "output.json")
