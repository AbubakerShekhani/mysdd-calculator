# Calculator Module Specification

This document outlines the complete specification for the basic calculator module.

## 1. What makes this a good specification?

1.  **User-Centric:** Starts with user stories (why features exist)
2.  **Type-Explicit:** Clear signatures with Python 3.12+ union types
3.  **Edge-Case Complete:** Documents all "gotcha" behaviors
4.  **Testable:** Concrete test scenarios, not prose descriptions
5.  **Scoped:** Explicitly states what's out of scope
6.  **Unambiguous:** No room for interpretation (e.g., "division always returns float")

## 2. General Behavior

### Return Types
For `add`, `subtract`, and `multiply`, the return type will be `float` if any of the input operands is a `float`. The return type will be `int` only if all inputs are integers. The `divide` function always returns a `float`.

### Floating-Point Precision (IEEE 754)
All operations involving floats adhere to standard IEEE 754 floating-point arithmetic. This means that some operations may have small precision errors. For example, `0.1 + 0.2` will result in a value that is approximately `0.3` (e.g., `0.30000000000000004`).

## 3. User Stories & Acceptance Criteria

### User Story: Addition

> As a developer, I want to add two numbers, so that I can find their sum.

**Function Signature:**
`--
def add(a: int | float, b: int | float) -> int | float:
`--

**Acceptance Criteria:**

*   **Happy path (integers)**
    *   GIVEN two integers `a = 5` and `b = 10`
    *   WHEN the `add` function is called with `a` and `b`
    *   THEN the result is `15`

*   **Happy path (floats)**
    *   GIVEN two floats `a = 3.5` and `b = 2.1`
    *   WHEN the `add` function is called with `a` and `b`
    *   THEN the result is `5.6`

*   **Type handling (mixed types)**
    *   GIVEN an integer `a = 5` and a float `b = 2.5`
    *   WHEN the `add` function is called with `a` and `b`
    *   THEN the result is `7.5`

*   **Edge case (zero)**
    *   GIVEN an integer `a = 10` and `b = 0`
    *   WHEN the `add` function is called with `a` and `b`
    *   THEN the result is `10`

*   **Edge case (negative numbers)**
    *   GIVEN two negative integers `a = -10` and `b = -5`
    *   WHEN the `add` function is called with `a` and `b`
    *   THEN the result is `-15`

*   **Edge case (large numbers)**
    *   GIVEN two large integers `a = 1_000_000_000` and `b = 2_000_000_000`
    *   WHEN the `add` function is called with `a` and `b`
    *   THEN the result is `3_000_000_000`

*   **Error case (invalid types)**
    *   GIVEN an integer `a = 10` and a string `b = "5"`
    *   WHEN the `add` function is called with `a` and `b`
    *   THEN a `TypeError` is raised

### User Story: Subtraction

> As a developer, I want to subtract two numbers, so that I can find their difference.

**Function Signature:**
`--
def subtract(a: int | float, b: int | float) -> int | float:
`--

**Acceptance Criteria:**

*   **Happy path (integers)**
    *   GIVEN two integers `a = 10` and `b = 5`
    *   WHEN the `subtract` function is called with `a` and `b`
    *   THEN the result is `5`

*   **Edge case (negative result)**
    *   GIVEN two integers `a = 5` and `b = 10`
    *   WHEN the `subtract` function is called with `a` and `b`
    *   THEN the result is `-5`

*   **Edge case (negative numbers)**
    *   GIVEN two negative integers `a = -10` and `b = -5`
    *   WHEN the `subtract` function is called with `a` and `b`
    *   THEN the result is `-5`

*   **Error case (invalid types)**
    *   GIVEN an integer `a = 10` and a string `b = "5"`
    *   WHEN the `subtract` function is called with `a` and `b`
    *   THEN a `TypeError` is raised

### User Story: Multiplication

> As a developer, I want to multiply two numbers, so that I can find their product.

**Function Signature:**
`--
def multiply(a: int | float, b: int | float) -> int | float:
`--

**Acceptance Criteria:**

*   **Happy path (integers)**
    *   GIVEN two integers `a = 5` and `b = 10`
    *   WHEN the `multiply` function is called with `a` and `b`
    *   THEN the result is `50`

*   **Edge case (zero)**
    *   GIVEN an integer `a = 10` and `b = 0`
    *   WHEN the `multiply` function is called with `a` and `b`
    *   THEN the result is `0`

*   **Edge case (negative number)**
    *   GIVEN a positive integer `a = 10` and a negative integer `b = -5`
    *   WHEN the `multiply` function is called with `a` and `b`
    *   THEN the result is `-50`

*   **Error case (invalid types)**
    *   GIVEN an integer `a = 10` and a string `b = "5"`
    *   WHEN the `multiply` function is called with `a` and `b`
    *   THEN a `TypeError` is raised

### User Stories: Division & Error Handling

> As a developer, I want to divide two numbers, so that I can find their quotient.
>
> As a developer, I want to be notified when I try to divide by zero, so that I can handle the error gracefully.

**Function Signature:**
`--
def divide(a: int | float, b: int | float) -> float:
`--

**Acceptance Criteria:**

*   **Happy path (integers)**
    *   GIVEN two integers `a = 10` and `b = 5`
    *   WHEN the `divide` function is called with `a` and `b`
    *   THEN the result is `2.0`

*   **Happy path (float result)**
    *   GIVEN two integers `a = 5` and `b = 2`
    *   WHEN the `divide` function is called with `a` and `b`
    *   THEN the result is `2.5`

*   **Edge case (zero numerator)**
    *   GIVEN an integer `a = 0` and an integer `b = 10`
    *   WHEN the `divide` function is called with `a` and `b`
    *   THEN the result is `0.0`

*   **Error case (division by zero)**
    *   GIVEN an integer `a = 10` and `b = 0`
    *   WHEN the `divide` function is called with `a` and `b`
    *   THEN a `ValueError` is raised with the message "Cannot divide by zero."

*   **Error case (invalid types)**
    *   GIVEN an integer `a = 10` and a string `b = "2"`
    *   WHEN the `divide` function is called with `a` and `b`
    *   THEN a `TypeError` is raised

## 4. Out of Scope

The following items are explicitly out of scope for this module:

*   **Complex numbers:** The calculator only supports integers and floats.
*   **Arbitrary precision arithmetic:** Standard Python floating-point precision is used.
*   **Scientific calculator functions:** Trigonometric, logarithmic, and exponential functions are not included.
*   **Expression parsing:** The module does not parse strings like `"2 + 2"`. It only operates on numbers directly via function calls.
*   **User Interface (UI):** This is a library/module, not a standalone application.
