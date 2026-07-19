# Monthly Financial Goal Planner

YouTube Presentation Link: 

## Project Overview

The Monthly Financial Goal Planner is a terminal-based Python application that helps users organize their monthly finances and monitor savings goals.

Users can enter monthly income, record fixed and variable expenses, create multiple savings goals, add contributions, and view a complete financial summary. The application also estimates how many months it will take to complete each goal based on its planned monthly contribution.

Financial information can be saved to a JSON file and automatically loaded when the program starts again.

## Features

- Set monthly income
- Add fixed and variable expenses
- Create multiple savings goals
- Add contributions to individual goals
- Calculate fixed expenses
- Calculate variable expenses
- Calculate total expenses
- Calculate remaining monthly income
- Display savings-goal progress
- Calculate the remaining amount for each goal
- Estimate months needed to complete each goal
- Save the complete financial plan to JSON
- Automatically load previously saved data
- Validate menu selections and numeric input
- Reject invalid expense types and savings-goal selections

## Python Concepts Demonstrated

This project applies concepts from Chapters 8–11, including:

- Classes and objects
- Object-oriented programming
- Lists and dictionaries
- Loops and conditional statements
- Functions and helper functions
- Exception handling with `try` and `except`
- Reading and writing JSON data
- File handling with `pathlib.Path`
- Imports and multiple Python modules
- Input validation
- Formatted strings
- The `math` module
- The `if __name__ == "__main__":` pattern

## Project Files

- `main.py` — Runs the menu and handles user interaction
- `expense.py` — Defines the `Expense` class
- `savings_goal.py` — Defines the `SavingsGoal` class
- `financial_plan.py` — Manages income, expenses, goals, and JSON persistence
- `financial_plan.json` — Stores saved financial-plan data
- `.gitignore` — Excludes unnecessary development files
- `README.MD` — Explains the project and its features

## How to Run the Program

### Requirements

- Python 3
- No external packages are required

### Clone the Repository

```bash
git clone https://github.com/a1990alpalo/Project_8_11_amedina6.git
cd Project_8_11_amedina6
```

### Run the Application

```bash
python main.py
```

## Program Menu

```text
Monthly Financial Goal Planner
1. Set monthly income
2. Add an expense
3. Create a savings goal
4. Add a contribution
5. View financial summary
6. Save the financial plan
7. Exit
```

## Example Financial Summary

```text
Financial Summary
Monthly income: $4500.00
Fixed expenses: $1200.00
Variable expenses: $400.00
Total expenses: $1600.00
Remaining income: $2900.00

Savings Goals
- Emergency Fund: $750.00 saved of $5000.00 (15.0% complete)
  Remaining amount: $4250.00
  Planned monthly contribution: $500.00
  Estimated completion: 9 months
```

## Saving and Loading Data

Choose option `6` to save the current financial plan to `financial_plan.json`.

The saved information includes:

- Monthly income
- All expenses
- Expense types
- Savings-goal names
- Target amounts
- Current saved amounts
- Planned monthly contributions

The program automatically attempts to load `financial_plan.json` when it starts, allowing the user to continue working with previously saved information.

## Input Validation

The application includes validation to prevent common errors:

- Monetary amounts must be positive numbers
- Expense types must be `fixed` or `variable`
- Menu choices must be between `1` and `7`
- Savings-goal selections must correspond to an available goal
- Invalid numeric input displays a friendly message instead of crashing the program

## Future Improvements

Possible future additions include:

- Edit or delete expenses
- Edit or delete savings goals
- Automatically save changes when exiting
- Display monthly financial reports
- Add a graphical user interface
- Add automated tests

## Author

Alberto Medina