from cms.database import db
from sqlalchemy.sql import func
from sqlalchemy import between
from cms.entities.store import Store
from cms.entities.user import User
from cms.entities.order import Order


class ServiceStore:

    retention_count = 0
    order_count = 0

    def get_store_list(self):
        return db.session.query(Store).order_by(Store.name)

    def set_order_count(self, store_id, start_date, end_date):
        self.order_count = db.session.query(Order). \
            filter(Order.store_id == store_id). \
            filter(between(Order.created_at, start_date, end_date)).\
            count()

    def set_retention_count(self, store_id, start_date, end_date):
        stmt = db.session.query(User, func.count(Order.id).label('cnt')).\
            outerjoin(Order).\
            filter(Order.store_id == store_id).\
            filter(between(Order.created_at, start_date, end_date)).\
            group_by(User.id).\
            subquery()

        self.retention_count = db.session.query(stmt).\
            select_entity_from(stmt).filter('cnt >= 2').count()

    def get_retention_percentage(self, store_id, start_date, end_date):
        self.set_retention_count(store_id, start_date, end_date)
        self.set_order_count(store_id, start_date, end_date)

        try:
            return round((self.retention_count / self.order_count) * 100, 2)
        except ZeroDivisionError:
            return 0
