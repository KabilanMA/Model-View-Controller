# this is the server class responding to the request.

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
# from model.Expense import Expense
# from model.flaskdb import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/expense_manager.db'
# db.init_app(app)
db = SQLAlchemy(app)

    
class Expense(db.Model):
    trans_id = db.Column(db.Integer, primary_key=True)
    income = db.Column(db.Float, nullable=True, default=0)
    
    def __repr__(self):
        return 'Transaction %r' % self.trans_id
    
    def __str__(self):
        return 'Transaction %r' % self.trans_id


@app.route('/income', methods=['POST'])
def income():
    if request.method == 'POST':
        amount = request.get_json()['amount']
        try:
            amount = float(amount)
            if amount<0:
                raise ValueError('amount must be positive')
        except Exception as e:
            return str(e), 400
        else:
            trans = Expense(income=amount)
            db.session.add(trans)
            db.session.commit()
        return str(trans)
    else:
        return "Not allowed method",405
    
@app.route('/expense', methods=['POST'])
def expense():
    if request.method == 'POST':
        amount = request.get_json()['amount']
        try:
            amount = float(amount)
            if amount<0:
                raise ValueError('amount must be positive')
        except Exception as e:
            return str(e), 400
        else:
            amount = amount*(-1)
            trans = Expense(income=amount)
            db.session.add(trans)
            db.session.commit()
            return str(trans)
    else:
        return "Not allowed method",405

@app.route('/balance', methods=['POST', 'GET'])
def balance():
    if request.method == 'POST' or 'GET':
        
        total_balance = Expense.query.with_entities(func.sum(Expense.income).label('balance')).first().balance
        
        return '%.2f'%total_balance
    
    
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
    