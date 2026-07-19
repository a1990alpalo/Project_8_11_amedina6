"""
Program: Monthly Financial Goal Planner
Author: Alberto Medina
Purpose: Define the expense class used to represent a monthly expense.
Date: July 15,2026"""


class Expense:
    """Represent one fixed or variable monthly expense."""

    def __init__(self, name, amount, expense_type):
        """Initialize the expense name, amount, and type."""
        self.name = name
        self.amount = amount
        self.expense_type = expense_type

    def get_summary(self):
        """Return a formatted summary of the expense."""
        return (
            f"{self.name.title()}: ${self.amount:.2f} " f"({self.expense_type.title()})"
        )

    def to_dictionary(self):
        """Return the expense data as a dictionary."""
        return {
            "name": self.name,
            "amount": self.amount,
            "expense_type": self.expense_type,
        }


if __name__ == "__main__":
    rent = Expense("rent", 1200, "fixed")

    print(rent.get_summary())
    print(rent.to_dictionary())
