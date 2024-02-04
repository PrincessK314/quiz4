from dataclasses import dataclass

@dataclass
class Product:
    name: str
    quantity: int
    price: float

item = Product("milk", 2, 4.99)

print(item.price)