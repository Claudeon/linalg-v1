from math import *

class Rat:
    def __init__(self, num, *den):
        if den:
            den = den[0]
            if den > 0:
                d = gcd(num, den)
            else:
                d = -gcd(num, den)
            self.num = num//d
            self.den = den//d
        else:
            self.num = num
            self.den = 1
            
    def __str__(self):
        return f'{self.num}/{self.den}'
        
    def __add__(self, other):
        if type(other) == int:
            return Rat(self.num + other*self.den, self.den)
        return Rat(self.num*other.den + self.den*other.num, self.den*other.den)
    
    def __sub__(self, other):
        if type(other) == int:
            return Rat(self.num - other*self.den, self.den)
        return Rat(self.num*other.den - self.den*other.num, self.den*other.den)
        
    def __mul__(self, other):
        if type(other) == int:
            return Rat(self.num*other, self.den)
        return Rat(self.num*other.num, self.den*other.den)
        
    def __div__(self, other):
        if type(other) == int:
            return Rat(self.num, self.den*other)
        return Rat(self.num*other.den, self.den*other.num)
