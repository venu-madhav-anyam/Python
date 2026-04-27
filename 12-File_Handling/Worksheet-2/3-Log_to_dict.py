"""
Log Parser to Dictionary
Develop a function that reads each line of the log file and parses it into a dictionary with
keys: timestamp, log_level, module (if available), and message. Return a list of
such dictionaries.
Challenge: Handle lines that deviate from the standard format by either skipping them or
recording an error message.
"""


def parse_log(file_name):
    log_entries = []

    try:
        with open(file_name, "r") as file:
            for line in file:
                parts = line.strip().split(" ", 4)

                log_dict = {
                    "timestamp": parts[0] + " " + parts[1],
                    "log_level": parts[2],
                    "module": None,
                    "message": "",
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

for log in logs:
    print(log)
