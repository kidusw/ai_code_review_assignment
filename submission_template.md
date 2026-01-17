# AI Code Review Assignment (Python)

## Candidate

- Name:Kidus Workneh Abebe
- Approximate time spent:1hr

---

# Task 1 — Average Order Value

## 1) Code Review Findings

### Critical bugs

- count = len(orders) considers all the orders whether they're cancelled or not, that would make the denominator incorrect as it would contain cancelled orders, thus making the final average value incorrect

- if orders list is empty it would lead to a zero division error

### Edge cases & risks

- negative amount values would result in incorrect average calculations
- invalid or incompatible amouunt values can result in application crashes

### Code quality / design issues

- the code doesn't address edge cases
- code can result in incorrect final outputs

## 2) Proposed Fixes / Improvements

### Summary of changes

- the improved code can handle edge cases, like handling negative amount values, checks whether the input types are of the correct type.

- the improved code utilizes one liners list comprehensions for concise and pythonic code design

### Corrected code

See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

### Testing Considerations

If you were to test this function, what areas or scenarios would you focus on, and why?

## 3) Explanation Review & Rewrite

### AI-generated explanation (original)

> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation

- the original explanation is more of a description than an explanation, it doesn't clearly explain the techniques used, why they were used

### Rewritten explanation

- This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of non cancelled orders orders. It handles most edge cases and risks that might result in code failure

## 4) Final Judgment

- Decision: Request Changes
- Justification:
- Confidence & unknowns:9

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings

### Critical bugs

- it will consider all string inputs which contain the @ symbol as valid email addresses.

### Edge cases & risks

- the current code doesn't consider incompatible types and how to handle them.

### Code quality / design issues

- the current code design is too simple and doesn't really address the required functionality

## 2) Proposed Fixes / Improvements

### Summary of changes

- the updated code uses regular expressions that can correctly identify valid email address
- the updated code can handle incompatible input types without crasing the program/ raising errors

### Corrected code

See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`.

### Testing Considerations

If you were to test this function, what areas or scenarios would you focus on, and why?

## 3) Explanation Review & Rewrite

### AI-generated explanation (original)

> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation

- the explanation cannot be used for the original code implementation, but it can be used for the improved implementaion

### Rewritten explanation

- no changes required

## 4) Final Judgment

- Decision:Request Changes
- Justification:
- Confidence & unknowns:9

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings

### Critical bugs

- the current implementation doesn't address the incompatible input types
- it doesn't address empty list values

### Edge cases & risks

- it doesn't address empty list values

### Code quality / design issues

-

## 2) Proposed Fixes / Improvements

### Summary of changes

- the code correctly address empty list values and correctly handles values which are incompatible

### Corrected code

See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations

If you were to test this function, what areas or scenarios would you focus on, and why?

## 3) Explanation Review & Rewrite

### AI-generated explanation (original)

> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation

- the explanation cannot be used for the original code implementation, but it can be used for the improved implementaion

### Rewritten explanation

- no changes required

## 4) Final Judgment

- Decision: Request Changes
- Justification:
- Confidence & unknowns:9
