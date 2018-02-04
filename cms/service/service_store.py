from cms.database import db
from sqlalchemy.sql import func
from sqlalchemy import between
from cms.entities.store import Store
from cms.entities.user import User
from cms.entities.order import Order


class ServiceStore:

    _retention_count = 0
    _order_count = 0

    def get_store_list(self):
        return db.session.query(Store).order_by(Store.name)

    def _set_order_count(self, store_id, start_date, end_date):
        self._order_count = db.session.query(Order). \
            filter(Order.store_id == store_id). \
            filter(between(Order.created_at, start_date, end_date)).\
            count()

    def get_order_count(self):
        return self._order_count

    def _set_retention_count(self, store_id, start_date, end_date):
        stmt = db.session.query(User, func.count(Order.id).label('cnt')).\
            outerjoin(Order).\
            filter(Order.store_id == store_id).\
            filter(between(Order.created_at, start_date, end_date)).\
            group_by(User.id).\
            subquery()

        self._retention_count = db.session.query(stmt).\
            select_entity_from(stmt).filter('cnt >= 2').count()

    def get_retention_percentage(self, store_id, start_date, end_date):
        self._set_retention_count(store_id, start_date, end_date)
        self._set_order_count(store_id, start_date, end_date)

        try:
            return round((self._retention_count / self._order_count) * 100, 2)
        except ZeroDivisionError:
            return 0

    def get_new_customer_count(self, store_id, start_date, end_date):
        stmt = db.session.query(User, func.count(Order.id).label('cnt')). \
            outerjoin(Order). \
            filter(Order.store_id == store_id). \
            filter(between(Order.created_at, start_date, end_date)). \
            group_by(User.id). \
            subquery()

        return db.session.query(stmt). \
            select_entity_from(stmt).filter('cnt = 1').count()
