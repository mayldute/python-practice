"""
Task:
Create a ShoppingCart class that manages products and their quantities.

Requirements:
- Create a Product class with name and price.
- Create a ShoppingCart class.
- Allow adding a product with a quantity.
- Allow removing a product by name.
- Do not allow adding a quantity <= 0.
- Do not allow a product price < 0.
- Calculate the total cart price.
- If the same product is added multiple times, increase its quantity.
- Removing a product should remove all of its quantity.
- Return 0 for an empty cart.
- Use type hints.
"""


class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name

        if price < 0:
            raise ValueError("Price can not be less 0.")
        
        self.price = price


class ShoppingCart:
    def __init__(self) -> None:
        self.cart: dict[Product, int] = {}

    def add(self, product: Product, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("Quantity can not be equal or less 0.")
        
        self.cart[product] = self.cart.get(product, 0) + quantity

    def total(self) -> float:
        total = 0

        for product, quantity in self.cart.items():
            total += product.price * quantity

        return total

    def remove(self, product_name: str) -> None:
        for product in self.cart:
            if product.name == product_name:
                del self.cart[product]
                return
