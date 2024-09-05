def main():
    transactions = []  # This will store all transactions
    balance = 0        # This will keep track of the current balance

    while True:
        print("Income and Expenditure Tracker")
        print("1. Add a Transaction")
        print("2. Display Transactions")
        print("3. Calculate Balance")
        print("4. Generate Report")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            balance = add_transaction(transactions, balance)
        elif choice == "2":
            display_transactions(transactions)
        elif choice == "3":
            print(f"Current Balance: {balance}")
        elif choice == "4":
            generate_report(transactions, balance)
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice! Please choose a valid option.")

def add_transaction(transactions, balance):
    trans_type = input("Is this an income or expenditure? (income/exp): ").lower()
    amount = float(input("Enter the amount: "))
    description = input("Enter a description: ")

    if trans_type == "income":
        transactions.append(f"Income: +{amount} - {description}")
        balance += amount
    elif trans_type == "exp":
        transactions.append(f"Expenditure: -{amount} - {description}")
        balance -= amount
    else:
        print("Invalid transaction type. Please enter 'income' or 'exp'.")

    return balance

def display_transactions(transactions):
    print("All Transactions")
    if transactions:
        for transaction in transactions:
            print(transaction)
    else:
        print("No transactions to display.")

def generate_report(transactions, balance):
    display_transactions(transactions)
    print(f"Final Balance: {balance}")

if __name__ == "__main__":
    main()
