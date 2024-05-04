from datetime import date

# difind person class
class Person:
    def __init__(self, name: str, country: str, date_of_brith: str) -> str:
        self.name = name 
        self.country = country
        self.date_of_brith = date_of_brith

    # function calculate age 
    def calculate_age(self) -> int:
        '''
        for calculate age :
        1. finde this year 
        2. finde brith year
        3. this year - brith year
        return age 
        '''
        year = int(date.today().strftime('%Y'))
        self.date_of_brith = int(self.date_of_brith.split("/")[0])
        age = year - self.date_of_brith 
        return age        
    
    # reprisentation for person object
    def __repr__(self):
        OKGREEN = '\033[95m'
        ENDC = '\033[0m'
        text = ''
        text += f'name :{OKGREEN}{self.name}{ENDC}\n'
        text += f'country : {OKGREEN}{self.country}{ENDC}\n'
        text += f'brith_day : {OKGREEN}{self.date_of_brith}{ENDC}\n'
        text += f'age : {OKGREEN}{str(self.calculate_age())}{ENDC}\n'
        return text

if __name__ == "__main__":
    name = input('please enter name: ')
    country = input('please enter country: ')
    date_of_brith = input('please enter date of brith e.x:1997/09/21: ')
    person = Person(name, country, date_of_brith)
    print(person)
