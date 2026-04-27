"""
Regular Expression Challenge (IP Address Extractor)
Write a Python function that uses a regular expression to extract all unique IPv4 addresses
from the log file. Some log messages include IP addresses (e.g., “Ping to server
192.168.1.100 succeeded”). Return a list of unique IP addresses found.
Challenge: Ensure your regex correctly matches typical IPv4 formats and does not capture
invalid patterns.
"""

import re


def extract_unique_ips(log_file):
    ip_pattern = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")

    unique_ips = set()

    try:
        with open(log_file, "r") as file:
            for line in file:
                ips = ip_pattern.findall(line)
                for ip in ips:
                    unique_ips.add(ip)

    except FileNotFoundError:
        print("Error: Log file not found")
    except Exception as e:
        print(f"An error occurred: {e}")

    return list(unique_ips)


ips = extract_unique_ips("ips.log")
print(ips)
