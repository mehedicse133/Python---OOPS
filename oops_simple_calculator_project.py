# Simple Calculator


class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        try:
            return round(self.num1 / self.num2, 3)
        except ZeroDivisionError as e:
            return print(e)


if __name__ == "__main__":

    calc = Calculator(5, 0)
    print(calc.add())
    print(calc.sub())
    print(calc.mul())
    print(calc.div())
