from dataclasses import dataclass

@dataclass
class Product:
    name: str
    quantity: int
    price: float

    def totalPrice(self) -> float:
        return self.price * self.quantity

item = Product("milk", 2, 4.99)

print(item.totalPrice())