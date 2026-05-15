from models import Customer
from storage import load_customers, save_customers


class CustomerManager:
    def __init__(self):
        self.customers = load_customers()

    def _next_id(self):
        if not self.customers:
            return 1
        return max(customer.customer_id for customer in self.customers) + 1

    def add_customer(self, name, email, phone):
        if "@" not in email:
            raise ValueError("Email must contain @.")

        customer = Customer(self._next_id(), name, email, phone)
        self.customers.append(customer)
        save_customers(self.customers)
        return customer

    def list_customers(self):
        return self.customers

    def find_customer(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        return None
