from cms.database import db
from sqlalchemy_utils import UUIDType


class Store(db.Model):
    __tablename__ = 'store'

    id = db.Column(UUIDType(binary=False), primary_key=True)
    name = db.Column(db.Text)
    address = db.Column(db.Text)

    def __init__(self, id=None, name=None, address=None):
        self.id = id
        self.name = name
        self.address = address

    def __repr__(self):
        return "<Store %r>" % self.id
