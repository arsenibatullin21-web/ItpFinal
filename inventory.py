from models import Product
from storage import load_products, save_products


class InventoryManager:
    def __init__(self):
        self.products = load_products()

    def _next_id(self):
        if not self.products:
            return 1
        return max(product.product_id for product in self.products) + 1

    def add_product(self, name, category, price, quantity):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        product = Product(self._next_id(), name, category, price, quantity)
        self.products.append(product)
        save_products(self.products)
        return product

    def list_products(self):
        return self.products

    def find_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None

    def search_products(self, keyword):
        keyword = keyword.lower()
        return [
            product
            for product in self.products
            if keyword in product.name.lower() or keyword in product.category.lower()
        ]

    def update_product(self, product_id, name=None, category=None, price=None, quantity=None):
        product = self.find_product(product_id)
        if product is None:
            raise ValueError("Product ID was not found.")

        if name:
            product.name = name
        if category:
            product.category = category
        if price is not None:
            if price < 0:
                raise ValueError("Price cannot be negative.")
            product.price = price
        if quantity is not None:
            if quantity < 0:
                raise ValueError("Quantity cannot be negative.")
            product.quantity = quantity

        save_products(self.products)
        return product

    def delete_product(self, product_id):
        product = self.find_product(product_id)
        if product is None:
            raise ValueError("Product ID was not found.")

        self.products.remove(product)
        save_products(self.products)
        return product

    def reduce_stock(self, product_id, quantity):
        product = self.find_product(product_id)
        if product is None:
            raise ValueError("Product ID was not found.")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if product.quantity < quantity:
            raise ValueError(f"Insufficient stock. Available: {product.quantity}")

        product.quantity -= quantity
        save_products(self.products)
        return product
