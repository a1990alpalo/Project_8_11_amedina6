import math

class SavingsGoal:
    """Represents a financial savings goal."""

    def __init__(
            self, 
            name, 
            target_amount, 
            monthly_contribution=0.00
        ):
        
        """Initialize the savings goal."""
        self.name = name
        self.target_amount = target_amount
        self.monthly_contribution = monthly_contribution
        self.current_amount = 0.00

    def add_contribution(self, amount):
        """Add money to the designated savings goal."""
        self.current_amount += amount

    def get_remaining_amount(self):
        """Return the amount still needed to reach the goal."""
        return max(
            self.target_amount - self.current_amount,
             0.00,
            )
    
    def get_progress_percentage(self):
        """Return the percentage of the savings goal completed."""

        if self.target_amount == 0:
            return 100.00
        
        return min(
            (self.current_amount / self.target_amount) * 100,
            100.00,
        )
    
    def get_estimated_months(self):
        """Return the estimated months needed to complete the goal."""
        remaining_amount = self.get_remaining_amount()

        if remaining_amount == 0:
            return 0

        if self.monthly_contribution <= 0:
            return None

        return math.ceil(
            remaining_amount / self.monthly_contribution
        )
    
    def to_dictionary(self):
        """Return the savings goal data as a dictionary."""
        return {
            "name": self.name,
            "target_amount": self.target_amount,
            "monthly_contribution": self.monthly_contribution,
            "current_amount": self.current_amount,
        }
    
    def get_summary(self):
        """Return a formatted summary of the savings goal."""
        return (
            f"{self.name}: ${self.current_amount:.2f} saved "
            f"of ${self.target_amount:.2f} "
            f"({self.get_progress_percentage():.1f}% complete)"
        )
if __name__ == "__main__":
    emergency_fund = SavingsGoal(
        "Emergency Fund",
         5000.00,
         500.00,
        )

    emergency_fund.add_contribution(750.00)

    print(emergency_fund.get_summary())
    print(
        f"Remaining amount: "
        f"${emergency_fund.get_remaining_amount():.2f}"
    )
    print(
        f"Estimated months: "
        f"{emergency_fund.get_estimated_months()}"
    )