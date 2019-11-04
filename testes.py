import numpy as np

def curva():
    a = (940, 523)
    b = (873, 522)
    c = (839, 573)

    a, b, c = np.polyfit(x, y, 2)

    return [a, b, c]


def calcPoint(abc, x_list):
    y_list = []
    for xl in x_list:
        y = abc[0]**xl + abc[1]*xl + abc[2]
        y_list.append(y)
        print(f"x:{x}, y:{y}")
    return y_list

'''abc = curva()
y = calcPoint(abc, [733])'''



'''a = (733, 465)
b = (645, 515)
c = (819, 584)

A = np.array([[a[0]**2,a[0], 1], [b[0]**2, b[0], 1], [c[0]**2, c[0], 1]])
B = np.array([a[1], b[1], c[1]])

x = np.linalg.solve(A, B)
print(x)

teste = np.allclose(np.dot(A, x), B)


print(teste)'''



'''a = np.array([[4, 2, 4], [16, 4, -1], [1 ,1 ,1]])
b = np.array([8, 30, 108])

x = np.linalg.solve(a, b)
print(x)
a = x[0]
b = x[1]
c = x[2]


y = 4*-a + 2*b + c
print(y)
'''

'''xy1 = (940, 523)
xy2 = (873, 522)
xy3 = (839, 573)


x = [940, 839, 873]
y = [523, 573, 522]

a, b, c = np.polyfit(x, y, 2)
print(a,b,c)
calcPoint([a,b,c],[940, 839, 873])'''



x =[0,2,3]
y =[10,0,0]

a, b, c = np.polyfit(x,y,2)
print(a,b,c)


x_vector = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

y_vector = calcPoint([float(a),float(b),float(c)], x_vector)

for i in range(0, len(x)):
    print(f"x:{x[i]}, y:{y[i]}")