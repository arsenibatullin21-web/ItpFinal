import csv
import json
from pathlib import Path

from models import Customer, Order, Product, User


DATA_DIR = Path(__file__).parent / "data"
PRODUCTS_JSON = DATA_DIR / "products.json"
CUSTOMERS_JSON = DATA_DIR / "customers.json"
ORDERS_JSON = DATA_DIR / "orders.json"
USERS_JSON = DATA_DIR / "users.json"


def ensure_data_folder():
    DATA_DIR.mkdir(exist_ok=True)


def load_json(path, default):
    ensure_data_folder()
    if not path.exists():
        return default

    try:
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return default


def save_json(path, records):
    ensure_data_folder()
    with path.open("w", encoding="utf-8") as file:
        json.dump(records, file, indent=2)





def load_products():
    return [Product.from_dict(item) for item in load_json(PRODUCTS_JSON, [])]


def save_products(products):
    save_json(PRODUCTS_JSON, [product.to_dict() for product in products])
    export_products_csv(products)


def load_customers():
    return [Customer.from_dict(item) for item in load_json(CUSTOMERS_JSON, [])]


def save_customers(customers):
    save_json(CUSTOMERS_JSON, [customer.to_dict() for customer in customers])
    export_customers_csv(customers)


def load_orders():
    return [Order.from_dict(item) for item in load_json(ORDERS_JSON, [])]


def save_orders(orders):
    save_json(ORDERS_JSON, [order.to_dict() for order in orders])
    export_orders_csv(orders)


def load_users():
    return [User.from_dict(item) for item in load_json(USERS_JSON, [])]


def save_users(users):
    save_json(USERS_JSON, [user.to_dict() for user in users])




def export_products_csv(products):
    ensure_data_folder()
    with (DATA_DIR / "products.csv").open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["product_id", "name", "category", "price", "quantity"])
        for product in products:
            writer.writerow([product.product_id, product.name, product.category, product.price, product.quantity])


def export_customers_csv(customers):
    ensure_data_folder()
    with (DATA_DIR / "customers.csv").open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["customer_id", "name", "email", "phone"])
        for customer in customers:
            writer.writerow([customer.customer_id, customer.name, customer.email, customer.phone])


def export_orders_csv(orders):
    ensure_data_folder()
    with (DATA_DIR / "orders.csv").open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["order_id", "customer_id", "customer_name", "total", "status", "created_at"])
        for order in orders:
            writer.writerow([order.order_id, order.customer_id, order.customer_name, order.total, order.status, order.created_at])
