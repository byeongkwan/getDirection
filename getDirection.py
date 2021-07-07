import math
import numpy as np

def getDirection(vector_1, vector_2):
    
    # Calculate dx, dy, and z from two vector
    dx = vector_2[0] - vector_1[0]
    dy = vector_2[1] - vector_1[1]
    z = math.sqrt(dx**2 + dy**2)
    
    # Calculate angle of two vector (0 ~ 359)
    if np.sign(dx) == -1 and np.sign(dy) == -1:
        angle = math.degrees(math.acos(dx/z)) + 90
    elif np.sign(dx) == 0 and np.sign(dy) == -1:
        angle = math.degrees(math.acos(dx/z)) + 180
    elif np.sign(dx) == 1 and np.sign(dy) == -1:
        angle = math.degrees(math.acos(dx/z)) + 270
    else:
        angle = math.degrees(math.acos(dx/z))
    
    # Determine cardianl point according to the angle
    cardinal_points = {"E":(-23, 22), "NE":(23, 67), "N":(68, 112), "NW":(113, 157), "W":(158, 202), "SW":(203, 247), "S":(248, 292), "SE":(293, 337)}
    final_direction = ""

    for direction in cardinal_points:
        range1 = cardinal_points[direction][0]
        range2 = cardinal_points[direction][1]
        if angle >=337:
            angle = 360 - angle
        if angle > range1 and angle <= range2:
            final_direction = direction

    print(f'Angle: {int(angle)}, Directionality: {final_direction}')

    return 0    # Options : angle or int(angle) or final_direction

# Validation
v0 = [0, 0]; v1 = [1, 0]; v2 = [1, 1]; v3 = [0, 1]; v4 = [-1, 1]; v5 = [-1, 0]; v6 = [-1, -1]; v7 = [0, -1]; v8 = [1, -1]

getDirection(v0, v1)
getDirection(v0, v2)
getDirection(v0, v3)
getDirection(v0, v4)
getDirection(v0, v5)
getDirection(v0, v6)
getDirection(v0, v7)
getDirection(v0, v8)
