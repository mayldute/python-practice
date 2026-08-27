"""
Task:
Implement a simple order management system using object-oriented programming.

Requirements:
- Create `Product`, `OrderItem`, and `Order` classes.
- A Product has a name and price.
- An OrderItem represents a product and its quantity.
- An Order contains multiple OrderItem objects.
- An order can be paid only once.
- An order cannot be paid if it is empty.
- The total price of an order depends on the products and quantities.

Rules:
- Product name cannot be empty.
- Product price must be greater than 0.
- OrderItem quantity must be greater than 0.
- An order starts as unpaid.
- An empty order has a total price of 0.
- An unpaid order can be paid.
- A paid order cannot be paid again.
- Adding an item with the same product to an order should combine
  the quantities instead of creating a separate item.

Methods:

Product:
    - name
    - price

OrderItem:
    - product
    - quantity

Order:
    - add_item(product, quantity)
    - total_price()
    - pay()
    - is_paid()

Algorithm:
- Adding an existing product requires finding the corresponding item.
- `total_price()` calculates the total cost of all items.
"""


class Product:
    def __init__(self, name: str, price: float) -> None:
        if not name:
            raise ValueError("Name can not be empty.")

        if price <= 0:
            raise ValueError("Price must be greater than 0.")

        self.name = name
        self.price = price

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Product):
            return NotImplemented

        return self.name == other.name and self.price == other.price


class OrderItem:
    def __init__(self, product: Product, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")

        self.product = product
        self.quantity = quantity


class Order:
    def __init__(self) -> None:
        self.order_items: list[OrderItem] = []
        self._paid = False

    def add_item(self, product: Product, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")

        for existing_item in self.order_items:
            if existing_item.product == product:
                existing_item.quantity += quantity
                return

        self.order_items.append(OrderItem(product, quantity))

    def total_price(self) -> float:
        return sum(item.product.price * item.quantity for item in self.order_items)

    def pay(self) -> None:
        if not self.order_items or self._paid:
            raise ValueError("Order is empty or already paid.")

        self._paid = True

    def is_paid(self) -> bool:
        return self._paid
