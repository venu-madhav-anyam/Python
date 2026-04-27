"""
Group Logs by Module
Using the output from Question 3, write a function that groups log entries by their module.
For each module, output the count of log entries.
Challenge: Use dictionary comprehensions or iterative methods to build the grouped result.
"""


def group_logs_by_module(parsed_logs):
    module_counts = {}

    for log in parsed_logs:
        if "module" in log:
            module = log["module"]
            module_counts[module] = module_counts.get(module, 0) + 1

    return module_counts

def parse_log(file_name):
    log_entries = []

    try:
        with open(file_name,'r') as file:
            for line in file:
                parts = line.strip().split(" ",4)

                log_dict = {
                    "timestamp": parts[0] + " " + parts[1],
                    "log_level": parts[2],
                    "module": None,
                    "message": ""
                }

                if len(parts) == 5:
                    log_dict["module"] = parts[3]
                    log_dict["message"] = parts[4]
                else:
                    log_dict["message"] = " ".join(parts[3:])

            log_entries.append(log_dict)

    except FileNotFoundError:
        print("Error: LOg File not Found")
    except Exception as e:
        print(f"An error occurres: {e}")

    return log_entries

logs = parse_log("mixed_logs.log")
groups = group_logs_by_module(logs)

print("Log count by module:")
for module, count in groups.items():
    print(f"{module}: {count}")