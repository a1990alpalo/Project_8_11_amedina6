import json
from pathlib import Path


from expense import Expense
from savings_goal import SavingsGoal


class FinancialPlan: 
    """Manage income, expense, and savings goals."""

    def __init__(self) -> None:
        """Starts an empty financial plan."""
        self.monthly_income = 0.00
        self.expenses = []
        self.savings_goals = []

    def set_monthly_income(self, amount):
        """Set monthly income amount."""
        self.monthly_income = amount

    def add_expense(self, expense):
        """Add an expense to the financial plan."""
        self.expenses.append(expense)

    def add_savings_goal(self, savings_goal):
        """Add a savings goal to the financial plan."""
        self.savings_goals.append(savings_goal)

    def get_total_expenses(self):
        """Return the total amount of all expenses."""
        return sum(expense.amount for expense in self.expenses)
    
    def get_fixed_expenses(self):
        """Return the total amount of fixed expenses."""
        return sum(
            expense.amount
            for expense in self.expenses
            if expense.expense_type == "fixed"
        )
    
    def get_variable_expenses(self):
        """Return the total amount of variable expenses."""
        return sum(
            expense.amount
            for expense in self.expenses
            if expense.expense_type == "variable"
        )
    
    def get_remaining_income(self):
        """Return the monthly income remaining after expenses."""
        return self.monthly_income - self.get_total_expenses()
    
    def to_dictionary(self): 
        """Return the complete financial plan as a dictionary."""
        return {
            "monthly_income": self.monthly_income, 
            "expenses": [
                expense.to_dictionary()
                for expense in self.expenses
            ],
            "savings_goals": [
                savings_goal.to_dictionary()
                for savings_goal in self.savings_goals
            ]
        }
    def save_to_file(self, filename="financial_plan.json"):
        """Save the financial plan to a JSON file."""

        file_path = Path(filename)
        plan_data = self.to_dictionary()

        file_path.write_text(
            json.dumps(plan_data, indent=4),
            encoding = "utf-8",
        )
        
    
if __name__ == "__main__": 
    financial_plan = FinancialPlan()

    financial_plan.set_monthly_income(4500.00)

    rent = Expense("Rent", 1200.00, "fixed")
    groceries = Expense("Groceries", 400.00, "variable")

    financial_plan.add_expense(rent)
    financial_plan.add_expense(groceries)

    emergency_fund = SavingsGoal("Emergency Fund", 5000.00)
    financial_plan.add_savings_goal(emergency_fund)


    print(f"Monthly income: ${financial_plan.monthly_income:.2f}")
    print(f"Total expenses: ${financial_plan.get_total_expenses():.2f}")
    print(f"Remaining income: ${financial_plan.get_remaining_income():.2f}")
    print(f"Savings goals: {len(financial_plan.savings_goals)}")
    print(f"Fixed expenses: ${financial_plan.get_fixed_expenses():.2f}")
    print(f"Variable expenses: " 
          f"${financial_plan.get_variable_expenses():.2f}"
    )
    print(financial_plan.to_dictionary())
    financial_plan.save_to_file()
    print("Financial plan saved successfully.")