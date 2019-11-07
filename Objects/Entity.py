class Entity:
    def __init__(self, vs_entity, size):
        # vs_entity is the virtual screen the entity is going to be places
        # size is a tuple, changing size may occur in mal function
        # velocity - will NOT be implemented
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