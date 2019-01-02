
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

    def __check_drawings(self, value):
        available_value = self.__limit + self.__limit
        return value <= available_value

    def drawings(self, value):
        if (self.__check_drawings(value)):
            self.__balance -= value
        else:
            print('Value {} has exceeded the limit'.format(value))

    def tranfer(self, value, destiny):
        self.deposit()
        destiny.drawings(value)
    
    @property
    def holder(self, holder):
        return self.__holder

    @property
    def balance(self):
        return self.__balance

    @limit.setter
    def limit(self, limit):
        self.__limit = limit

    @property
    def get_limit(self):
        return self.__limit











