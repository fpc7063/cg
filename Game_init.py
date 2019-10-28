from VScreen import *
from getMouse import *




size=(1000,700)

win = GraphWin("Batata", size[0], size[1], autoflush=False)
tela = VScreen(win,size)









pontos = []
for i in range(1):
    ponto = getMouse(tela,win.getMouse())
    pontos.append(ponto)
print(pontos)



win.getMouse()
win.close()
