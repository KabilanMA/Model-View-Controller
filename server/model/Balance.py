import sys
sys.path.append('/home/vinojith/Desktop/myproject/Model-View-Controller/server/model')

from DBModel import DBModel
from sqlalchemy import func

class Balance:
        
    def __str__(self):
        return ('Balance query')
        
    def getBalance(self, sqldb):
        total_balance = sqldb.session.query(DBModel).with_entities(func.sum(DBModel.income).label('balance')).first().balance
        return '%.2f'%total_balance    
        