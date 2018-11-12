#Database creator?

from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///tools.db', echo=True)
Base = declarative_base()

class Tool(Base):
    __tablename__ = 'tools'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return '{}'.format(self.name)

class Bin(Base):
    """"""
    __tablename__ = 'bins'

    id = Column(Integer, primary_key=True)
    location = Column(String)

    partnumber_id = Column(Integer, ForeignKey('tools.id'))
    partnumber = relationship('Tool', backref=backref('bins', order_by=id))

#create tables??
Base.metadata.create_all(engine)
