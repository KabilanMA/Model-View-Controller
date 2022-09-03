from sqlalchemy import MetaData, Column, Integer, Float
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()
Base = declarative_base(metadata=metadata)

class Expense(Base):
    __tablename__ = 'expense'
    
    trans_id = Column(Integer, primary_key=True)
    income = Column(Float, nullable=False, default=0)
    
    def __init__(self):
        pass
    
    def __repr__(self):
        return 'Transaction %r' % self.trans_id
    
    def __str__(self):
        return 'Transaction %r' % self.trans_id
    
    def check(self):
        return "Success"