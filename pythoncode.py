import tkinter as tk

class ATM:
    def __init__(self, balance=1000):
        self.balance = balance

    def check_balance(self):
        return f"Balance: ${self.balance}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount. Please enter a positive value."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        elif amount > self.balance:
            return "Insufficient funds. Cannot withdraw."
        else:
            return "Invalid withdrawal amount. Please enter a positive value."

def check_balance_click():
    result_label.config(text=atm.check_balance())

def deposit_click():
    amount = float(deposit_entry.get())
    result_label.config(text=atm.deposit(amount))

def withdraw_click():
    amount = float(withdraw_entry.get())
    result_label.config(text=atm.withdraw(amount))

atm = ATM()

# Create the main window
root = tk.Tk()
root.title("ATM Simulator")

# Create GUI components
balance_button = tk.Button(root, text="Check Balance", command=check_balance_click)
deposit_label = tk.Label(root, text="Deposit Amount:")
deposit_entry = tk.Entry(root)
deposit_button = tk.Button(root, text="Deposit", command=deposit_click)
withdraw_label = tk.Label(root, text="Withdraw Amount:")
withdraw_entry = tk.Entry(root)
withdraw_button = tk.Button(root, text="Withdraw", command=withdraw_click)
result_label = tk.Label(root, text="", padx=10, pady=10)

# Place GUI components on the window
balance_button.pack()
deposit_label.pack()
deposit_entry.pack()
deposit_button.pack()
withdraw_label.pack()
withdraw_entry.pack()
withdraw_button.pack()
result_label.pack()

# Start the Tkinter event loop
root.mainloop()