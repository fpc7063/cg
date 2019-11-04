from VScreen import *
from getMouse import *
#from testes import *


size = (1000, 700)
win = GraphWin("Batata", size[0], size[1], autoflush=False)
tela = VScreen(win, size)






'''pontos = []
for i in range(15):
    ponto = getMouse(tela,win.getMouse())
    pontos.append(ponto)
print(pontos)'''


'''abc = curva()
for x in range(839, 940 + 1):
    y = abc[0]*(x**2) + abc[1]*x + abc[2]
    print(f"x: {x}, y: {int(y)}")
    tela.point_1((int(x),int(y)), '#0000FF')'''























win.getMouse()
win.close()
