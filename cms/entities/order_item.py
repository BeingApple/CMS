from cms.database import db
from sqlalchemy_utils import UUIDType


class OrderItem(db.Model):
    __tablename__ = 'order_item'

    id = db.Column(UUIDType(binary=False), primary_key=True)
    order_id = db.Column(UUIDType(binary=False))
    item_id = db.Column(UUIDType(binary=False))

    def __init__(self, id=None, order_id=None, item_id=None):
        self.id = id
        self.order_id = order_id
        self.item_id = item_id

    def __repr__(self):
        return "<OrderItem %r>" % self.id
