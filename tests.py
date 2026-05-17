from auth import AuthManager
from customers import CustomerManager
from inventory import InventoryManager
from orders import OrderProcessor
from seed_data import seed_sample_data


def run_tests():
    seed_sample_data()
    inventory = InventoryManager()
    customers = CustomerManager()
    orders = OrderProcessor(inventory, customers)
    auth = AuthManager()

    assert len(inventory.list_products()) >= 5
    assert inventory.search_products("electronics")
    assert customers.find_customer(1) is not None
    assert auth.login("admin", "admin123").role == "admin"
    assert auth.login("aigerim", "user123").role == "user"

    try:
        orders.create_order(1, {1: 9999})
    except ValueError as error:
        assert "Not enough stock" in str(error)
    else:
        raise AssertionError("Insufficient-stock order should fail.")

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
