from flask import Flask, render_template, request # type: ignore

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        drink = request.form["drink"]
        milk = request.form["milk"]
        size = request.form["size"]
        sweetener = request.form["sweetener"]

        order_summary = f"Your order: {size} {drink} with {milk} and {sweetener}."
        return render_template("order_confirmation.html", order=order_summary)  #Render order confirmation page
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)