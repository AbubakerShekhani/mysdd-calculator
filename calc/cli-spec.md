### CLI Specification: `calc_cli.py`

This document outlines the specification for a command-line interface (CLI) for the calculator module.

---

### 1. User Story

> As a command-line user, I want to perform a calculation by providing an operation name and two numbers as arguments, so that I can see the result printed directly to the console.

---

### 2. CLI Design and Acceptance Criteria

The command-line tool will be invoked as `python calc_cli.py <operation> <num1> <num2>`.

**Acceptance Criteria:**

*   **Happy path (addition)**
    *   GIVEN the command-line arguments `add 5 3`
    *   WHEN the script is executed
    *   THEN the script prints `Result: 8` to standard output and exits with a `0` status code.

*   **Happy path (division with floats)**
    *   GIVEN the command-line arguments `divide 12.5 2.5`
    *   WHEN the script is executed
    *   THEN the script prints `Result: 5.0` to standard output and exits with a `0` status code.

*   **Error case (Division by Zero)**
    *   GIVEN the command-line arguments `divide 10 0`
    *   WHEN the script is executed
    *   THEN the script prints `Error: Cannot divide by zero.` to **standard error** and exits with a non-zero status code.

*   **Error case (Invalid Operation)**
    *   GIVEN the command-line arguments `power 2 3`
    *   WHEN the script is executed
    *   THEN the script prints a usage error (e.g., `argument operation: invalid choice: 'power'`) to **standard error** and exits with a non-zero status code.

*   **Error case (Not enough numeric arguments)**
    *   GIVEN the command-line arguments `add 5`
    *   WHEN the script is executed
    *   THEN the script prints a usage error (e.g., `the following arguments are required: numbers`) to **standard error** and exits with a non-zero status code.

*   **Error case (Invalid number type)**
    *   GIVEN the command-line arguments `add 5 five`
    *   WHEN the script is executed
    *   THEN the script prints a usage error (e.g., `argument numbers: invalid float value: 'five'`) to **standard error** and exits with a non-zero status code.

*   **Help command**
    *   GIVEN the command-line argument `-h` or `--help`
    *   WHEN the script is executed
    *   THEN the script prints a helpful usage message describing the available commands and arguments, then exits gracefully.
