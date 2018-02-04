from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
from flask import flash
import uuid
from cms.create_app import get_app
from cms.service.service_user import ServiceUser
from cms.service.service_store import ServiceStore


app = get_app()
app.config.from_object('config.config')


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

    retention = 0
    order_count = 0

    # ROW BLOCK LIST
    row_block_list = [10, 20, 50, 100, 200]

    # FILTER
    search = {'store': '', 'start_date': '', 'end_date': '',
              'row_block': service_user.get_row_block()}

    if request.method == 'POST':
        store = request.form['store']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        row_block = request.form['row_block']

        if store != '':
            search['store'] = uuid.UUID(store)
        if start_date != '':
            search['start_date'] = start_date
        if end_date != '':
            search['end_date'] = end_date
        if row_block != '':
            search['row_block'] = int(row_block)

        # ROW BLOCK 변경
        if search['row_block'] != '':
            service_user.set_row_block(search['row_block'])

            message = "조회 수가 " + row_block + "개로 변경되었습니다."
            flash(message, "success")

        # 매장 FILTER 변경
        if search['store'] != '' and search['start_date'] != '' and \
                search['end_date'] != '':
            retention = service_store.get_retention_percentage(
                search['store'],
                search['start_date'],
                search['end_date']
            )
            order_count = service_store.order_count
        elif search['store'] == '' or search['start_date'] == '' or \
                search['end_date'] == '':
            flash("조회하실 데이터를 모두 입력해주십시오", "warning")

    users = service_user.get_customer_list(page)
    count = service_user.get_count()
    pagination = service_user.get_pagination("/customer_list", page)
    stores = service_store.get_store_list()

    return render_template("customer_list.html", users=users,
                           pagination=pagination, stores=stores,
                           search=search, retention=retention,
                           count=count, order_count=order_count,
                           row_block_list=row_block_list)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
