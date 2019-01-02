
class Account:

    def __init__(self, number, holder, balance, limit):
        #print('Create object...{}'.format(self))
        print('Create object...')
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

    def set_balance(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_limit(self, limit):
        self.__limit = limit

    def get_limit(self):
        return self.__limit











