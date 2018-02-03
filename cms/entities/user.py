from cms.database import db
from sqlalchemy_utils import UUIDType


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(UUIDType(binary=False), primary_key=True)
    name = db.Column(db.Text)
    gender = db.Column(db.Text)
    age = db.Column(db.Numeric)
    ages = db.Column(db.Numeric)
    phone = db.Column(db.Text)
    birthdate = db.Column(db.Date)

    def __init__(self, id=None, name=None, gender=None, age=None, ages=None,
                 phone=None, birthdate=None):
        self.id = id
        self.name = name
        self.gender = gender
        self.age = age
        self.ages = ages
        self.phone = phone
        self.birthdate = birthdate

    def __repr__(self):
        return "<User %r>" % self.id


