from cms.database import db
from sqlalchemy_utils import UUIDType


class Order(db.Model):
    __tablename__ = 'order'

    id = db.Column(UUIDType(binary=False), primary_key=True)
    created_at = db.Column(db.TIMESTAMP)
    store_id = db.Column(UUIDType(binary=False))
    user_id = db.Column(UUIDType(binary=False))

    def __init__(self, id=None, created_at=None, store_id=None, user_id=None):
        self.id = id
        self.created_at = created_at
        self.store_id = store_id
        self.user_id = user_id

    def __repr__(self):
        return "<Order %r>" % self.id
