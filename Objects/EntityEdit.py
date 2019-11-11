class EntityDraw:
    def __init__(self, entity):
        self._matrix = entity.matrix
        self._entity = entity
        self.size = entity._size

    def __str__(self):
        vs = ''
        for x in range(0, self.size[0]):
            for y in range(0, self.size[1]):
                vs += f'({x}, {y}: {self._matrix[x][y]}), '
            print(vs)
            vs = ''
        return 'Objeto printado!'

    def point_1_vs(self, p, color='#000000'):
        self._matrix[p[0]][p[1]] = color

    def point_2(self, p, color='#000000'):
        """ # - ponto passado para a funcao
        #*
        **
        """

        self.point_1_vs((p[0] + 1, p[1]), color)
        self.point_1_vs((p[0], p[1] + 1), color)
        self.point_1_vs((p[0], p[1]), color)
        self.point_1_vs((p[0] + 1, p[1] + 1), color)

    def point_3(self, p, color="#000000"):
        ''' # - ponto passado para a funcao
             *
            *#*
             *
        '''
        self.point_1_vs((p[0], p[1]), color)
        self.point_1_vs((p[0], p[1] - 1), color)
        self.point_1_vs((p[0], p[1] + 1), color)
        self.point_1_vs((p[0] - 1, p[1]), color)
        self.point_1_vs((p[0] + 1, p[1]), color)

    def point_4(self, p, color="#000000"):
        """ # - ponto passado para a funcao

             **
            *#**
            ****
             **
        """
        self.point_1_vs((p[0], p[1]), color)
        self.point_1_vs((p[0] + 1, p[1]), color)
        self.point_1_vs((p[0] + 2, p[1]), color)
        self.point_1_vs((p[0] - 1, p[1]), color)
        self.point_1_vs((p[0], p[1] - 1), color)
        self.point_1_vs((p[0] + 1, p[1] - 1), color)
        self.point_1_vs((p[0] - 1, p[1] + 1), color)
        self.point_1_vs((p[0], p[1] + 1), color)
        self.point_1_vs((p[0] + 1, p[1] + 1), color)
        self.point_1_vs((p[0] + 2, p[1] + 1), color)
        self.point_1_vs((p[0], p[1] + 2), color)
        self.point_1_vs((p[0] + 1, p[1] + 2), color)

    def fill(self, p, color='#000000'):
        print("In Fill")
        lista = list()
        x = p
        lista.append(x)
        while (len(lista) != 0):
            high = (x[0] > 0 and x[1] > 0)
            low = (x[0] < self.size[0] and x[1] < self.size[1])
            if color != self._matrix[x[0]][x[1]] and high and low:
                self.point_1_vs(x, color)
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
                    self.point_1_vs((x1, y1), color)
                    p = p - dY
                    if (p < 0):
                        y1 = y1 + yInc
                        p = p + dX
                    x1 = x1 + xInc
            else:
                p = dY / 2
                while (y1 != y2):
                    self.point_1_vs((x1, y1), color)
                    p = p - dX
                    if (p < 0):
                        x1 = x1 + xInc
                        p = p + dY
                    y1 = y1 + yInc
                self.point_1_vs((x1, y1), color)

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
            self.point_1_vs((x + c[0], y + c[1]), color)
            self.point_1_vs((-x + c[0], y + c[1]), color)
            self.point_1_vs((-x + c[0], -y + c[1]), color)
            self.point_1_vs((x + c[0], -y + c[1]), color)
            self.point_1_vs((y + c[0], x + c[1]), color)
            self.point_1_vs((-y + c[0], x + c[1]), color)
            self.point_1_vs((-y + c[0], -x + c[1]), color)
            self.point_1_vs((y + c[0], -x + c[1]), color)
            while (x < y):
                x += 1
                if (p < 0):
                    p += 2 * x + 1
                else:
                    y = y - 1
                    p += 2 * x + 1 - 2 * y
                self.point_1_vs((x + c[0], y + c[1]), color)
                self.point_1_vs((-x + c[0], y + c[1]), color)
                self.point_1_vs((-x + c[0], -y + c[1]), color)
                self.point_1_vs((x + c[0], -y + c[1]), color)
                self.point_1_vs((y + c[0], x + c[1]), color)
                self.point_1_vs((-y + c[0], x + c[1]), color)
                self.point_1_vs((-y + c[0], -x + c[1]), color)
                self.point_1_vs((y + c[0], -x + c[1]), color)

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