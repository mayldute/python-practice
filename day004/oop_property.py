"""
Task: Product Encapsulation

Create a Product class that uses properties to control access
to its internal state.

Requirements:
- The Product has a name, price, and quantity.
- Price cannot be negative.
- Quantity cannot be negative.
- Validate price and quantity both when the object is created
  and when their values are changed later.
- Store price and quantity as internal attributes.
- Use properties to access and modify price and quantity.
- Add a read-only total property that calculates:
  price * quantity.
"""


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")

        self._price = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError("Quantity cannot be negative.")

        self._quantity = value

    @property
    def total(self):
        return self.price * self.quantity
    