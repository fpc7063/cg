import random


def scenario(tela):
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

    #Sol
    sunPoint = (80, tela.size[1] - 80)
    sunColor = "#FFD94F"
    tela.circle(sunPoint, 50, 4, sunColor)
    tela.fill(sunPoint, sunColor)

    # Terra
    earth_point = (807, 560)
    earth_color = '#0000FF'
    tela.circle(earth_point, 80, 4, earth_color)
    tela.fill(earth_point, earth_color)

    #717171 - Montanha
    color_montanha = '#717171'
    tela.line((0, 275), (324, 275), 1, color_montanha)
    tela.line((324, 275), (420, 205), 1, color_montanha)
    tela.line((420, 205), (tela.size[0], 205), 1, color_montanha)
    tela.line((420, 205), (0, 205), 1, color_montanha)
    tela.fill((240, 247), color_montanha)

    #A3A3A3 - Planice sombreada
    color_planice_sombreada = '#A3A3A3'
    tela.line((420, 205), (0, 205), 1, color_planice_sombreada)
    tela.line((420, 205), (410, 160), 1, color_planice_sombreada)
    tela.line((410, 160), (0, 160), 1, color_planice_sombreada)
    tela.fill((273, 176), '#A3A3A3')

    #C3C3C3 - Planice
    color_planice = '#C3C3C3'
    tela.line((410, 160), (0, 160), 1, color_planice)
    tela.line((420, 205), (410, 160), 1, color_planice)
    tela.line((420, 205), (tela.size[0], 205), 1, color_planice)
    tela.fill((630, 157), color_planice)



    #Rocks
    # X: 0 -> size[0] - 1
    # Y: 0 -> 205
    # x = random.randint(0, tela.size[0] -1)
    # y = random.randint(0, 205)
    pontos = [(64, 168), (86, 96), (282, 87), (192, 50), (242, 126), (430, 116), (406, 32), (665, 146), (518, 76),
              (693, 52), (788, 145), (850, 94), (926, 140), (798, 39), (781, 88)]

    color_rock = '#839373'
    color_rock_dark = '#637353'
    for p in pontos:
        x = p[0]
        y = p[1]

        z = random.randint(10, 18)
        p1 = [int(x - z // 2), int(y + (z * 1.7) / 2)]
        p2 = [int(x + z / 2), int(y + (z * 1.7) / 2)]
        p3 = [x + z, y]
        p4 = [int(x + z / 2), int(y - (z * 1.7) / 2)]
        p5 = [int(x - z / 2), int(y - (z * 1.7) / 2)]
        p6 = [x - z, y]
        pontos_hex = [p1, p2, p3, p4, p5, p6]

        def r(z):
            return random.randint(z//5, (z//5)*2)

        for pX in pontos_hex:
            pX[0] += r(z)
            pX[1] += r(z)


        if(p[0] >= tela.size[0]//2):
            tela.line(p3, p, 1, color=color_rock)
            tela.line(p, p5, 1, color=color_rock)
            tela.line(p1, p2, 1, color=color_rock)
            tela.line(p2, p3, 1, color=color_rock)
            tela.line(p5, p6, 1, color=color_rock)
            tela.line(p6, p1, 1, color=color_rock)
            tela.fill((p[0], p[1] + 3), color=color_rock)

            tela.line(p3, p, 1, color=color_rock_dark)
            tela.line(p, p5, 1, color=color_rock_dark)
            tela.line(p3, p4, 1, color=color_rock_dark)
            tela.line(p4, p5, 1, color=color_rock_dark)
            tela.fill((p[0] + 3, p[1] - 3), color=color_rock_dark)
        else:
            tela.line(p3, p, 1, color=color_rock)
            tela.line(p, p5, 1, color=color_rock)
            tela.line(p1, p2, 1, color=color_rock)
            tela.line(p2, p3, 1, color=color_rock)
            tela.line(p5, p6, 1, color=color_rock)
            tela.line(p6, p1, 1, color=color_rock)
            tela.fill((p[0], p[1] + 3), color=color_rock)

            tela.line(p3, p, 1, color=color_rock_dark)
            tela.line(p, p6, 1, color=color_rock_dark)
            tela.line(p3, p4, 1, color=color_rock_dark)
            tela.line(p4, p5, 1, color=color_rock_dark)
            tela.line(p5, p6, 1, color=color_rock_dark)
            tela.fill((p[0] + 3, p[1] - 3), color=color_rock_dark)

    tela.win.update()
    print("Out Scenario")













def module(tela):
    pass