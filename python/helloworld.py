#!env python3

import sys


class Hello:
    def __init__(self):
        self.names = 'Myoung sig '

    def sayhello(self):
        print(self.names + ' Hello World!')

    def __del__(self):
        print(self.names + ' I Will back')
        
if __name__ == '__main__':
        myHello = Hello()
        myHello.sayhello()
        
        sys.exit()
