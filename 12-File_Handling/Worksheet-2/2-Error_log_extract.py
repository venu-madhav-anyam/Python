"""
 Error Log Extractor
Using basic string manipulation (without regex), write a script that filters and prints all log
entries containing the word “ERROR”.
Challenge: Verify that only well-formed error lines are extracted while ignoring
misformatted lines.
"""


def extract_error(file_name):
    try:
        with open(file_name, "r") as file:
            print("ERROR log entries:")

            for line in file:
                if "ERROR" in line:
                    print(line.strip())

    except FileNotFoundError:
        print("Error: Log file not found")
    except Exception as e:
        print(f"An error occurred: {e}")


extract_error("mixed_logs.log")
