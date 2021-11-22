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
            
#### GLOBAL VARIABLES ####
INPUT_TXT   = 2
SPACING     = 9
BREAK_CMD   = "break"
ZERO, ONE   = Rat(0), Rat(1)
DEBUGMODE   = False

class RealMatrix(object):
    pass

class RatMatrix(RealMatrix):
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.list = [[ZERO]*self.cols for row in range(self.rows)]
    
    def get(self, row, col):
        return self.list[row][col]
    def __getitem__(self, row):
        return self.list[row]
    def set(self, val, row, col):
        self.list[row][col] = val
    def remove(self, row, col):
        self.set(0, row, col)

    def __str__(self):
        return repr(self)
    def __repr__(self):
        txt = ""
        for row in range(self.rows):
            for col in range(self.cols):
                ele = str(self[row][col])
                if len(ele) >= SPACING:
                    txt += " " + ele
                else:
                    txt += " "*(SPACING - len(ele)) + ele
            txt += "\n"
        return txt

    def copy(self):
        temp = zeros(self.rows, self.cols)
        for row in range(self.rows):
            for col in range(self.cols):
                temp[row][col] = self[row][col]
        return temp
    # transpose matrix
    def T(self):
        temp = zeros(self.cols, self.rows)
        for row in range(self.rows):
            for col in range(self.cols):
                temp[col][row] = self[row][col]
        return temp

    def combine(self, other, vert = False):
        row1, col1 = self.rows, self.cols
        row2, col2 = other.rows, other.cols
        if vert == False:
            if row1 != row2:
                raise ValueError("Matrix sizes do not match")
            temp = zeros(row1, col1 + col2)
            rowsize, colsize = temp.rows, temp.cols
            for r in range(rowsize):
                for c in range(colsize):
                    if c < col1:
                        temp[r][c] = self[r][c]
                    else:
                        temp[r][c] = other[r][c-col1]
        elif vert == True:
            if col1 != col2:
                raise ValueError("Matrix sizes do not match")
            temp = zeros(row1 + row2, col1)
            rowsize, colsize = temp.rows, temp.cols
            for r in range(rowsize):
                for c in range(colsize):
                    if r < row1:
                        temp[r][c] = self[r][c]
                    else:
                        temp[r][c] = other[r-row1][c]
        return temp
    def slice(self, start, end, vert = True):
        if vert == True:
            rows, cols = self.rows, end - start
            temp = zeros(rows, cols)
            for r in range(rows):
                for c in range(cols):
                    # print('temp',(r,c))
                    # print('matr',(r,c + start))
                    temp[r][c] = self[r][c+start]
        elif vert == False:
            rows, cols = end - start, self.cols
            temp = zeros(rows, cols)
            for r in range(rows):
                for c in range(cols):
                    temp[r][c] = self[r+start][c]
        return temp

        
    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.rows:
            return
        temp = self.copy()
        for r in range(self.rows):
            for c in range(self.cols):
                temp[r][c] += + other[r][c]
        return temp
    def __mul__(self, other):
        if isinstance(other, RealMatrix):
            if self.cols != other.rows:
                raise ValueError
            temp = zeros(self.rows, other.cols)
            for r in range(self.rows):
                for c in range(other.cols):
                    v = ZERO
                    for i in range(self.cols):
                        v += self[r][i]*other[i][c]
                    temp[r][c] = v
            return temp
        else:
            temp = zeros(self.rows, self.cols)
            for r in range(self.rows):
                for c in range(self.cols):
                    temp.set(self.get(r,c)*other, r, c)
            return temp
    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.rows:
            return
        temp = zeros(self.rows, self.cols)
        for r in range(self.rows):
            for c in range(self.cols):
                temp[r][c] += self[r][c]
                temp[r][c] -= other[r][c]
        return temp
    
    # swapping r1 and r2
    def row_swap(self, row1, row2):        
        for col in range(self.cols):
            self[row1][col], self[row2][col] = self[row2][col], self[row1][col]
    # multiplying $row$ by factor
    def row_mul(self, row, factor):        
        for col in range(self.cols):
            self[row][col] = self[row][col]*factor
    # adding row2*factor to row1
    def row_add(self, row1, row2, factor):  
        for col in range(self.cols):
            self[row1][col] = self[row1][col] + self[row2][col]*factor
    
    def ref(self):
        temp = self.copy()
        rows, cols = temp.rows, temp.cols
        # c, p = 0, 0
        # while c < cols:
        #     r = p
        #     while r < rows:
        #         if temp[c][r] != ZERO:
        #             break
        #         r += 1
        #     if r == rows:
        #         c += 1
        #         continue
        #     if r != p:
        #         temp.row_swap(p, r)
        #     pivot_ele = temp[p][c]
        #     for i in range(p+1, rows):
        #         curr_ele = temp[i][c]
        #         if curr_ele == ZERO:
        #             continue
        #         factor = ZERO - (curr_ele/pivot_ele)
        #         temp.row_add(i, p, factor)   
        #     p += 1
        #     c += 1
        # return temp

        p = 0
        for c in range(cols):
            r = p
            for r in range(p, rows+1):
                if r == rows or temp[c][r] != ZERO:
                    r = r
                    break
            if r == rows:
                continue
            if r != p:
                print(temp, f'\n >>> R{p+1} <-> R{r+1}') if DEBUGMODE else None
                temp.row_swap(p, r)
            pivot_ele = temp[p][c]
            for i in range(p+1, rows):
                curr_ele = temp[i][c]
                if curr_ele == ZERO:
                    continue
                factor = ZERO - (curr_ele/pivot_ele)
                print(temp, f'\n >>> R{i+1} + {factor} X R{p+1}') if DEBUGMODE else None
                temp.row_add(i, p, factor)
            p += 1
        return temp
    def rref(self):
        temp = self.ref()
        rows, cols = temp.rows, temp.cols
        r, p = rows-1,  cols
        for r in range(rows):
            r = (rows-1) - r
            c = 0
            for c in range(p+1):
                if c == p or temp[r][c] != ZERO:
                    c = c
                    break
            if c == p:
                continue
            if temp[r][c] != ONE:
                factor = ONE/temp[r][c]
                print(temp, f'\n >>> R{r+1} X {factor}') if DEBUGMODE else None
                temp.row_mul(r, factor)
            for i in range(0,r):
                curr_ele = temp[i][c]
                if curr_ele == ZERO:
                    continue
                factor = ZERO - curr_ele
                print(temp, f'\n >>> R{i+1} + {factor} X R{r+1}') if DEBUGMODE else None
                temp.row_add(i, r, factor)
            p = c
        return temp
    def inv(self):
        if self.rows != self.cols:
            raise ValueError("Not a square matrix")
        size = self.rows
        temp = self.combine(eye(size), vert = False)
        temp = temp.rref().slice(size, 2 * size)
        return temp

def zeros(m,n):
    return RatMatrix(m,n)
def eye(n):
    temp = RatMatrix(n,n)
    for i in range(n):
        temp[i][i] = ONE
    return temp

def combine(mat1, mat2, vert = False):
    return mat1.combine(mat2, vert)

def T(matrix):
    return matrix.T()
def ref(matrix):
    return matrix.ref()
def rref(matrix):
    return matrix.rref()
def inv(matrix):
    return matrix.inv()



class Matrix(RatMatrix):
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
                    try:
                        self[row][col] = Rat(row_input[col])
                    except ValueError:
                        self[row][col] = float(row_input[col])
                repeat = False
            if is_break:
                break


