# Expense Tracker (Flask Mini Project)

A simple web app built with Python Flask to record expenses and see how much is spent in each category.

## Features
- Add an expense (title, amount, category) using an HTML form
- View all expenses with a running total
- View total spending per category
- Input validation with friendly error messages (blank title, non-numeric or negative amount, etc.)

## Routes
| Route | Method | Description |
|---|---|---|
| `/` | GET | Home page: form and list of expenses |
| `/add` | POST | Validates the form and saves the expense, shows the result page |
| `/summary` | GET | Category-wise totals |
| `/about` | GET | About page |

## How to Run
1. Open a terminal in the project folder.
2. Create and activate a virtual environment:
   - Windows: `python -m venv venv` then `venv\Scripts\activate`
   - Mac/Linux: `python3 -m venv venv` then `source venv/bin/activate`
3. Install Flask: `pip install -r requirements.txt`
4. Start the app: `python app.py`
5. Open http://127.0.0.1:5000 in your browser.

## Testing Done
- Valid input: expense is saved and shown on the result page
- Empty title / empty amount: error message shown
- Text in amount ("abc"): error message shown
- Zero or negative amount: error message shown

## Notes
Expenses are stored in a Python list, so they reset when the server restarts. No database or secret keys are used.

## Screenshots
(Add your screenshots here)
