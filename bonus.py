from collections.abc import Sized, Iterable

def countCharacters(a:Iterable[Sized])->list[int]:
    result = []
    for item in a:
        result.append(len(str(item)))
    return result

a = ["apple", "milk", "cheese"]
b = [12, 432, 6]
print(countCharacters(b))