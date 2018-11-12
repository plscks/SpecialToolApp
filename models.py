# models.py

from app import db

class Tool(db.Model):
    __tablename__ = 'tools'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __repr__(self):
        return '{}'.format(self.name)

class Bin(db.Model):
    """"""
    __tablename__ = 'bins'

    id = db.Column(db.Integer, primary_key=True)
    #part_number = db.Column(db.String)
    location = db.Column(db.String)

    partnumber_id = db.Column(db.Integer, db.ForeignKey("tools.id"))
    partnumber = db.relationship("Tool", backref=db.backref("bins", order_by=id), lazy=True)
