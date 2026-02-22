class Product:
    """
    Represents a product in the shop.
    """
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.__quantity = quantity

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value

    @property
    def quantity(self) -> int:
        return self.__quantity

    @quantity.setter
    def quantity(self, value: int):
        if value < 0:
            raise ValueError("Quantity cannot be negative")
        self.__quantity = value


class Category:
    """
    Represents a category of products.
    """
    total_categories = 0
    total_unique_products = 0

    def __init__(self, name: str, description: str, products: list = None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.total_categories += 1
        Category.total_unique_products += len(self.__products)

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError("Only Product instances can be added to Category")
        self.__products.append(product)
        Category.total_unique_products += 1

    @property
    def products(self) -> list:
        return self.__products
