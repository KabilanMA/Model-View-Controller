import imp
import sys, os
from urllib import response

ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..','..','pattern_name','MVC'))
sys.path.insert(0, os.path.join(ROOT_DIR, 'client/controller'))
sys.path.append(os.path.join(ROOT_DIR, 'server/model'))
sys.path.append(os.path.join(ROOT_DIR, 'server'))

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from flask import current_app,Flask
from Balance import Balance
from DBModel import DBModel
from Expense import Expense
from flaskdb import db
from connector import Connector


from unittest.mock import MagicMock, patch,Mock
from requests.models import Response
# from client.controller.connector import Connector
import pytest
from controller import create_app
# from server.model.Expense import Expense
# from server.model.flaskdb import db


# import controller

from unittest.mock import patch

import unittest

class TestClass(unittest.TestCase):


    def setUp(self):
        print('Setting Up...')
        self.connector = Connector("http://127.0.0.1:5000")
        self.app = create_app()
        self.appctx = self.app.app_context()
        self.appctx.push()
        db.create_all()
        self.client = self.app.test_client()
        # self.balance = Balance(db)
        # self.tester = self.controller.test_client(self)



    def tearDown(self):
        print('Tearing Down...\n')
        self.connector = None
        self.appctx.pop()
        self.app = None
        self.appctx = None
        self.client = None
        pass

    def test_app(self):
        assert self.app is not None
        assert current_app == self.app


#==================
    def test_income12(self):
        response = self.client.post('/income',json={'amount':100}, follow_redirects=True)
        assert response.status_code == 200
#============

#==================
    def test_Expense12(self):
        response = self.client.post('/expense',json={'amount':0}, follow_redirects=True)
        assert response.status_code == 200
#============

    def test_balance123(self):
        balance = self.connector.getBalance()
        response = self.client.get('/balance', follow_redirects=True)
        # self.assertEqual(balance,response)


    def test_income(self):
        with patch('connector.requests.post') as mocked_post:
            print("=============================")
            print("running income URL test")
            a= "8237482394"
            print(int(a))
            balance = float(self.connector.getBalance())
            print(balance)
            amount = 100
            print(amount)
            total = float(balance)+ float(amount)  
            print(total)
            response = self.connector.saveExpense(amount, 'income')
            mocked_post.assert_called_with(url='http://127.0.0.1:5000/income',json={'amount':100})
            print("Income URL Test Success")
            print("=============================")

    """Check if the getBalance() function of the connector works and URL of the server also works"""
    def test_balance(self):
        print("=============================")
        print("running balance URL test")
        with patch('connector.requests.get') as mocked_get:
            balance1 = self.connector.getBalance()
            mocked_get.assert_called_with('http://127.0.0.1:5000/balance')
            print("Balance URL Test Success")
        print("=============================")

    """Check if the saveExpense() function of the connector works and URL of the server also works for expense"""
    def test_expense(self):
        print("=============================")
        with patch('connector.requests.post') as mocked_post:
            print("running expence URL test")
            amount = 100
            expense = 50
            response3 = self.connector.saveExpense(amount, 'income')
            response2 = self.connector.saveExpense(expense, 'expense')
            mocked_post.assert_called_with(url='http://127.0.0.1:5000/expense',json={'amount':50})
            print("Expense URL Test Success")
        print("=============================")

    """Check if the getBalance() function of the connector works properly for income. It depends on the saveExpense() function of the connector"""
    def test_income_two(self):
        print("=============================")
        print("running income test2")
        balance = float(self.connector.getBalance())
        print(balance)
        amount = 100
        print(amount)
        total = float(balance)+ float(amount)  
        print(total)
        response = self.connector.saveExpense(amount, 'income')
        response1 = float(self.connector.getBalance())
        print(response1)
        self.assertEqual(total,response1)
        print("Income Test Success")
        print("=============================") 

    """Check if the getBalance() function of the connector works properly. It depends on the saveExpense() function of the connector"""
    def test_balance_two(self):
        print("=============================")
        print("running balance test")
        balance = float(self.connector.getBalance())
        response3 = self.connector.saveExpense(100, 'income')
        balance2 = float(self.connector.getBalance()) - 100
        print(balance2, balance)
        self.assertEqual(balance,balance2)
        print("Balance Test Success")
        print("=============================")

    """Check if the saveExpense() function of the connector works properly for expense. it depends on getBalance() function of the connector"""
    def test_expense_two(self):
        print("=============================")
        
        print("running expence test")
        balance = float(self.connector.getBalance())
        amount = 100
        expense = 50
        total = balance+amount-expense
        response3 = self.connector.saveExpense(amount, 'income')
        response2 = self.connector.saveExpense(expense, 'expense')
        response1 = float(self.connector.getBalance())
        print(response1)
        self.assertEqual(total,response1)
        print("Expense Test Success")
        print("=============================")

    
    # def test_balance(self):
    #    name = self.balance.__str__()
    #    print(name)
    #    self.assertEqual(1,1)


    @pytest.fixture(scope="session")
    def flask_app():
            app = create_app()
            client = app.test_client()
            ctx = app.test_request_context()
            ctx.push()
            yield client
            ctx.pop()

    @pytest.fixture(scope="session")
    def app_with_db(flask_app):
            db.create_all()

            yield flask_app

            db.session.commit()
            db.drop_all()
    
    @pytest.fixture
    def app_with_data(app_with_db):
        Expense = Expense(db,3,4)
        db.session.add(Expense)
        db.session.commit()

        yield app_with_db
        
if __name__ == '__main__':
    unittest.main()


# def server():
#     server_root = os.path.realpath(os.path.join(os.path.dirname(__file__), '..','..'))
#     server_path = os.path.join(ROOT_DIR, 'server')
#     server_file = server_path + '/controller.py'
#     exec(open(server_file).read())
       
# if __name__ == '__main__':
#     thread = Thread(target=unittest.main())
#     thread.start()
#     # server()