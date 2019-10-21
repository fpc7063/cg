import random

def scenario(tela):
    def rock(p):
        rz = random.randint(15)
        p1 = (p[0] + 5*rz, p[1] -3*rz)
        p2 = (p[0] + 5*rz, p[1] -3*rz)
        p3 = (p[0], p[1])
        p4 = (p[0], p[1])
        p5 = (p[0], p[1])
        p6 = (p[0], p[1])

    print("In Scenario")

    for i in range(800):
        rand_numberx = random.randint(2, tela.size[0] - 1)
        rand_numbery = random.randint(2, tela.size[1] - 1)
        rand_estrela_type = random.randint(1, 5)
        if(rand_estrela_type == 1):
            tela.point_1((rand_numberx,rand_numbery), '#FFFFFF')
        if (rand_estrela_type == 2):
            tela.point_1((rand_numberx, rand_numbery), '#00FF00')
        if (rand_estrela_type == 3):
            tela.point_1((rand_numberx, rand_numbery), '#FF0000')
        if (rand_estrela_type == 4):
            tela.point_1((rand_numberx, rand_numbery), '#AF0000')
            tela.point_1((rand_numberx + 1, rand_numbery), '#572626')
            tela.point_1((rand_numberx, rand_numbery + 1), '#572626')
            tela.point_1((rand_numberx, rand_numbery - 1), '#572626')
            tela.point_1((rand_numberx - 1, rand_numbery), '#572626')

    sunPoint = (120,tela.size[1] - 120)
    sunColor = "#FFD94F"
    tela.circle(sunPoint, 100, 4, sunColor)
    tela.fill(sunPoint, sunColor)

    tela.line((1, 275),(324,275), 1, '#737373')
    tela.line((324,275), (420, 205), 1, '#737373')
    tela.line((420,205), (tela.size[0], 205), 1, '#737373')

    tela.win.update()
    print("Out Scenario")