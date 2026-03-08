import os
import re
import argparse
import logging
from datetime import datetime

def loadRegex():
    regexes = {
        "Github Access Token": r"ghp_[A-Za-z0-9]{36}",
        "Google API Key": r"AIza[0-9A-Za-z\-_]{35}",
        "Instagram Auth Token": r"[0-9a-fA-F]{7}\.[0-9a-fA-F]{32}",
        "Twitter Access Token": r"access_token\$production\$[0-9a-z]{16}\$[0-9a-z]{32}",
        "Password": r"password\s*=\s*['\"].+?['\"]"
    }
    return regexes

def scanFile(filepath, regexes):
    output = []

    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as file:
            lines = file.readlines()

            for lineNumber, line in enumerate(lines, start=1):
                for name, regex in regexes.items():
                    matches = re.findall(regex, line)

                    for match in matches:
                        foundAt = datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")
                        message = f"WARNING - Secret detected at {foundAt} in {filepath} line {lineNumber}"
                        logging.warning(message)
                        output.append((filepath, lineNumber, name, match))
    except Exception as e:
        logging.error(f"Error reading {filepath}: {e}")
    return output

def printOutput(output):
    if not output:
        print("No secrets found.")
        return
    
    print("\nScan Report")
    print("------------------")

    for file, line, secretType, match in output:
        print(f"File: {file}")
        print(f"Line: {line}")
        print(f"Type: {secretType}")
        print(f"Match: {match}")

def main():
    parser = argparse.ArgumentParser(description="Secret Scanner")
    parser.add_argument("path", help="File or directory to scan")
    args = parser.parse_args()

    logging.basicConfig(
        filename="scanner.log",
        level=logging.WARNING,
        format="%(message)s"
    )

    regexes = loadRegex()
    path = args.path
    results = []

    if os.path.isfile(path):
        results.extend(scanFile(path, regexes))

    elif os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for file in files:
                filepath = os.path.join(root, file)
                results.extend(scanFile(filepath, regexes))

    else:
        print("Invalid path.")
        return
    
    printOutput(results)


if __name__ == "__main__":
    main()