def getMouse(tela, point):
    x = (int(point.getX()), int(point.getY()))
    print(x)


    tela.point_3((x[0],x[1], '#FFFFFF'))
    return x