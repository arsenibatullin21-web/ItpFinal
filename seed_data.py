from pathlib import Path

from storage import CUSTOMERS_JSON, ORDERS_JSON, PRODUCTS_JSON, USERS_JSON, save_customers, save_orders, save_products, save_users
from models import Customer, Order, OrderItem, Product, User


def seed_sample_data():
    data_files = [PRODUCTS_JSON, CUSTOMERS_JSON, ORDERS_JSON, USERS_JSON]
    if all(Path(path).exists() for path in data_files):
        return

    products = [
        Product(1, "Wireless Mouse", "Electronics", 19.99, 25),
        Product(2, "USB-C Charger", "Electronics", 24.50, 18),
        Product(3, "Notebook Set", "Stationery", 8.75, 40),
        Product(4, "Desk Lamp", "Home Office", 32.00, 12),
        Product(5, "Water Bottle", "Accessories", 14.25, 30),
    ]
    customers = [
        Customer(1, "Aigerim S.", "aigerim@example.com", "+7 700 111 2233"),
        Customer(2, "Daniel K.", "daniel@example.com", "+7 701 444 5566"),
    ]
    orders = [
        Order(
            1,
            1,
            "Aigerim S.",
            [OrderItem(3, "Notebook Set", 2, 8.75), OrderItem(5, "Water Bottle", 1, 14.25)],
            "Processed",
            "2026-05-13 09:00:00",
        )
    ]
    users = [
        User(1, "admin", "admin123", "admin", None),
        User(2, "aigerim", "user123", "user", 1),
    ]

    save_products(products)
    save_customers(customers)
    save_orders(orders)
    save_users(users)
