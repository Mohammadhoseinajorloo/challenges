class Calculator:

    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def add(self):
        return self.x + self.y 

    def subtrace(self):
        return self.x - self.y

    def multply(self):
        return self.x * self.y

    def divid(self):
        return self.x / self.y

if __name__ == "__main__":
    while True:
        x = int(input('please enter first number: '))
        y = int(input('please enter secound number: '))
        operator = (input('please enter operator e.x:+, -, *, /: '))

        calculator = Calculator(x, y)

        if operator == '+':
            print(calculator.add())
        elif operator == "-":
            print(calculator.subtrace())
        elif operator == "*":
            print(calculator.multply())
        elif operator == "/":
            print(calculator.divid())
        else: 
            print('oprator not invalid!!!')

        countinu = input('countiniu? : y-n: ')
        if countinu == "n":
            break
