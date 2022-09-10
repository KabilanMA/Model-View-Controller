import imp
import sys
from urllib import response
# import os
# os.environ['DATABASE_URL'] = 'sqlite:///tests/expense_manager.db'  # use an in-memory database for tests


sys.path.insert(0, '/home/vinojith/Desktop/myproject/Model-View-Controller/client/controller')
sys.path.append('/home/vinojith/Desktop/myproject/Model-View-Controller/server/model')
sys.path.append('/home/vinojith/Desktop/myproject/Model-View-Controller/server')

from flask import current_app,Flask
# from Balance import Balance
# from DBModel import DBModel
# from Expense import Expense
# from flaskdb import db
from connector import Connector

# import controller

from unittest.mock import patch

import unittest


# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/expense_manager.db'
# db.init_app(app)


class TestClass(unittest.TestCase):


    def setUp(self):
        print('SetUP')
        self.connector = Connector("http://127.0.0.1:5000")
        # self.controller = controller()
        # self.balance = Balance(db)
        # self.tester = self.controller.test_client(self)



    def tearDown(self):
        print('\nTearDown......\n')
        self.connector = None
        pass

    # def test_app(self):
    #     print("Hi print test is running")
    #     response = self.tester.get('/balance')
    #     code = response.status_code
    #     self.assertEqual(code,200)


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
            # print(response1)
            print("Income URL Test Success")
            print("=============================")
            
            # self.assertEqual(response.status_code,200)
            # self.assertEqual(post_httpbin('http://127.0.0.1:5000/income').status_code, 200)

    def test_balance(self):
        print("=============================")
        print("running balance URL test")
        with patch('connector.requests.get') as mocked_get:
            balance1 = self.connector.getBalance()
            mocked_get.assert_called_with('http://127.0.0.1:5000/balance')
            # balance2 = self.connector.getBalance()
            # print(response)
            # self.assertEqual(balance1,balance2)
            print("Balance URL Test Success")
        print("=============================")

    def test_expense(self):
        print("=============================")
        with patch('connector.requests.post') as mocked_post:
            print("running expence URL test")
            amount = 100
            expense = 50
            response3 = self.connector.saveExpense(amount, 'income')
            response2 = self.connector.saveExpense(expense, 'expense')
            mocked_post.assert_called_with(url='http://127.0.0.1:5000/expense',json={'amount':50})
            # self.assertEqual(response2.status_code,200)
            print("Expense URL Test Success")
        print("=============================")


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


    def test_balance_two(self):
        print("=============================")
        print("running balance test")
        balance = float(self.connector.getBalance())
        response3 = self.connector.saveExpense(100, 'income')
        balance2 = float(self.connector.getBalance()) - 100
        self.assertEqual(balance,balance2)
        print("Balance Test Success")
        print("=============================")

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
        
if __name__ == '__main__':
    unittest.main()
