# Initialize global variables for balance, PIN, and transaction history
balance = 5000 #available balance in the Ac.
pin = 1122 # password 
transaction_history = []

# Function to check PIN
def check_pin():
    entered_pin = int(input("Enter your PIN: "))
    if entered_pin == pin:
        return True
    else:
        print("Incorrect PIN.")
        return False

# Function to display balance inquiry
def balance_inquiry():
    global balance
    print(f"Your account balance is: ₹{balance}")
    transaction_history.append("Balance Inquiry")

# Function for cash withdrawal
def cash_withdrawal():
    global balance
    amount = int(input("Enter the amount to withdraw: ₹"))
    if amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount  # Deduct the amount from balance
        print(f"₹{amount} withdrawn successfully.")
        print(f"Remaining balance: ₹{balance}")
        transaction_history.append(f"Withdrawal of ₹{amount}")

# Function for cash deposit
def cash_deposit():
    global balance
    amount = int(input("Enter the amount to deposit: ₹"))
    balance += amount  # Add the deposited amount to balance
    print(f"₹{amount} deposited successfully.")
    print(f"New balance: ₹{balance}")
    transaction_history.append(f"Deposit of ₹{amount}")

# Function to change PIN
def pin_change():
    global pin
    current_pin = int(input("Enter current PIN: "))
    if current_pin == pin:
        new_pin = int(input("Enter new PIN: "))
        confirm_pin = int(input("Confirm new PIN: "))
        if new_pin == confirm_pin:
            pin = new_pin  # Change the pin
            print("PIN changed successfully.")
            transaction_history.append("PIN changed")
        else:
            print("PIN mismatch. Please try again.")
    else:
        print("Incorrect current PIN.")

# Function to view transaction history
def view_transaction_history():
    if not transaction_history:
        print("No transactions found.")
    else:
        print("Transaction History:")
        for transaction in transaction_history:
            print(f"- {transaction}")

# ATM menu function to provide the user with options
def atm_menu():
    if not check_pin():  # If PIN check fails, return and exit the program
        return
    
    while True:
        print("\n---- ATM Menu ----")
        print("1. Balance Inquiry")
        print("2. Cash Withdrawal")
        print("3. Cash Deposit")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")
        
        choice = int(input("Choose an option: "))  # Take user input for menu choice

        # Call the appropriate function based on user’s choice
        if choice == 1:
            balance_inquiry()
        elif choice == 2:
            cash_withdrawal()
        elif choice == 3:
            cash_deposit()
        elif choice == 4:
            pin_change()
        elif choice == 5:
            view_transaction_history()
        elif choice == 6:
            print("Thank you for using the ATM!")
            break  # Exit the loop and end the program
        else:
            print("Invalid option. Please try again.")

# Start the ATM menu when the program runs
atm_menu()
