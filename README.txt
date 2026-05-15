Online Store Inventory & Order Processing System

Project description:
This Python console application manages products, customers, inventory stock, and order processing for a small online store. It checks stock before accepting an order, reduces inventory after a successful order, calculates totals, saves data, and handles common input errors.

How to run:
1. Install Python 3.
2. Open this folder in PyCharm or a terminal.
3. Run:
   python main.py

How to run tests:
   python tests.py

Main files:
main.py - menu interface and user input
models.py - Product, Customer, OrderItem, and Order classes
inventory.py - product and stock management
customers.py - customer management
orders.py - order processing
storage.py - JSON saving/loading and CSV exports
seed_data.py - sample data setup
tests.py - simple validation tests
data/ - product, customer, and order data files

Submission notes:
Do not include .venv, .idea, __pycache__, or other virtual environment folders in the submitted ZIP.
