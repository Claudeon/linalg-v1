# linalg-v1.1
Created specifically for Linear Algebra MA2001. Designed with the MA2001 student in mind.

## Instructions
- Download Python [here](https://www.python.org/downloads/) and IDLE (if applicable).
- Download the files into a single folder and open main.py using IDLE.
- Click Run -> Run Module. Alternatively, press F5.
- Check if all the packages are successfully installed.

## Features
- Initializing a matrix
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
- ERO and ECO Operations
```python
# A = 1 2 3
#     2 1 3
#     1 3 2

A.row_swap(1,2)


```
- Transposing matrix
- Finding RREF with Gauss-Jordan Elimination steps
- Combining matrices with {augmented} and {combine}
- Determinants and Inverse
- Nullspaces and Column spaces

## Contributing
