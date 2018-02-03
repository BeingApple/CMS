from cms.database import db
from sqlalchemy_utils import UUIDType


class Item(db.Model):
    __tablename__ = 'item'

    id = db.Column(UUIDType(binary=False), primary_key=True)
    name = db.Column(db.Text)
    unit_price = db.Column(db.Numeric)

    def __init__(self, id=None, name=None, unit_price=None):
        self.id = id
        self.name = name
        self.unit_price = unit_price

    def __repr__(self):
        return "<Item %r>" % self.id
