from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from cms.create_app import get_app


app = get_app()


@app.route("/")
def index():
    return redirect(url_for("customer_list"))


@app.route("/customer_list/")
def customer_list():
    return render_template("customer_list.html")