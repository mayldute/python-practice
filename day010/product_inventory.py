"""
Task:
Implement a simple product inventory using object-oriented programming.

Requirements:
- Create a `Product` class.
- Create an `Inventory` class.
- A Product has a name, price, and quantity.
- Price must be greater than 0.
- Quantity must be 0 or greater.
- Invalid values must raise `ValueError`.
- Inventory stores multiple Product objects.
- `add_product()` adds a product to the inventory.
- If a product with the same name already exists, increase its quantity.
- `find_product()` returns a product by name or `None`.
- `total_value()` returns the total value of all inventory.
- `most_expensive_product()` returns the product with the highest price.
- If the inventory is empty, return `None`.
- If multiple products have the same price, return the first one.

Algorithm:
- Search for existing products by name.
- Calculate inventory value by summing `price * quantity`.
- Find the most expensive product by comparing product prices.
"""


class Product:
    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.name = name

        if price <= 0:
            raise ValueError("Price must be greater than 0.")

        self.price = price

        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.quantity = quantity


class Inventory:
    def __init__(self) -> None:
        self.products: list[Product] = []

    def add_product(self, product: Product) -> None:
        for existing_product in self.products:
            if existing_product.name == product.name:
                existing_product.quantity += product.quantity
                return

        self.products.append(product)

    def find_product(self, product_name: str) -> Product | None:
        for product in self.products:
            if product.name == product_name:
                return product

        return None

    def total_value(self) -> float:
        total_value = 0

        for product in self.products:
            total_value += product.price * product.quantity

        return total_value

    def most_expensive_product(self) -> Product | None:
        if not self.products:
            return None

        return max(self.products, key=lambda product: product.price)
