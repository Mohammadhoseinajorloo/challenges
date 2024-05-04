# 8. Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.
import pandas as pd

class ShappingCart:
    def __init__(self):
        self.cart = []
        self.total = 0

    def add(self, name, count, price):
        item = (name, count, price)
        return self.cart.append(item)

    def remove(self, name):
        for item in self.cart:
            if item[0] == name:
                self.cart.remove(item)

    def counter(self):
        count = 0
        for item in self.cart:
            count += item[1]
        return count

    def calculate_total_price(self):
        price = 0
        for item in self.cart:
            price += item[2]
        return price

    def __repr__(self):
        linef = f'\033[38;2;{155};{0};{0}m'
        first = f'\033[38;2;{0};{155};{0}m'
        end = f'\033[0m'
        _str = ''
        name = []
        count = []
        price = []
        total = []
        dic = {'name': [], 'count': [], 'price': [], 'total': []}
        for item in self.cart:
            name.append(item[0])
            count.append(item[1])
            price.append(item[2])
            total.append(item[1]*item[2])
        dic['name']+=name
        dic['count']+=count
        dic['price']+=price
        dic['total']+=total
        _str += f'{first}{pd.DataFrame(dic)}{end}\n'
        _str += f'{linef}--------------------------------{end}\n'
        _str += f'{first}total:{end}\t\t{first}{sum(count)}{end}\t {first}{sum(total)}{end}'
        return _str

if __name__ == "__main__": 
    shappingcart = ShappingCart()
    print('welcome\n')
    while True:
        chooise = input('1.add\n2.remove\n3.esc')
        if chooise == '1': 
            name = input('please enter name: ')
            count = int(input('please enter count: '))
            price = int(input('please enter price: '))
            shappingcart.add(name, count, price)
            print(shappingcart)
        elif chooise == '2': 
            name = input('please enter name for remove: ')
            shappingcart.remove(name)
            print(shappingcart)
        elif chooise == '3': 
            break

