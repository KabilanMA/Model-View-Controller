from .DBModel import DBModel

class Expense:
    
    def __init__(self, sqldb, amount, code):
        self.amount = amount*code
        self.sqldb = sqldb
        
    def __str__(self):
        return ('Expense transaction' if self.amount<0 else 'Income transaction')
    
    def save(self):
        model = DBModel(income=self.amount)
        self.sqldb.session.add(model)
        self.sqldb.session.commit()  
        