from cms.database import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref
from sqlalchemy_utils import UUIDType


class OrderItem(db.Model):
    __tablename__ = 'order_item'

    id = db.Column(UUIDType(binary=False), primary_key=True)
    order_id = db.Column(UUIDType(binary=False), ForeignKey('order.id'))
    item_id = db.Column(UUIDType(binary=False), ForeignKey('item.id'))

    order = relationship("Order", backref=backref('order_item', order_by=id))
    item = relationship("Item", backref=backref('order_item', order_by=id))

    def __init__(self, id=None, order_id=None, item_id=None):
        self.id = id
        self.order_id = order_id
        self.item_id = item_id

    def __repr__(self):
        return "<OrderItem %r>" % self.id
