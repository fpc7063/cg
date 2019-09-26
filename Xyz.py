

class Cube():
    def __init__(self, coords, color):
        def consctructCube(coords):
            pass
        # coords = ((x,y,z),(x1,y1,z1),(x2,y2,z2),(x3,y3,z3))
        self.mtx[coords[0][0]][coords[0][1]][coords[0][2]] = color
        self.mtx[coords[1][0]][coords[1][1]][coords[1][2]] = color
        self.mtx[coords[2][0]][coords[2][1]][coords[2][2]] = color
        self.mtx[coords[3][0]][coords[3][1]][coords[3][2]] = color
        self.color = color
        self.index = 0



    def destroyCube(self):
        pass



    #Getters
    def getPoint(self, p):
        return self.mtx[p[0]][p[1]][p[2]] #return color of the point



    #Setters
    def setPoint(self, p, color):
        self.mtx[p[0]][p[1]][p[2]] = color

    def setIndex(self, index):
        self.index = index
















class Xyz():
    def __init__(self, cam_coords):
        self.mtx = [[[('Obj_cod', '') for x in range(10000)] for y in range(10000)] for z in range(10000)]
        self.Cube = Cube()

        self.cam = (cam_coords[0], cam_coords[1], cam_coords[2])  # get's a (x,y) for the cam position
        self.objects = list()


    def createCube(self, coords, color = '#000000'):
        # coords = ((x,y,z),(x1,y1,z1),(x2,y2,z2),(x3,y3,z3))
        cubo = Cube(coords, color)
        self.objects.append(cubo)


    #Getters
    def getPointColor(self, p):
        return self.mtx[p[0]][p[1]][p[2]]




    #Setters
    def setPointColor(self, p, color):
        #color = '#000000' - '#FFFFFF'
        self.mtx[p[0]][p[1]][p[2]] = color

































Xyz = Xyz((100, 100, 100))
print(Xyz)