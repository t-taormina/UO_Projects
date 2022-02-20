


class Food:
    """Could be composite or elementary (recursive or base, interior node or leaf node)"""

    def calories(self) -> int:
        raise NotImplementedError("There are no generic foods")

class ElementaryFood(Food):
    def __init__(self, cal_per_portion: int):
        self.cal = cal_per_portion

    def calories(self) -> int:
        return self.cal

class CompositeFood(Food):
    def __init__(self, parts: list):
        self.parts = parts

    def calories(self) -> int:
        total = 0
        for part in self.parts:
            total += part.calories()
        return total

spam = ElementaryFood(100)
rice = ElementaryFood(30)
sushi = CompositeFood([spam, rice])
print(sushi.calories())
