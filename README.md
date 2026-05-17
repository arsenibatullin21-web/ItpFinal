# Online Store Inventory & Order Processing System

## Project Description

This is a Python console application for managing a small online store. The system manages products, customers, inventory stock, user accounts, and order processing.

The project now includes registration and user roles:

- `admin` can manage products, customers, users, and all orders.
- `user` can view/search products, create orders, and view their own orders.

## How to Run

Open the project folder in PyCharm or a terminal and run:

```bash
python main.py
```

If `python` does not work on Windows, use the project virtual environment:

```bash
.venv\Scripts\python.exe main.py
```

## Default Accounts

The project creates sample accounts on the first run:

| Username | Password | Role |
|---|---|---|
| admin | admin123 | admin |
| aigerim | user123 | user |

You can also register a new simple user from the account menu.

## How to Run Tests

```bash
python tests.py
```

Expected result:

```text
All tests passed.
```

## Main Project Files

| File | Purpose |
|---|---|
| `main.py` | Main menu, login/register flow, admin menu, user menu, and user input |
| `auth.py` | Registration, login, and user role management |
| `models.py` | Data classes for User, Product, Customer, OrderItem, and Order |
| `inventory.py` | Product management and stock updates |
| `customers.py` | Customer creation, listing, and search |
| `orders.py` | Order validation, stock checking, order creation, and saving |
| `storage.py` | JSON loading/saving and CSV export |
| `seed_data.py` | Creates sample products, customers, orders, and users |
| `tests.py` | Simple automatic tests |
| `data/` | Stores JSON and CSV data files |

## Project Logic

The application starts in `main.py`.

First, `seed_sample_data()` runs. This creates sample data if the required data files do not already exist.

Then the program creates the main manager objects:

```text
AuthManager
InventoryManager
CustomerManager
OrderProcessor
```

The user first sees the account menu:

```text
1. Login
2. Register as simple user
0. Exit
```

After login, the program checks the user's role.

If the role is `admin`, the admin menu is shown. The admin can:

- view products
- add products
- update products
- delete products
- search products
- view customers
- add customers
- create orders
- view all orders
- register new accounts
- view users

If the role is `user`, the simple user menu is shown. The user can:

- view products
- search products
- create an order
- view only their own orders

## Order Processing Logic

Order processing is handled in `orders.py`.

When an order is created, the system:

1. Checks if the customer exists.
2. Checks if the cart is not empty.
3. Checks every product in the cart.
4. Checks that quantity is greater than zero.
5. Checks if enough stock is available.
6. Creates `OrderItem` objects.
7. Reduces product stock.
8. Creates an `Order` object.
9. Saves the order to JSON and CSV files.

This prevents the store from selling products that are not available.

## Data Storage Logic

Data is saved in the `data/` folder.

JSON files are used by the program:

- `products.json`
- `customers.json`
- `orders.json`
- `users.json`

CSV files are exported for easy viewing:

- `products.csv`
- `customers.csv`
- `orders.csv`

The `storage.py` file is responsible for loading and saving this data.

## Notes for Submission

For source code submission, include the Python files, `README.md`, `README.txt`, and the `data/` files.

Do not include:

- `.venv`
- `.idea`
- `__pycache__`
- generated report/presentation helper scripts
