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


    tela.line((0, 150),(tela.size[0], 150), 2, '#737373')
    #tela.fill((1, 1), '#737373')
    tela.fill((tela.size[0],1), '#737373')

    tela.win.update()
    print("Out Scenario")