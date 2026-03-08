# Secret Scanner

## Description
This Python program scans files or directories for possible hardcoded secrets such as API keys, passwords, tokens, and other sensitive information. Hardcoded secrets in source code can create security vulnerabilities, so this tool helps identify them using pattern matching.

## How It Works
The program uses regular expressions to search for common secret patterns. Each file is read line by line and checked against a set of predefined regex patterns. If a match is found, the program records the filename, line number, type of secret detected, and the matched string.

The tool can scan either a single file or all files within a directory.

## Detected Secret Types
The scanner currently checks for the following patterns:

- Github Access Tokens
- Google API Keys
- Instagram Authentication Tokens
- Twitter Access Tokens
- Hardcoded Passwords

## How To Use:
Run the program from the command line and provide a file or directory path.

Example:

python scanner.py myfile.py

or

python scanner.py myproject/

## Output
If secrets are detected, the program will display:

- File name
- Line number
- Type of secret
- The matched string

All detections are also recorded in a log file named scanner.log.