"""
Command-Line Log Filter
Develop a command-line tool using Python’s argparse module that accepts two
arguments: a log level (e.g., “ERROR”) and a module name. The script should filter the log
file to print only those entries matching both criteria.
Challenge: Validate the command-line inputs and provide helpful error messages for invalid
or missing arguments.
"""

import argparse
import re


def filter_logs(log_file, log_level, module_name):
    log_pattern = re.compile(
        rf"^\d{{4}}-\d{{2}}-\d{{2}} "
        rf"\d{{2}}:\d{{2}}:\d{{2}},\d{{3}} "
        rf"{log_level}: "
        rf"\[{module_name}\] - "
        rf".+$"
    )

    try:
        with open(log_file, "r") as file:
            for line in file:
                if log_pattern.match(line.strip()):
                    print(line.strip())
    except FileNotFoundError:
        print("Error: Log file not found")
    except Exception as e:
        print(f"Unexpected error: {e}")


parser = argparse.ArgumentParser(
    description="Filter log entries by log level and module name"
)

parser.add_argument("log_file", help="Path to the log file")

parser.add_argument(
    "log_level", help="Log level to filter (INFO, DEBUG, WARNING, ERROR)"
)

parser.add_argument("module", help="Module name to filter (e.g., ModuleX)")
args = parser.parse_args()

filter_logs(args.log_file, args.log_level, args.module)
