from graphics import Point

def getMouse(tela, point):
    print(f"In GetMouse - {point}")
    x = (int(point.getX()), int(point.getY()))
    print(x)

    tela.point_4(x, '#FFFFFF')
    tela.win.update()
    print(f"Out GetMouse - {x}")
    return x