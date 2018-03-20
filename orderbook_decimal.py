import sortedcontainers
from decimal import *

class orderBook:
    def __init__(self, side):
        self.book = sortedcontainers.SortedDict()
        self.side = side

    def clear(self):
        if not self.is_empty():
            self.book.clear()

    def is_empty(self):
        return len(self.book) == 0

    def update(self, price, size):
        if Decimal(size) == 0:
            if Decimal(price) in self.book:
                del self.book[Decimal(price)]
        else:
            self.book.update({Decimal(price): Decimal(size)})

    def best(self):
        if self.side == 'ask':
            if len(self.book) == 0:
                return Decimal('9999999999.9')
            else:
                return self.book.iloc[0]
        else:
            if len(self.book) == 0:
                return Decimal('0')
            else:
                return self.book.iloc[-1]

    def best_size(self):
        if self.is_empty():
            return Decimal('0')
        else:
            if self.side == 'ask':
                return self.book[self.book.iloc[0]]
            else:
                return self.book[self.book.iloc[-1]]

    def size(self, price):
        if self.is_empty():
            return Decimal('0')
        else:
            cum_size = Decimal('0')
            if self.side == 'ask':
                for i in iter(self.book):
                    if i > Decimal(price):
                        return cum_size
                    cum_size += self.book[i]
            else:
                for i in reversed(self.book):
                    if i < Decimal(price):
                        return cum_size
                    cum_size += self.book[i]

    def price(self, size):
        cum_size = Decimal('0')
        if self.side == 'ask':
            if self.is_empty():
                return Decimal('9999999999.9')
            else:
                for i in iter(self.book):
                    cum_size += self.book[i]
                    if cum_size > Decimal(size):
                        return i
        else:
            if self.is_empty():
                return Decimal('0')
            else:
                for i in reversed(self.book):
                    cum_size += self.book[i]
                    if cum_size > Decimal(size):
                        return i
