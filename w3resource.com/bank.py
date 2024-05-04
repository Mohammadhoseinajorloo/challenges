# 11. Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.
import random 

class Account:
    def __init__(self, owner):
        self.owner = owner
        self.u_number = random.randint(1, 10)
        self.balanc = 0

    def __repr__(self):
        _str = ""
        _str += f'{self.owner} {self.u_number} {self.balanc}'
        return _str

class Bank:
    def __init__(self):
        self.customer =[] 

    def create_account(self, account):
        if account in self.customer:
            print("exist owner in bank")
        else:
            self.customer.append(account)

    def make_deposit(self, account, amount):
        if account in self.customer:
            account.balanc += amount
        else:
            print('please create account ofter try agein')
    
    def make_withdrowal(self, account, amount):
        if account in self.customer:
            if account.balanc > amount:
                account.balanc -= amount
            else:
                print('cant withdrowal this amount')
        else:
            print('please creae_accound after try agein')

    def __repr__(self):
        _str = ""
        for item in self.customer:
            _str += f'{item.owner}\t{item.u_number}\t{item.balanc}\n'
        return _str

if __name__ == '__main__':
    bank = Bank()
    print('Welcome to my bank...')
    while True:
        chooise = input('please chooise:\n1. create_account\n2. make_deposit\n3. make_withdrowal\n4.exit\nenter number:')
        if chooise == "1":
            owner = input('please enter owner: ')
            account = Account(owner)
            bank.create_account(account)

        if chooise == "2":
            owner = input('owner: ')
            amount = int(input ('amount: '))
            for account in bank.customer:
                if account.owner == owner:
                    bank.make_deposit(account, amount)

        if chooise == "3":
            owner = input('owner: ')
            amount = int(input ('amount: '))
            for account in bank.customer:
                if account.owner == owner:
                    bank.make_withdrowal(account, amount)
                    print(bank)
        if chooise == "4":
            break
