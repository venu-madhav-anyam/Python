"""
6. Functions and Modular Programming
• Concepts: Function definitions, parameters, return values, and basic modular design.
• Task:
• Refactor one of the earlier tasks (such as log parsing) into reusable functions and
modules.
• Validation: Test the functions independently to ensure they work correctly with
predefined inputs.
"""


def read_log(file_path):
    try:
        with open(file_path, "r") as file:
            log_entries = file.readlines()
        return log_entries
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return []

    except Exception as e:
        print(f"An error occurred: {e}")
        return []

    finally:
        file.close()

    return log_entries


log_entries = read_log("log.log")

for entry in log_entries:
    print(entry)
