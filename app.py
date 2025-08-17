from flask import Flask, render_template, request, redirect, url_for

from yandex_market import list_orders, deliver_digital_goods

app = Flask(__name__)


@app.route("/")
def orders():
    data = list_orders()
    orders = data.get("orders", [])
    return render_template("orders.html", orders=orders)


@app.post("/deliver/<int:order_id>")
def deliver(order_id: int):
    item_id = int(request.form["item_id"])
    codes = [c.strip() for c in request.form["codes"].split(",") if c.strip()]
    deliver_digital_goods(order_id, [{"id": item_id, "codes": codes}])
    return redirect(url_for("orders"))


if __name__ == "__main__":
    app.run(debug=True)
