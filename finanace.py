class FinanceManager:
    def __init__(self):
        self.incomes = []
        self.expenses = []

    def add_income(self, amount, source):
        self.incomes.append({'amount': amount, 'source': source})

    def add_expense(self, amount, category):
        self.expenses.append({'amount': amount, 'category': category})

    def get_total_income(self):
        return sum(income['amount'] for income in self.incomes)

    def get_total_expenses(self):
        return sum(expense['amount'] for expense in self.expenses)

    def get_budget(self):
        return self.get_total_income() - self.get_total_expenses()

    def print_summary(self):
        print("Incomes:")
        for income in self.incomes:
            print(f"  {income['source']}: {income['amount']}")
        print("Expenses:")
        for expense in self.expenses:
            print(f"  {expense['category']}: {expense['amount']}")
        print(f"Total Income: {self.get_total_income()}")
        print(f"Total Expenses: {self.get_total_expenses()}")
        print(f"Budget: {self.get_budget()}")

# Create a finance manager instance
finance_manager = FinanceManager()

# Add incomes and expenses
finance_manager.add_income(5000, "Salary")
finance_manager.add_income(1000, "Investments")
finance_manager.add_expense(2000, "Rent")
finance_manager.add_expense(500, "Food")
finance_manager.add_expense(1000, "Transportation")

# Print summary
finance_manager.print_summary()
