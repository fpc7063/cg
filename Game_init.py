from Objects.VScreen import *
from Objects.Entity import *
from Objects.getMouse import *
from Scenario.trajectory import *
import time


size = (1000, 700)
tela = VScreen("Batata", size)
module = Entity(tela, (100, 100))

for t in range(0, 32):
    p = trajectory_to_2d(t)
    module.draw((p[0], p[1]))
    time.sleep(0.5)











'''pontos = []
for i in range(1):
    ponto = getMouse(tela, tela.win.getMouse())
    pontos.append(ponto)
print(pontos)'''


'''abc = curva()
for x in range(839, 940 + 1):
    y = abc[0]*(x**2) + abc[1]*x + abc[2]
    print(f"x: {x}, y: {int(y)}")
    tela.point_1((int(x),int(y)), '#0000FF')'''























tela.win.getMouse()
tela.win.close()
