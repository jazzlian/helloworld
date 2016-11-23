#!env python3

import sys

class Hello():
    def __init__(self):
        self.names = 'Myoungsig '
    def sayHello(self):
        print(self.names + ' Hello World!')
if __name__ == '__main__':
        myHello = Hello()
        myHello.sayHello()
