# linalg-v1.1
Created specifically for Linear Algebra MA2001. Designed with the MA2001 student in mind.

## Instructions
- Download Python [here](https://www.python.org/downloads/) and IDLE (if applicable).
- Download the files into a single folder and open main.py using IDLE.
- Click Run -> Run Module. Alternatively, press F5.
- Check if all the packages are successfully installed.

## Features
- Initializing a matrix\n
There are two ways to initialize a matrix. One way is to assign the expression Matrix(m,n) to variable var where m is the number of rows and n is the number of columns. Then, type in the entries
```python
# 1st approach: default assignment 
>>> A = Matrix(3,3)
row 0: 1 2 3
row 1: 2 1 3
row 2: 1 3 2
# 2nd approach: using Python commands
>>> B = Matrix(5,6)
>>> for i in range(5):
        for j in range(6):
            A[i][j] = Rat(i+j)
```
- ERO and ECO Operations \n
Three methods are available: mainly row_swap, row_add, and row_mul. The syntax is as follows:
```python
# matrix variable name + dot + followed by method_name and arguments

>>> matrix = Matrix(4,6)
>>> matrix.row_swap(row1, row2)
>>> matrix.row_mul(row, factor)
>>> matrix.row_add(row1, row2, factor)
```
Please note that these should be treated as methods not functions, i.e. matrix.row_swap(0,1) NOT row_swap(matrix, 0, 1). Furthermore, this will modify the original matrix, not return a new matrix. An example given below:
```python
# A = 1 2 0
#     2 1 0
#     1 0 2

>>> A.row_swap(1,2)
# A = 1 2 0
#     1 0 2
#     2 1 0
>>> B = A.row_mul(1,10)
>>> print(B)
None

```
- Transposing matrix
- Finding RREF with Gauss-Jordan Elimination steps
- Combining matrices with {augmented} and {combine}
- Determinants and Inverse
- Nullspaces and Column spaces

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
