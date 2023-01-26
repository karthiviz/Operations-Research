import numpy as np
import sys
import itertools

def checkRule1(A):
    n,m = A.shape
    '''check if every element in A is 0,1 or -1'''
    for i in range(n):
        for j in range(m):
            if A[i][j] != 0 and A[i][j] !=1 and  A[i][j] != -1:
                return False
    else:
        return True

def checkRule2(A,r,c):
    '''Check if one sub matriz have determinant 0,1 or -1'''
    det=A[r[0]][c[0]]*A[r[1]][c[1]]- A[r[1]][c[0]]*A[r[0]][c[1]]
    if det == 1 or det == -1 or det==0:
        return True
    else:
        return False

def theoremNo2det(A):
    '''
       Check Rule 1 for matrix A 
       Generate all 2x2 submatrices of A and check rule 2
    '''
    if checkRule1(A):
        n,m=A.shape
        N=range(n)
        M=range(m)
        rows=itertools.permutations(N,2)
        columns=itertools.permutations(M,2)
        for r in rows:
            for c in columns:
                if not checkRule2(A,r,c):
                   return False 
        return True

if __name__ == '__main__':
   
    A=np.array([[1,0,1,0],
                [0,1,0,1],
                [1,0,0,1],
                [0,1,1,0]])

    n,m=A.shape
    print(f"{n}:{m}")

    if theoremNo2det(A):
        print ('A is a TU Matrix')