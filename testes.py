import numpy as np

def curva(a,b,c):
    a = (733, 465)
    b = (645, 515)
    c = (819, 584)
    abc = a + b + c
    m = min(abc) - 1
    newA = (a[0] - m, a[1] - m)
    newB = (b[0] - m, b[1] - m)
    newC = (c[0] - m, c[1] - m)
    print(newA + newB + newC)



    A = np.array([[newA[0]**2, newA[0], 1],
                  [newB[0]**2, newB[0], 1],
                  [newC[0]**2, newC[0], 2]])
    B = np.array([newA[1], newB[1], newC[1]])
    X2 = np.linalg.solve(A,B)
    print(X2)

    X2_int = [int(X2[0]),int(X2[1]),int(X2[2])]
    print(X2_int)
    return X2_int