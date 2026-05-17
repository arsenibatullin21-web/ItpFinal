from auth import AuthManager
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


def show_users(users):
    if not users:
        print("No users found.")
        return

    print("\nID | Username             | Role  | Customer ID")
    print("-" * 52)
    for user in users:
        customer_id = user.customer_id if user.customer_id is not None else "-"
        print(f"{user.user_id:<2} | {user.username:<20} | {user.role:<5} | {customer_id}")


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


def create_order_menu(orders, customer_id=None):
    if customer_id is None:
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


def register_menu(auth, customers, allow_role_choice=False):
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    role = "user"
    if allow_role_choice:
        role = input("Role (admin/user): ").strip().lower() or "user"

    customer_id = None
    if role == "user":
        print("Create customer profile for this user.")
        name = input("Customer name: ").strip()
        email = input("Email: ").strip()
        phone = input("Phone: ").strip()
        customer = customers.add_customer(name, email, phone)
        customer_id = customer.customer_id

    user = auth.register_user(username, password, role, customer_id)
    print(f"Registered {user.role} account: {user.username}")
    return user


def login_menu(auth):
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    return auth.login(username, password)


def authenticate(auth, customers):
    while True:
        print("\nACCOUNT MENU")
        print("1. Login")
        print("2. Register as simple user")
        print("0. Exit")

        choice = input("Choose an option: ").strip()
        try:
            if choice == "1":
                user = login_menu(auth)
                print(f"Welcome, {user.username}! Role: {user.role}")
                return user
            elif choice == "2":
                user = register_menu(auth, customers)
                print("You can now use the system.")
                return user
            elif choice == "0":
                return None
            else:
                print("Invalid menu choice. Please try again.")
        except ValueError as error:
            print(f"Error: {error}")


def admin_menu(auth, inventory, customers, orders):
    while True:
        print("\nADMIN MENU")
        print("1. View products")
        print("2. Add product")
        print("3. Update product")
        print("4. Delete product")
        print("5. Search products")
        print("6. View customers")
        print("7. Add customer")
        print("8. Create order")
        print("9. View orders")
        print("10. Register new account")
        print("11. View users")
        print("0. Logout")

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
            elif choice == "10":
                register_menu(auth, customers, allow_role_choice=True)
            elif choice == "11":
                show_users(auth.users)
            elif choice == "0":
                print("Logged out.")
                break
            else:
                print("Invalid menu choice. Please try again.")
        except ValueError as error:
            print(f"Error: {error}")


def user_menu(current_user, inventory, orders):
    while True:
        print("\nUSER MENU")
        print("1. View products")
        print("2. Search products")
        print("3. Create order")
        print("4. View my orders")
        print("0. Logout")

        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                show_products(inventory.list_products())
            elif choice == "2":
                keyword = input("Search keyword: ").strip()
                show_products(inventory.search_products(keyword))
            elif choice == "3":
                create_order_menu(orders, current_user.customer_id)
            elif choice == "4":
                my_orders = [order for order in orders.list_orders() if order.customer_id == current_user.customer_id]
                show_orders(my_orders)
            elif choice == "0":
                print("Logged out.")
                break
            else:
                print("Invalid menu choice. Please try again.")
        except ValueError as error:
            print(f"Error: {error}")


def main():
    seed_sample_data()
    auth = AuthManager()
    inventory = InventoryManager()
    customers = CustomerManager()
    orders = OrderProcessor(inventory, customers)

    while True:
        current_user = authenticate(auth, customers)
        if current_user is None:
            print("Goodbye!")
            break
        if current_user.role == "admin":
            admin_menu(auth, inventory, customers, orders)
        else:
            user_menu(current_user, inventory, orders)


if __name__ == "__main__":
    main()
