
import sys, os
from urllib import response

ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..','..','pattern_name','MVC'))
sys.path.insert(0, os.path.join(ROOT_DIR, 'client/controller'))
sys.path.append(os.path.join(ROOT_DIR, 'server/model'))
sys.path.append(os.path.join(ROOT_DIR, 'server'))

from flask import current_app,Flask

from connector import Connector

from unittest.mock import patch

import unittest

class TestClass(unittest.TestCase):


    def setUp(self):
        print('Setting Up...')
        self.connector = Connector("http://127.0.0.1:5000")
        self.connector.dropAllData()

    def tearDown(self):
        print('Tearing Down...\n')
        self.connector.dropAllData()
        self.connector = None
        pass
    
    """Check if the saveExpense() function of the connector works and URL of the server also works for income"""
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