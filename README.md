# Bank Management System

A console-based banking simulation built in Python. This application allows users to manage multiple bank accounts with full CRUD functionality, including deposits, withdrawals, transfers, ATM withdrawals, and coin deposits.

## ✨ Features

- **Open New Accounts** — Auto-generates unique 8-digit account numbers and 4-digit PINs
- **Account Management** — View balance and details (with masked SSN)
- **Transactions**:
  - Deposit money (dollars and cents)
  - Withdraw money
  - Transfer between accounts
  - ATM Withdrawal (dispenses in $20, $10, $5 bills)
  - Deposit coins (P, N, D, Q, H, W)
- **Security Features**:
  - PIN validation
  - Account number lookup
- **Extra Features**:
  - Add monthly interest to all accounts
  - Close accounts
  - Input validation throughout

## 🛠️ Technologies

- **Python 3**
- Object-Oriented Programming (Classes & Encapsulation)
- Regular Expressions (for coin parsing)
- Random number generation for account/PIN creation

## 📁 Project Structure

```
BankingSystem/
├── BankManager.py      # Main program logic and menu
├── Bank.py             # Bank class (manages accounts)
├── Account.py          # Account class (individual accounts)
├── BankUtility.py      # Utility functions (input, conversions, validation)
├── CoinCollector.py    # Coin deposit parser
└── README.md
```

## 🚀 How to Run

1. Make sure all Python files are in the same folder.
2. Run the main file:

```bash
python BankManager.py
```

3. Follow the on-screen menu to navigate.

## 📋 Available Operations

| Option | Description |
|--------|-----------|
| 1 | Open a new account |
| 2 | Get account information & balance |
| 3 | Change PIN |
| 4 | Deposit money |
| 5 | Transfer money between accounts |
| 6 | Withdraw money |
| 7 | ATM withdrawal (multiples of $5) |
| 8 | Deposit change (coins) |
| 9 | Close an account |
| 10 | Add monthly interest to all accounts |
| 11 | Exit program |

## 🔑 Key Classes

- **`Account`** — Stores account details with private attributes
- **`Bank`** — Manages up to 100 accounts
- **`BankUtility`** — Handles user input, conversions, and validations
- **`CoinCollector`** — Parses coin strings (P, N, D, Q, H, W)
- **`BankManager`** — Main controller and menu system

## 💡 Notable Implementations

- Strong input validation and error handling
- Proper encapsulation (private attributes with getters/setters)
- Custom `__eq__` and `__repr__` methods in Account class
- Masked SSN display for privacy

---

**Author**: Ben Fullenkamp
