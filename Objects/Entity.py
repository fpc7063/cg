from Objects.EntityEdit import *


class Entity:
    def __init__(self, vs_entity, size):
        # vs_entity is the virtual screen the entity is going to be places
        # size is a tuple, changing size may occur in mal function
        # velocity - will NOT be implemented
        # draw is the image's function to print on the matrix, used only once
        self._coord_point = None
        self._size = size
        self.matrix = [[None for y in range(size[1] + 1)] for x in range(size[0] + 1)]
        # self._velocity = velocity
        # self._draw = draw
        self._Vs_entity = vs_entity
        self._on = False
        self.appended_objects = []

    def append_object(self, obj):
        self.appended_objects.append([obj[0], obj[1]])

    def __str__(self):
        entity = f'Main Coordenate: {self._coord_point}\n'
        for x in range(0, self._size[0]):
            for y in range(0, self._size[1]):
                xy = (x + self._coord_point[0], y + self._coord_point[1])
                entity += f'({xy[0]}, {xy[1]}: {self.matrix[xy[0]][xy[1]],})'
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
        self._coord_point = new_cord_point
        if (len(self.appended_objects) != 0) and (new_cord_point[2] == True):
            for o in self.appended_objects:
                o[0].draw((self._coord_point[0] - o[1][0], self._coord_point[1] - o[1][1]))
        else:
            try:
                for o in self.appended_objects:
                    o[0].undraw()
            except:
                pass
        for x in range(0, self._size[0]):
            for y in range(0, self._size[1]):
                xy = (x + new_cord_point[0], y + new_cord_point[1])
                color = self.matrix[x][y]
                self._Vs_entity.point_1_screen((xy[0], xy[1]), color)
        self._on = True


def set_matrix_module(module):
    editer = EntityDraw(module)

    editer.circle((100, 100), 20, 1, '#0F0FFF')
    # quadrado
    editer.line((80, 80), (80, 121), 1, '#0F0FFF')
    editer.line((80, 121), (122, 121), 1, '#0F0FFF')
    editer.line((122, 121), (122, 80), 1, '#0F0FFF')
    editer.line((122, 80), (80, 80), 1, '#0F0FFF')
    # retangulo
    editer.line((80, 80), (80, 60), 1, '#0F0FFF')
    editer.line((80, 60), (122, 60), 1, '#0F0FFF')
    editer.line((122, 60), (122, 80), 1, '#0F0FFF')
    # pernas esquerda
    editer.line((80, 80), (65, 65), 1, '#0F0FFF')
    editer.line((65, 65), (65, 40), 1, '#0F0FFF')
    editer.line((65, 40), (70, 40), 1, '#0F0FFF')
    editer.line((65, 40), (60, 40), 1, '#0F0FFF')
    # perna direita
    editer.line((121, 81), (136, 66), 1, '#0F0FFF')
    editer.line((136, 66), (136, 40), 1, '#0F0FFF')
    editer.line((136, 40), (141, 40), 1, '#0F0FFF')
    editer.line((136, 40), (131, 40), 1, '#0F0FFF')
    # complementos
    editer.line((122, 60), (137, 55), 1, '#0F0FFF')
    editer.line((122, 60), (131, 70), 1, '#0F0FFF')

    editer.line((80, 60), (65, 55), 1, '#0F0FFF')
    editer.line((80, 60), (70, 69), 1, '#0F0FFF')

    # circulos na parte de cima

    editer.circle((88, 125), 3, 1, '#0F0FFF')
    editer.circle((115, 125), 3, 1, '#0F0FFF')

    # orelha
    editer.line((79, 105), (69, 105), 1, '#0F0FFF')
    editer.line((74, 105), (74, 110), 1, '#0F0FFF')
    editer.line((74, 105), (74, 100), 1, '#0F0FFF')

    editer.line((122, 105), (132, 105), 1, '#0F0FFF')
    editer.line((127, 105), (127, 110), 1, '#0F0FFF')
    editer.line((127, 105), (127, 100), 1, '#0F0FFF')

    # thruster
    editer.line((100, 60), (90, 45), 1, '#0F0FFF')
    editer.line((90, 45), (110, 45), 1, '#0F0FFF')
    editer.line((110, 45), (100, 60), 1, '#0F0FFF')


def set_matrix_thruster(thruster):
    editer = EntityDraw(thruster)

    # chama grande
    editer.circle((100, 150), 30, 1, '#FFE845')
    editer.fill((98, 167), '#FFE845')
    editer.line((70, 150), (100, 20), 1, '#FFE845')
    editer.line((100, 20), (130, 150), 1, '#FFE845')
    editer.line((130, 150), (70, 150), 1, '#FFE845')
    editer.fill((98, 59), '#FFE845')
    # chama pequena
    editer.circle((100, 130), 20, 1, '#FF553F')
    editer.fill((103, 138), '#FF553F')
    editer.line((80, 125), (100, 70), 1, '#FF553F')
    editer.line((100, 70), (120, 125), 1, '#FF553F')
    editer.line((120, 125), (80, 125), 1, '#FF553F')
    editer.fill((100, 98), '#FF553F')