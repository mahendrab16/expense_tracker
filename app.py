from flask import Flask, render_template, request

app = Flask(__name__)

# Expenses are kept in memory (a simple list). They reset when the app restarts.
expenses = []

CATEGORIES = ["Food", "Travel", "Books", "Entertainment", "Other"]


def validate_expense(title, amount_text, category):
    """Check the form input. Returns (cleaned_data, error_message)."""
    title = title.strip()
    if not title:
        return None, "Please enter a title for the expense."
    if len(title) > 50:
        return None, "Title is too long (maximum 50 characters)."
    if not amount_text.strip():
        return None, "Please enter the amount."
    try:
        amount = float(amount_text)
    except ValueError:
        return None, "Amount must be a number, for example 150 or 99.50."
    if amount <= 0:
        return None, "Amount must be greater than zero."
    if category not in CATEGORIES:
        return None, "Please choose a valid category."
    return {"title": title, "amount": round(amount, 2), "category": category}, None


@app.route("/")
def home():
    """GET: show the form and all expenses added so far."""
    total = sum(e["amount"] for e in expenses)
    return render_template("index.html", expenses=expenses, total=total,
                           categories=CATEGORIES, error=None, form={})


@app.route("/add", methods=["POST"])
def add_expense():
    """POST: validate the form, save the expense and show the result."""
    title = request.form.get("title", "")
    amount_text = request.form.get("amount", "")
    category = request.form.get("category", "")

    data, error = validate_expense(title, amount_text, category)
    if error:
        total = sum(e["amount"] for e in expenses)
        return render_template("index.html", expenses=expenses, total=total,
                               categories=CATEGORIES, error=error,
                               form=request.form), 400

    expenses.append(data)
    total = sum(e["amount"] for e in expenses)
    return render_template("result.html", expense=data, total=total,
                           count=len(expenses))


@app.route("/summary")
def summary():
    """GET: total spending per category."""
    totals = {c: 0 for c in CATEGORIES}
    for e in expenses:
        totals[e["category"]] += e["amount"]
    grand_total = sum(totals.values())
    return render_template("summary.html", totals=totals, grand_total=grand_total)


@app.route("/about")
def about():
    """GET: about page."""
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
