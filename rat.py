from math import *

class Rat(object):
    def __init__(self, arg, *args):
        if len(args) == 0:
            if type(arg) == str and len(args) == 0:
                tup = tuple(arg.split('/'))
                if len(tup) == 2:
                    temp = Rat(int(tup[0]), int(tup[1]))
                    self.num, self.den = temp.num, temp.den
                elif len(tup) == 1:
                    self.num, self.den = int(tup[0]), 1
            elif type(arg) == int and len(args) == 0:
                self.num, self.den = arg, 1
        elif len(args) == 1:
            temp_num, temp_den = int(arg), int(args[0])
            d = gcd(temp_num, temp_den)
            if d:
                self.num, self.den = temp_num//d, temp_den//d
                if self.den < 0:
                    self.num, self.den = -temp_num//d, -temp_den//d
            else:
                self.num, self.den = 0, 1
        else:
            raise TypeError("More than 2 arguments")

    def __str__(self):
        if self.den == 1 or self.num == 0:
            return str(self.num)
        return f'{self.num}/{self.den}'
    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if isinstance(other, Rat):
            if self.num == 0 and other.num == 0:
                return True
            return (self.num == other.num) and (self.den == other.den)
        elif isinstance(other, int):
            return self == Rat(other)
        elif isinstance(other, float):
            return self.num/self.den == other
        else:
            raise TypeError("other of unknown type")

    def __add__(self, other):
        if isinstance(other, Rat):
            return Rat(self.num*other.den + self.den*other.num, self.den*other.den)
        elif isinstance(other, int):
            return Rat(self.num + self.den*other, self.den)
        elif isinstance(other, float):
            return self.num/self.den + other
        else:
            raise TypeError("other of unknown type")
    def __mul__(self, other):
        if isinstance(other, Rat):
            return Rat(self.num*other.num, self.den*other.den)
        elif isinstance(other, int):
            return Rat(self.num*other, self.den)
        elif isinstance(other, float):
            return self.num/self.den * other
        else:
            raise TypeError("other of unknown type")
    def __sub__(self, other):
        return self + (other * (-1))
    def __truediv__(self, other):
        if isinstance(other, Rat):
            return Rat(self.num*other.den, self.den*other.num)
        elif isinstance(other, int):
            return Rat(self.num, self.den*other)
        elif isinstance(other, float):
            return (self.num/self.den) / other
        else:
            raise TypeError("other of unknown type")
