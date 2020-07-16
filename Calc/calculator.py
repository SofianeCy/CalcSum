class Calculator:
    def __init__(self, *num):
        self._num = list(num)

    @property
    def total(self):
        grand_total = sum(self._num)
        return grand_total


c = Calculator(5, 10, 20)
print(c.total)