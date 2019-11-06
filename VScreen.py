import random
from create_scenario import *
from graphics import GraphWin


class Entity:
    def __init__(self, vs_entity, size):
        # vs_entity is the virtual screen the entity is going to be places
        # size is a tuple, changing size may occur in mal function
        # velocity
        # draw is the image's function to print on the matrix, used only once
        self._coord_point = None
        self._size = size
        self._matrix = [["#00FF00" for y in range(size[1] + 1)] for x in range(size[0] + 1)]
        #self._velocity = velocity
        #self._draw = draw
        self._Vs_entity = vs_entity
        self._on = False

    def __str__(self):
        entity = f'Main Coordenate: {self._coord_point}\n'
        for x in range(0, self._size[0]):
            for y in range(0, self._size[1]):
                xy = (x + self._coord_point[0], y + self._coord_point[1])
                entity += f'({xy[0]}, {xy[1]}: {self._matrix[xy[0]][xy[1]], })'
            entity += '\n'
        return entity

    def move(self, direction):
        if direction == 'left':
            self.draw(self._coord_point[0] - 1)
        if direction == 'right':
            self.draw(self._coord_point[0] + 1)

        if direction == 'up':
            self.draw(self._coord_point[1] + 1)
        if direction == 'down':
            self.draw(self._coord_point[1] - 1)

    def undraw(self):
        for x in range(0, self._size[0]):
            for y in range(0, self._size[1]):
                xy = (x + self._coord_point[0], y + self._coord_point[1])
                color = self._Vs_entity.get_point_color((xy[0], xy[1]))
                self._Vs_entity.point_1((xy[0], xy[1]), color)

    def draw(self, new_cord_point):
        if self._on:
            self.undraw()
        for x in range(0, self._size[0]):
            for y in range(0, self._size[1]):
                xy = (x + new_cord_point[0], y + new_cord_point[1])
                color = self._matrix[x][y]
                self._Vs_entity.point_1_screen((xy[0], xy[1]), color)
        self._coord_point = new_cord_point
        self._on = True
        self._Vs_entity.refresh()







class VScreen():
    def __init__(self, name, size):
        """Size is a Tuple(x,y)
            Win is a GraphWin from graphics.py"""
        self.__matrix = [["#000000" for y in range(size[1] + 1)] for x in range(size[0] + 1)]
        self.win = win = GraphWin(name, size[0], size[1], autoflush=False)
        self.win.setCoords(0, 0, size[0], size[1])
        self.win.setBackground("black")
        self.size = size
        scenario(self)

    def refresh(self):
        self.win.update()

    def get_point_color(self, p):
        return self.__matrix[p[0]][p[1]]

    def __str__(self):
        vs = ''
        for x in range(0, self.size[0]):
            for y in range(0, self.size[1]):
                vs += f'({x}, {y}: {self.__matrix[x][y]}), '
            print(vs)
            vs = ''
        return 'Objeto printado!'

    def point_1_screen(self, p, color='#000000'):
        self.win.plot(p[0], p[1], color)

    def point_1(self, p, color='#000000'):
        self.__matrix[p[0]][p[1]] = color
        self.win.plot(p[0], p[1], color)

    def point_2(self, p, color='#000000'):
        """ # - ponto passado para a funcao
        #*
        **
        """

        self.point_1((p[0] + 1, p[1]), color)
        self.point_1((p[0], p[1] + 1), color)
        self.point_1((p[0], p[1]), color)
        self.point_1((p[0] + 1, p[1] + 1), color)

    def point_3(self, p, color="#000000"):
        ''' # - ponto passado para a funcao
             *
            *#*
             *
        '''
        self.point_1((p[0], p[1]), color)
        self.point_1((p[0], p[1] - 1), color)
        self.point_1((p[0], p[1] + 1), color)
        self.point_1((p[0] - 1, p[1]), color)
        self.point_1((p[0] + 1, p[1]), color)

    def point_4(self, p, color="#000000"):
        """ # - ponto passado para a funcao

             **
            *#**
            ****
             **
        """
        self.point_1((p[0], p[1]), color)
        self.point_1((p[0] + 1, p[1]), color)
        self.point_1((p[0] + 2, p[1]), color)
        self.point_1((p[0] - 1, p[1]), color)
        self.point_1((p[0], p[1] - 1), color)
        self.point_1((p[0] + 1, p[1] - 1), color)
        self.point_1((p[0] - 1, p[1] + 1), color)
        self.point_1((p[0], p[1] + 1), color)
        self.point_1((p[0] + 1, p[1] + 1), color)
        self.point_1((p[0] + 2, p[1] + 1), color)
        self.point_1((p[0], p[1] + 2), color)
        self.point_1((p[0] + 1, p[1] + 2), color)

    def fill(self, p, color='#000000'):
        print("In Fill")
        lista = list()
        x = p
        lista.append(x)
        while (len(lista) != 0):
            high = (x[0] > 0 and x[1] > 0)
            low = (x[0] < self.size[0] and x[1] < self.size[1])
            if color != self.__matrix[x[0]][x[1]] and high and low:
                self.point_1(x, color)
                lista.append((x[0] + 1, x[1]))
                lista.append((x[0], x[1] + 1))
                lista.append((x[0] - 1, x[1]))
                lista.append((x[0], x[1] - 1))
            x = lista.pop(0)
        print("Out Fill")

    # Linhas
    def line(self, p1, p2, size, color='#000000'):
        if (size == 1):
            x1 = p1[0]
            y1 = p1[1]
            x2 = p2[0]
            y2 = p2[1]
            p = 0
            dX = x2 - x1
            dY = y2 - y1
            xInc = 1
            yInc = 1

            if (dX < 0):
                xInc = -1
                dX = -dX
            if (dY < 0):
                yInc = -1
                dY = -dY
            if (dY <= dX):
                p = dX / 2
                while (x1 != x2):
                    self.point_1((x1, y1), color)
                    p = p - dY
                    if (p < 0):
                        y1 = y1 + yInc
                        p = p + dX
                    x1 = x1 + xInc
            else:
                p = dY / 2
                while (y1 != y2):
                    self.point_1((x1, y1), color)
                    p = p - dX
                    if (p < 0):
                        x1 = x1 + xInc
                        p = p + dY
                    y1 = y1 + yInc
                self.point_1((x1, y1), color)

        elif (size == 2):
            x1 = p1[0]
            y1 = p1[1]
            x2 = p2[0]
            y2 = p2[1]
            p = 0
            dX = x2 - x1
            dY = y2 - y1
            xInc = 1
            yInc = 1

            if (dX < 0):
                xInc = -1
                dX = -dX
            if (dY < 0):
                yInc = -1
                dY = -dY
            if (dY <= dX):
                p = dX / 2
                while (x1 != x2):
                    self.point_2((x1, y1), color)
                    p = p - dY
                    if (p < 0):
                        y1 = y1 + yInc
                        p = p + dX
                    x1 = x1 + xInc
            else:
                p = dY / 2
                while (y1 != y2):
                    self.point_2((x1, y1), color)
                    p = p - dX
                    if (p < 0):
                        x1 = x1 + xInc
                        p = p + dY
                    y1 = y1 + yInc
                self.point_2((x1, y1), color)

        elif (size == 3):
            x1 = p1[0]
            y1 = p1[1]
            x2 = p2[0]
            y2 = p2[1]
            p = 0
            dX = x2 - x1
            dY = y2 - y1
            xInc = 1
            yInc = 1

            if (dX < 0):
                xInc = -1
                dX = -dX
            if (dY < 0):
                yInc = -1
                dY = -dY
            if (dY <= dX):
                p = dX / 2
                while (x1 != x2):
                    self.point_3((x1, y1), color)
                    p = p - dY
                    if (p < 0):
                        y1 = y1 + yInc
                        p = p + dX
                    x1 = x1 + xInc
            else:
                p = dY / 2
                while (y1 != y2):
                    self.point_3((x1, y1), color)
                    p = p - dX
                    if (p < 0):
                        x1 = x1 + xInc
                        p = p + dY
                    y1 = y1 + yInc
                self.point_3((x1, y1), color)

        elif (size == 4):
            x1 = p1[0]
            y1 = p1[1]
            x2 = p2[0]
            y2 = p2[1]
            p = 0
            dX = x2 - x1
            dY = y2 - y1
            xInc = 1
            yInc = 1

            if (dX < 0):
                xInc = -1
                dX = -dX
            if (dY < 0):
                yInc = -1
                dY = -dY
            if (dY <= dX):
                p = dX / 2
                while (x1 != x2):
                    self.point_4((x1, y1), color)
                    p = p - dY
                    if (p < 0):
                        y1 = y1 + yInc
                        p = p + dX
                    x1 = x1 + xInc
            else:
                p = dY / 2
                while (y1 != y2):
                    self.point_4((x1, y1), color)
                    p = p - dX
                    if (p < 0):
                        x1 = x1 + xInc
                        p = p + dY
                    y1 = y1 + yInc
                self.point_4((x1, y1), color)

    # Circulo
    def circle(self, c, r, size, color="#000000"):
        print("In Circle")
        if (size == 1):
            # c eh o PONTO DO CENTRO DO CIRCULO
            # r eh o RAIO do circulo
            x = 0
            y = r
            p = 5 / 4 - r
            self.point_1((x + c[0], y + c[1]), color)
            self.point_1((-x + c[0], y + c[1]), color)
            self.point_1((-x + c[0], -y + c[1]), color)
            self.point_1((x + c[0], -y + c[1]), color)
            self.point_1((y + c[0], x + c[1]), color)
            self.point_1((-y + c[0], x + c[1]), color)
            self.point_1((-y + c[0], -x + c[1]), color)
            self.point_1((y + c[0], -x + c[1]), color)
            while (x < y):
                x += 1
                if (p < 0):
                    p += 2 * x + 1
                else:
                    y = y - 1
                    p += 2 * x + 1 - 2 * y
                self.point_1((x + c[0], y + c[1]), color)
                self.point_1((-x + c[0], y + c[1]), color)
                self.point_1((-x + c[0], -y + c[1]), color)
                self.point_1((x + c[0], -y + c[1]), color)
                self.point_1((y + c[0], x + c[1]), color)
                self.point_1((-y + c[0], x + c[1]), color)
                self.point_1((-y + c[0], -x + c[1]), color)
                self.point_1((y + c[0], -x + c[1]), color)

        elif (size == 2):
            # c eh o PONTO DO CENTRO DO CIRCULO
            # r eh o RAIO do circulo
            x = 0
            y = r
            p = 5 / 4 - r
            self.point_2((x + c[0], y + c[1]), color)
            self.point_2((-x + c[0], y + c[1]), color)
            self.point_2((-x + c[0], -y + c[1]), color)
            self.point_2((x + c[0], -y + c[1]), color)
            self.point_2((y + c[0], x + c[1]), color)
            self.point_2((-y + c[0], x + c[1]), color)
            self.point_2((-y + c[0], -x + c[1]), color)
            self.point_2((y + c[0], -x + c[1]), color)
            while (x < y):
                x += 1
                if (p < 0):
                    p += 2 * x + 1
                else:
                    y = y - 1
                    p += 2 * x + 1 - 2 * y
                self.point_2((x + c[0], y + c[1]), color)
                self.point_2((-x + c[0], y + c[1]), color)
                self.point_2((-x + c[0], -y + c[1]), color)
                self.point_2((x + c[0], -y + c[1]), color)
                self.point_2((y + c[0], x + c[1]), color)
                self.point_2((-y + c[0], x + c[1]), color)
                self.point_2((-y + c[0], -x + c[1]), color)
                self.point_2((y + c[0], -x + c[1]), color)

        elif (size == 3):
            # c eh o PONTO DO CENTRO DO CIRCULO
            # r eh o RAIO do circulo
            x = 0
            y = r
            p = 5 / 4 - r
            self.point_3((x + c[0], y + c[1]), color)
            self.point_3((-x + c[0], y + c[1]), color)
            self.point_3((-x + c[0], -y + c[1]), color)
            self.point_3((x + c[0], -y + c[1]), color)
            self.point_3((y + c[0], x + c[1]), color)
            self.point_3((-y + c[0], x + c[1]), color)
            self.point_3((-y + c[0], -x + c[1]), color)
            self.point_3((y + c[0], -x + c[1]), color)
            while (x < y):
                x += 1
                if (p < 0):
                    p += 2 * x + 1
                else:
                    y = y - 1
                    p += 2 * x + 1 - 2 * y
                self.point_3((x + c[0], y + c[1]), color)
                self.point_3((-x + c[0], y + c[1]), color)
                self.point_3((-x + c[0], -y + c[1]), color)
                self.point_3((x + c[0], -y + c[1]), color)
                self.point_3((y + c[0], x + c[1]), color)
                self.point_3((-y + c[0], x + c[1]), color)
                self.point_3((-y + c[0], -x + c[1]), color)
                self.point_3((y + c[0], -x + c[1]), color)


        elif (size == 4):
            # c eh o PONTO DO CENTRO DO CIRCULO
            # r eh o RAIO do circulo
            x = 0
            y = r
            p = 5 / 4 - r
            self.point_4((x + c[0], y + c[1]), color)
            self.point_4((-x + c[0], y + c[1]), color)
            self.point_4((-x + c[0], -y + c[1]), color)
            self.point_4((x + c[0], -y + c[1]), color)
            self.point_4((y + c[0], x + c[1]), color)
            self.point_4((-y + c[0], x + c[1]), color)
            self.point_4((-y + c[0], -x + c[1]), color)
            self.point_4((y + c[0], -x + c[1]), color)
            while (x < y):
                x += 1
                if (p < 0):
                    p += 2 * x + 1
                else:
                    y = y - 1
                    p += 2 * x + 1 - 2 * y
                self.point_4((x + c[0], y + c[1]), color)
                self.point_4((-x + c[0], y + c[1]), color)
                self.point_4((-x + c[0], -y + c[1]), color)
                self.point_4((x + c[0], -y + c[1]), color)
                self.point_4((y + c[0], x + c[1]), color)
                self.point_4((-y + c[0], x + c[1]), color)
                self.point_4((-y + c[0], -x + c[1]), color)
                self.point_4((y + c[0], -x + c[1]), color)
        print("Out Circle")
