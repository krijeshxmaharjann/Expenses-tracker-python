
from Expense_tracker import Expense, ExpensesTracker

def main():
    tracker = ExpensesTracker()
    
    while True:
        print("\nExpense Tracker Menu.")
        print("1. Add Expense")
        print("2. Remove Expense")
        print("3. View Expense")
        print("4. Total Expense")
        print("5. Exit")

        choice = int(input("Enter your choice (1-5): "))
        
        if choice == 1:
            date = input("Enter the  date (YYY-MM-DD): ")
            description = input("Enter the description: ")
            amount = float(input("Enter the Total amount of expense: "))
            new_expense = Expense(date, description, amount)
            tracker.add_expense(new_expense)
            print("Expense added successfully.")
        elif choice == 2:
            index = int(input("Enter the expense index to remove: ")) - 1
            tracker.remove_expenses(index)
        elif choice == 3:
            tracker.view_expenses()
        elif choice == 4:
            tracker.total_expenses()
        elif choice == 5:
            print("Goodbye!")
            break 
        else:
            print("Invalid choice. Please try again.")

if __name__ =="__main__":
    main()