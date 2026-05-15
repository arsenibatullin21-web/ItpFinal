from customers import CustomerManager
from inventory import InventoryManager
from orders import OrderProcessor
from seed_data import seed_sample_data


def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid whole number.")


def read_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def show_products(products):
    if not products:
        print("No products found.")
        return

    print("\nID | Product Name              | Category       | Price  | Stock")
    print("-" * 65)
    for product in products:
        print(f"{product.product_id:<2} | {product.name:<25} | {product.category:<14} | ${product.price:<6.2f} | {product.quantity}")


def show_customers(customers):
    if not customers:
        print("No customers found.")
        return

    print("\nID | Customer Name        | Email                    | Phone")
    print("-" * 70)
    for customer in customers:
        print(f"{customer.customer_id:<2} | {customer.name:<20} | {customer.email:<24} | {customer.phone}")


def show_orders(orders):
    if not orders:
        print("No orders found.")
        return

    for order in orders:
        print(f"\nOrder #{order.order_id} | Customer: {order.customer_name} | Total: ${order.total:.2f} | {order.status}")
        for item in order.items:
            print(f"  - {item.product_name}: {item.quantity} x ${item.unit_price:.2f} = ${item.line_total:.2f}")


def add_product_menu(inventory):
    name = input("Product name: ").strip()
    category = input("Category: ").strip()
    price = read_float("Price: ")
    quantity = read_int("Quantity: ")
    product = inventory.add_product(name, category, price, quantity)
    print(f"Added product #{product.product_id}: {product.name}")


def update_product_menu(inventory):
    product_id = read_int("Product ID to update: ")
    product = inventory.find_product(product_id)
    if product is None:
        print("Product not found.")
        return

    print("Press Enter to keep the current value.")
    name = input(f"Name [{product.name}]: ").strip() or None
    category = input(f"Category [{product.category}]: ").strip() or None
    price_text = input(f"Price [{product.price}]: ").strip()
    quantity_text = input(f"Quantity [{product.quantity}]: ").strip()
    price = float(price_text) if price_text else None
    quantity = int(quantity_text) if quantity_text else None

    inventory.update_product(product_id, name, category, price, quantity)
    print("Product updated.")


def delete_product_menu(inventory):
    product_id = read_int("Product ID to delete: ")
    product = inventory.delete_product(product_id)
    print(f"Deleted product: {product.name}")


def add_customer_menu(customers):
    name = input("Customer name: ").strip()
    email = input("Email: ").strip()
    phone = input("Phone: ").strip()
    customer = customers.add_customer(name, email, phone)
    print(f"Added customer #{customer.customer_id}: {customer.name}")


def create_order_menu(orders):
    customer_id = read_int("Customer ID: ")
    cart = {}

    print("Add products to the order. Enter 0 as product ID to finish.")
    while True:
        product_id = read_int("Product ID: ")
        if product_id == 0:
            break
        quantity = read_int("Quantity: ")
        cart[product_id] = cart.get(product_id, 0) + quantity

    order = orders.create_order(customer_id, cart)
    print(f"Order #{order.order_id} processed successfully. Total: ${order.total:.2f}")


def main():
    seed_sample_data()
    inventory = InventoryManager()
    customers = CustomerManager()
    orders = OrderProcessor(inventory, customers)

    while True:
        print("\nONLINE STORE INVENTORY & ORDER PROCESSING SYSTEM")
        print("1. View products")
        print("2. Add product")
        print("3. Update product")
        print("4. Delete product")
        print("5. Search products")
        print("6. View customers")
        print("7. Add customer")
        print("8. Create order")
        print("9. View orders")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                show_products(inventory.list_products())
            elif choice == "2":
                add_product_menu(inventory)
            elif choice == "3":
                update_product_menu(inventory)
            elif choice == "4":
                delete_product_menu(inventory)
            elif choice == "5":
                keyword = input("Search keyword: ").strip()
                show_products(inventory.search_products(keyword))
            elif choice == "6":
                show_customers(customers.list_customers())
            elif choice == "7":
                add_customer_menu(customers)
            elif choice == "8":
                create_order_menu(orders)
            elif choice == "9":
                show_orders(orders.list_orders())
            elif choice == "0":
                print("Goodbye!")
                break
            else:
                print("Invalid menu choice. Please try again.")
        except ValueError as error:
            print(f"Error: {error}")



main()
