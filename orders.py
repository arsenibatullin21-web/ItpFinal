from models import Order, OrderItem
from storage import load_orders, save_orders


class OrderProcessor:
    def __init__(self, inventory_manager, customer_manager):
        self.inventory = inventory_manager
        self.customers = customer_manager
        self.orders = load_orders()

    def _next_id(self):
        if not self.orders:
            return 1
        return max(order.order_id for order in self.orders) + 1

    def create_order(self, customer_id, cart):
        customer = self.customers.find_customer(customer_id)
        if customer is None:
            raise ValueError("Customer ID was not found.")
        if not cart:
            raise ValueError("Order must contain at least one item.")

        order_items = []
        for product_id, quantity in cart.items():
            product = self.inventory.find_product(product_id)
            if product is None:
                raise ValueError(f"Product ID {product_id} was not found.")
            if quantity <= 0:
                raise ValueError("Order quantity must be greater than zero.")
            if product.quantity < quantity:
                raise ValueError(f"Not enough stock for {product.name}. Available: {product.quantity}")
            order_items.append(OrderItem(product.product_id, product.name, quantity, product.price))

        for product_id, quantity in cart.items():
            self.inventory.reduce_stock(product_id, quantity)

        order = Order(self._next_id(), customer.customer_id, customer.name, order_items)
        self.orders.append(order)
        save_orders(self.orders)
        return order

    def list_orders(self):
        return self.orders
