Online Store Inventory & Order Processing System

Project description:
This Python console application manages products, customers, inventory stock, users, and order processing for a small online store.

New user roles:
- admin: can manage products, customers, users, and all orders
- user: can view/search products, create orders, and view own orders

Default accounts:
Admin:
  username: admin
  password: admin123

Simple user:
  username: aigerim
  password: user123

How to run:
1. Install Python 3.
2. Open this folder in PyCharm or a terminal.
3. Run:
   python main.py

If python does not work on Windows, run:
   .venv\Scripts\python.exe main.py

How to run tests:
   python tests.py

Main files:
main.py - login/register flow, admin menu, user menu, and user input
auth.py - registration, login, and user roles
models.py - User, Product, Customer, OrderItem, and Order classes
inventory.py - product and stock management
customers.py - customer management
orders.py - order processing
storage.py - JSON saving/loading and CSV exports
seed_data.py - sample data setup
tests.py - simple validation tests
data/ - stores JSON and CSV files

Project logic:
1. main.py starts the program and shows the account menu.
2. The user logs in or registers a simple user account.
3. The program checks the role.
4. Admin users see the admin menu.
5. Simple users see the user menu.
6. orders.py checks customer, products, quantity, and stock before creating an order.
7. inventory.py reduces stock after a successful order.
8. storage.py saves updated data to JSON and exports CSV files.

Submission notes:
Do not include .venv, .idea, __pycache__, or other virtual environment folders in the submitted ZIP.
