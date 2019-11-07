from Scenario.trajectory import *


def trajectory_to_2d(time):
    t = trajectory
    f = 350

    x = t[time][1]
    y = t[time][2]
    z = t[time][3]

    x2 = int((f/z)*x)
    y2 = int((f/z)*y)

    return tuple(x2, y2)























