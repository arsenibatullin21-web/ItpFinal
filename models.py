from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class User:
    user_id: int
    username: str
    password: str
    role: str
    customer_id: int | None = None

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "username": self.username,
            "password": self.password,
            "role": self.role,
            "customer_id": self.customer_id,
        }

    @classmethod
    def from_dict(cls, data):
        customer_id = data.get("customer_id")
        return cls(
            user_id=int(data["user_id"]),
            username=str(data["username"]),
            password=str(data["password"]),
            role=str(data["role"]),
            customer_id=int(customer_id) if customer_id is not None else None,
        )


@dataclass
class Product:
    product_id: int
    name: str
    category: str
    price: float
    quantity: int

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "quantity": self.quantity,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            product_id=int(data["product_id"]),
            name=str(data["name"]),
            category=str(data["category"]),
            price=float(data["price"]),
            quantity=int(data["quantity"]),
        )


@dataclass
class Customer:
    customer_id: int
    name: str
    email: str
    phone: str

    def to_dict(self):
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            customer_id=int(data["customer_id"]),
            name=str(data["name"]),
            email=str(data["email"]),
            phone=str(data["phone"]),
        )


@dataclass
class OrderItem:
    product_id: int
    product_name: str
    quantity: int
    unit_price: float

    @property
    def line_total(self):
        return self.quantity * self.unit_price

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "product_name": self.product_name,
            "quantity": self.quantity,
            "unit_price": self.unit_price,
            "line_total": self.line_total,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            product_id=int(data["product_id"]),
            product_name=str(data["product_name"]),
            quantity=int(data["quantity"]),
            unit_price=float(data["unit_price"]),
        )


@dataclass
class Order:
    order_id: int
    customer_id: int
    customer_name: str
    items: list[OrderItem]
    status: str = "Processed"
    created_at: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    @property
    def total(self):
        return sum(item.line_total for item in self.items)

    def to_dict(self):
        return {
            "order_id": self.order_id,
            "customer_id": self.customer_id,
            "customer_name": self.customer_name,
            "items": [item.to_dict() for item in self.items],
            "total": self.total,
            "status": self.status,
            "created_at": self.created_at,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            order_id=int(data["order_id"]),
            customer_id=int(data["customer_id"]),
            customer_name=str(data["customer_name"]),
            items=[OrderItem.from_dict(item) for item in data.get("items", [])],
            status=str(data.get("status", "Processed")),
            created_at=str(data.get("created_at", "")),
        )
