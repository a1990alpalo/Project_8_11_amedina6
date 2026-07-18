from expense import Expense
from financial_plan import FinancialPlan
from savings_goal import SavingsGoal

def display_menu():
    """Display the financial planner menu."""
    print("\nMonthly Financial Goal Planner")
    print("1. Set monthly income")
    print("2. Add an expense")
    print("3. Create a savings goal")
    print("4. Add a contribution")
    print("5. View financial summary")
    print("6. Save the financial plan")
    print("7. Exit")

def main():
    """Run the Monthly Financial Goal Planner."""
    financial_plan = FinancialPlan()

    while True:
        display_menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            amount = float(input("Enter your monthly income: $"))
            financial_plan.set_monthly_income(amount)
            print(f"Monthly income set to ${amount:.2f}.")

        elif choice == "2":
            name = input("enter the expense name: ")
            amount = float(input("Enter the expense amount: $"))
            expense_type = input(
                "Enter the expense type (fixed/variable):"
            ).strip().lower()

            expense = Expense(name, amount, expense_type)
            financial_plan.add_expense(expense)

            print(f"Expense added: {expense.get_summary()}")

        elif choice == "3":
            name = input("Enter the savings goal name: ")
            target_amount = float(
                input("Enter the target amount: $")
            )

            savings_goal = SavingsGoal(name, target_amount)
            financial_plan.add_savings_goal(savings_goal)

            print(
                f"Savings goal created: "
                f"{savings_goal.get_summary()}"
            )

        elif choice == "4":
            if not financial_plan.savings_goals:
                print("No savings goals are available")
                continue

            print("\nSavings goals: ")
            for number, goal in enumerate(
                financial_plan.savings_goals,
                start=1,
            ):
                print(f"{number}. {goal.name}")

            goal_number = int(
                input("Select a savings goal number: ")
            )
            
            selected_goal = financial_plan.savings_goals[
                goal_number - 1
            ]

            amount = float(input("Enter contribution amount: $"))
            selected_goal.add_contribution(amount)

            print(
                f"Contribution added: "
                f"{selected_goal.get_summary()}"
            )
        
        elif choice == "5":
            print("\nFinancial Summary")
            print(
                f"Monthly income: "
                f"${financial_plan.monthly_income:.2f}"
            )
            print(
                f"Fixed expenses: "
                f"${financial_plan.get_fixed_expenses():.2f}"
            )
            print(
                f"Variable expenses: "
                f"${financial_plan.get_fixed_expenses():.2f}"
            )
            print(
                f"Total expenses: "
                f"${financial_plan.get_total_expenses():.2f}"
            )
            print(
                f"Remaining income: "
                f"${financial_plan.get_remaining_income():.2f}"
            )

        elif choice == "7":
            print("Thank you for using the financial planner.")
            break


if __name__ == "__main__":
    main()