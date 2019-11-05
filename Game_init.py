from graphics import GraphWin
from VScreen import *
from getMouse import *
# from testes import *
from trajectory import trajectory


size = (1000, 700)
win = GraphWin("Batata", size[0], size[1], autoflush=False)
tela = VScreen(win, size)
module = Entity(tela, (100,100))
trajectory_module = trajectory

module.draw()

while True:
    break;




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
