from graphics import GraphWin
from VScreen import *
from getMouse import *
# from testes import *
from trajectory import trajectory
import time


size = (1000, 700)
tela = VScreen("Batata", size)
module = Entity(tela, (100, 100))
trajectory_module = trajectory

for x in range(200, 300):
    module.draw((x, x))
    time.sleep(0.01)

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
