import math

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
            d = math.gcd(temp_num, temp_den)
            if d < 0:
                d = -d
            if d:
                self.num, self.den = temp_num//d, temp_den//d
            else:
                self.num, self.den = 0, 1
        else:
            raise TypeError("More than 2 arguments")

    def __str__(self):
        if self.den == 1:
            return str(self.num)
        return f'{self.num}/{self.den}'
    def __repr__(self):
        return str(self)

    def __add__(self, other):
        if isinstance(other, Rat):
            return Rat(self.num*other.den + self.den*other.num, self.den*other.den)
        elif isinstance(other, int):
            return Rat(self.num + self.den*other, self.den)
        else:
            raise TypeError("other of unknown type")
    def __mul__(self, other):
        if isinstance(other, Rat):
            return Rat(self.num*other.num, self.den*other.den)
        elif isinstance(other, int):
            return Rat(self.num*other, self.den)
        else:
            raise TypeError("other of unknown type")
    def __sub__(self, other):
        return self + (other * (-1))
    def __div__(self, other):
        if isinstance(other, Rat):
            return Rat(self.num*other.den, self.den*other.num)
        elif isinstance(other, int):
            return Rat(self.num, self.den*other)
        else:
            raise TypeError("other of unknown type")
            
#### GLOBAL VARIABLES ####
INPUT_TXT   = 2
SPACING     = 9
BREAK_CMD   = "break"

class Mat(object):
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.list = [[Rat(0)]*self.cols for row in range(self.rows)]
    
    def get(self, row, col):
        return self.list[row][col]
    def set(self, val, row, col):
        self.list[row][col] = val
    def remove(self, row, col):
        self.set(0, row, col)

    def __str__(self):
        pass
        
    def __repr__(self):
        txt = ""
        for row in range(self.rows):
            for col in range(self.cols):
                ele = str(self.get(row, col))
                if len(ele) >= SPACING:
                    txt += " " + ele
                else:
                    txt += " "*(SPACING - len(ele)) + ele
            txt += "\n"
        return txt
        
    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.rows:
            return
        temp = Mat(self.rows, self.cols)
        for r in range(self.rows):
            for c in range(self.cols):
                temp.set(self.get(r,c) + other.get(r,c), r, c)
        return temp
    def __mul__(self, other):
        if isinstance(other, Mat):
            if self.cols != other.rows:
                raise ValueError
            temp = Mat(self.rows, other.cols)
            for r in range(self.rows):
                for c in range(other.cols):
                    v = Rat(0)
                    for i in range(self.cols):
                        v += self.get(r,i)*self.get(i,c)
                    temp.set(v, r, c)
            return temp
        else:
            temp = Mat(self.rows, self.cols)
            for r in range(self.rows):
                for c in range(self.cols):
                    temp.set(self.get(r,c)*other, r, c)
            return temp
    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.rows:
            return
        temp = Mat(self.rows, self.cols)
        for r in range(self.rows):
            for c in range(self.cols):
                temp.set(self.get(r,c) - other.get(r,c), r, c)
        return temp



class Matrix(Mat):
    def __init__(self, rows, cols):
        super().__init__(rows, cols)
        for row in range(self.rows):
            repeat, is_break = True, False
            txt = str(row) + (INPUT_TXT - len(str(row)))*" "
            while repeat:
                row_input = input(f'row {txt}: ')
                if row_input == BREAK_CMD:
                    is_break = True
                    print("Breaking operation")
                    break
                row_input = tuple(row_input.split(" "))
                row_input = tuple(filter(lambda x: x != "", row_input))
                if len(row_input) != self.cols:
                    print("Please retry")
                    continue
                for col in range(self.cols):
                    self.set(Rat(row_input[col]), row, col)
                repeat = False
            if is_break:
                break


