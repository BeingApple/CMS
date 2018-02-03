from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from cms.create_app import get_app
from cms.service.service_user import ServiceUser


app = get_app()


@app.route("/")
def index():
    return redirect(url_for("customer_list"))


@app.route("/customer_list/")
def customer_list():
    return customer_list_page(0)


@app.route("/customer_list/<int:page>/")
def customer_list_page(page):
    service_user = ServiceUser()

    users = service_user.get_customer_list(page)
    pagination = service_user.get_pagination("/customer_list", page)

    return render_template("customer_list.html", users=users,
                           pagination=pagination)


if __name__ == "__main__":
    app.run(host='0.0.0.0')