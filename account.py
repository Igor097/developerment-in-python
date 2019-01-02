
class Account:

    def __init__(self, number, holder, balance, limit):
        print('Create object...'.format(self))
        self.__number = number
        self.__holder = holder
        self.__balance = balance
        self.__limit = limit
    
    def extract(self):
        print('The Balance {} of holder is {}'.format(self.__balance, self.__holder))

    def deposit(self, value):
        self.__balance += value

    def drawings(self, value):
        if (self.__balance > self.__limit):
            print('Error')
        else:
            self.__balance -= value

    def tranfer(self, value, destiny):
        self.deposit()
        destiny.drawings(value)















