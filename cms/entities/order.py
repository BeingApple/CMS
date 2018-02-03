from cms.database import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref
from sqlalchemy_utils import UUIDType


class Order(db.Model):
    __tablename__ = 'order'

    id = db.Column(UUIDType(binary=False), primary_key=True)
    created_at = db.Column(db.TIMESTAMP)
    store_id = db.Column(UUIDType(binary=False), ForeignKey('store.id'))
    user_id = db.Column(UUIDType(binary=False), ForeignKey('user.id'))

    user = relationship("User", backref=backref('order', order_by=id))
    store = relationship("Store", backref=backref('order', order_by=id))

    def __init__(self, id=None, created_at=None, store_id=None, user_id=None):
        self.id = id
        self.created_at = created_at
        self.store_id = store_id
        self.user_id = user_id

    def __repr__(self):
        return "<Order %r>" % self.id
