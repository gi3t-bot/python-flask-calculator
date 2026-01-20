from flask import Flask, render_template, request
from Calculator_w_history.calculator import evaluate_and_save

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = ""
    expression = ""

    if request.method == "POST":
        expression = request.form.get("display", "")
        try:
            result = evaluate_and_save(expression)
        except Exception:
            result = "Error"

    return render_template(
        "calculator.html",
        result=result,
        expression=expression
    )

if __name__ == "__main__":
    app.run(debug=True)
