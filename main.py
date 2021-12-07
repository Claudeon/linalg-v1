from rational import Rat
from matrix   import RatMatrix, Matrix

def zeros(m,*n):
    if not n:
        return RatMatrix(m,m)
    return RatMatrix(m,*n)
def eye(n):
    temp = RatMatrix(n,n)
    for i in range(n):
        temp[i][i] = ONE
    return temp

def combine(mat1, mat2, vert = False):
    return mat1.combine(mat2, vert)
def augmented(mat1, mat2):
    return mat1.combine(mat2, vert = False)

def T(matrix):
    return matrix.T()
def ref(matrix, show = False):
    return matrix.ref(show = show)
def rref(matrix, show = False):
    return matrix.rref(show = show)
def inv(matrix):
    return matrix.inv()
def det(matrix):
    return matrix.det()
def rank(matrix):
    return matrix.rank()
def nullity(matrix):
    return matrix.nullity()
def null(matrix):
    return matrix.null()

def main():
    print("Package successfully installed!")

if __name__ == "__main__":
    main()
