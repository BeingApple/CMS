from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
import uuid
from cms.create_app import get_app
from cms.service.service_user import ServiceUser
from cms.service.service_store import ServiceStore


app = get_app()


@app.route("/")
def index():
    return redirect(url_for("customer_list"))


@app.route("/customer_list/", methods=['GET', 'POST'])
def customer_list():
    return customer_list_page(0)


@app.route("/customer_list/<int:page>/", methods=['GET', 'POST'])
def customer_list_page(page):
    service_user = ServiceUser()
    service_store = ServiceStore()

    users = service_user.get_customer_list(page)
    count = service_user.get_count()
    pagination = service_user.get_pagination("/customer_list", page)
    stores = service_store.get_store_list()

    retention = 0
    order_count = 0

    search = {'store': '', 'start_date': '', 'end_date': ''}

    if request.method == 'POST':
        store = request.form['store']
        start_date = request.form['start_date']
        end_date = request.form['end_date']

        if store != '':
            search['store'] = uuid.UUID(store)
        if start_date != '':
            search['start_date'] = start_date
        if end_date != '':
            search['end_date'] = end_date

        if search['store'] != '' and search['start_date'] != '' and \
                search['end_date'] != '':
            retention = service_store.get_retention_percentage(
                search['store'],
                search['start_date'],
                search['end_date']
            )
            order_count = service_store.order_count

    return render_template("customer_list.html", users=users,
                           pagination=pagination, stores=stores,
                           search=search, retention=retention,
                           count=count, order_count=order_count)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
