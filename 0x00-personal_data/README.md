# Personal Data Backend Authentication

## Project Overview
This project is focused on enhancing backend authentication by securing personal data. It involves implementing logging, encryption, and secure database connections to handle sensitive information appropriately.

## Project Details
- **Start Date:** Jul 3, 2024, 4:00 AM
- **End Date:** Jul 5, 2024, 4:00 AM
- **Checker Release:** Jul 3, 2024, 4:00 PM
- **Manual QA Review:** Required
- **Auto Review:** Launched at the deadline

## Learning Objectives
By completing this project, you will be able to:
1. Identify Personally Identifiable Information (PII) and understand its importance.
2. Implement a log filter to obfuscate PII fields.
3. Encrypt passwords and validate them.
4. Authenticate securely to a database using environment variables.

## Project Requirements
- All code should be written in Python 3.7 and compatible with Ubuntu 18.04 LTS.
- All files must end with a new line.
- The first line of all files should be `#!/usr/bin/env python3`.
- The project must include a `README.md` file.
- Code must adhere to the `pycodestyle` style guide (version 2.5).
- All files must be executable.
- Documentation is required for all modules, classes, and functions.

## Project Tasks
1. **Regex-ing**: Implement a function to obfuscate specified fields in a log message using regex.
2. **Log Formatter**: Create a custom log formatter to filter sensitive information.
3. **Create Logger**: Develop a logger that only logs up to the INFO level and uses the custom formatter.
4. **Connect to Secure Database**: Securely connect to a MySQL database using environment variables.
5. **Read and Filter Data**: Implement a function to read data from the database and log it with obfuscated fields.
6. **Encrypting Passwords**: Implement a function to hash passwords using bcrypt.
7. **Check Valid Password**: Implement a function to validate passwords against their hashed values.

## Repository
- **GitHub Repository:** alx-backend-user-data
- **Directory:** 0x00-personal_data

## Usage
1. Clone the repository.
2. Navigate to the project directory.
3. Ensure all environment variables are set correctly.
4. Execute the main script to start the project.

## License
This project is licensed under the ALX License.
