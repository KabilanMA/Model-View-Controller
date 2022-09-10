# this is the server class responding to the request.

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from model.Expense import Expense
from model.Balance import Balance
from model.flaskdb import db

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/expense_manager.db'
# db.init_app(app)

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/expense_manager.db'
    db.init_app(app)


    #controller of MVC
    @app.route('/income', methods=['POST'])
    def income():
        if request.method == 'POST':
            amount = request.get_json()['amount']
            try:
                amount = float(amount)
                if amount<0:
                    raise ValueError('Amount must be positive')
            except Exception as e:
                return str(e), 400
            else:
                db.create_all()
                expense = Expense(db, amount, 1)
                expense.save()
            return str(expense)
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
                db.create_all()
                expense = Expense(db, amount, -1)
                expense.save()
                return str(expense)
        else:
            return "Not allowed method",405

    @app.route('/balance', methods=['POST', 'GET'])
    def balance():
        if request.method == 'POST' or 'GET':
            
            balance = Balance()
            
            return balance.getBalance(db)
        
    return app  
if __name__ == "__main__":
    # app.run(debug=True)
    # db.create_all()
    app = create_app()
    app.run(debug=True)
    db.create_all()
    