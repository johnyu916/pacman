import json
import math
import os.path
from random import random
from time import time

from wafflecore.compute import new_id, vertices_cube, cuboid_new

def column_geometry_color(x_length, z_length, offset, byte_color):
    geometry = {}
    geometry = []
    for i in range(int(x_length)):
            for j in range(int(z_length)):
                        position = [(i + offset[0]), offset[1], (j + offset[2])]
                        vertices = vertices_cube(position, 1.0, byte_color, 0.05)
                        geometry.extend(vertices)
    return geometry

def column_geometry(x_length, z_length, offset):
    geometry = {}
    geometry = column_geometry_color(x_length, z_length, offset, [38.0, 38.0, 217.0, 255.0])
    return geometry

def column(x_length, z_length):
    geometry = column_geometry(x_length, z_length, [0.0, 0.0, 0.0])
    name = "".join(["blue", str(int(x_length)), "by", str(int(z_length))])
    filename = "/".join(["../geometries", name])
    with open(filename, "w") as f:
        f.write(json.dumps(geometry))
    return 

def rectangle(x_length, z_length):
    geometry = []
    byte_color = [38.0, 38.0, 217.0, 255.0]
    z_s = [0.0, (z_length - 1.0)]
    x_s = [0.0, (x_length - 1.0)]
    for i in range(2):
            z = z_s[int(i)]
            x = x_s[int(i)]
            vertices = column_geometry((x_length - 4.0), 1.0, [2.0, 0.0, z])
            geometry.extend(vertices)
            vertices = column_geometry(1.0, (z_length - 4.0), [x, 0.0, 2.0])
            geometry.extend(vertices)
    cubes = [[1.0, 0.0, 1.0], [1.0, 0.0, (z_length - 2.0)], [(x_length - 2.0), 0.0, 1.0], [(x_length - 2.0), 0.0, (z_length - 2.0)]]
    for cube in cubes:
            vertices = vertices_cube(cube, 1.0, byte_color, 0.05)
            geometry.extend(vertices)
    name = "".join(["blue", str(int(x_length)), "by", str(int(z_length))])
    filename = "/".join(["../geometries", name])
    with open(filename, "w") as f:
        f.write(json.dumps(geometry))
    return 

def c_shape(up_length, side_length, down_length):
    byte_color = [38.0, 38.0, 217.0, 255.0]
    geometry = []
    column = column_geometry(down_length, 1.0, [2.0, 0.0, 0.0])
    geometry.extend(column)
    column = column_geometry(1.0, side_length, [0.0, 0.0, 2.0])
    geometry.extend(column)
    column = column_geometry(up_length, 1.0, [2.0, 0.0, (3.0 + side_length)])
    geometry.extend(column)
    vertices = vertices_cube([1.0, 0.0, 1.0], 1.0, byte_color, 0.05)
    geometry.extend(vertices)
    vertices = vertices_cube([1.0, 0.0, (2.0 + side_length)], 1.0, byte_color, 0.05)
    geometry.extend(vertices)
    filename = "/".join(["../geometries", "blue_c_se"])
    with open(filename, "w") as f:
        f.write(json.dumps(geometry))
    return 

def t_very_long():
    byte_color = [38.0, 38.0, 217.0, 255.0]
    geometry = []
    column = column_geometry(68.0, 1.0, [2.0, 0.0, 0.0])
    geometry.extend(column)
    column = column_geometry(21.0, 1.0, [2.0, 0.0, 7.0])
    geometry.extend(column)
    column = column_geometry(37.0, 1.0, [33.0, 0.0, 7.0])
    geometry.extend(column)
    column = column_geometry(1.0, 4.0, [0.0, 0.0, 2.0])
    geometry.extend(column)
    column = column_geometry(1.0, 4.0, [71.0, 0.0, 2.0])
    geometry.extend(column)
    column = column_geometry(1.0, 1.0, [1.0, 0.0, 1.0])
    geometry.extend(column)
    column = column_geometry(1.0, 1.0, [70.0, 0.0, 1.0])
    geometry.extend(column)
    column = column_geometry(1.0, 1.0, [70.0, 0.0, 6.0])
    geometry.extend(column)
    column = column_geometry(1.0, 1.0, [1.0, 0.0, 6.0])
    geometry.extend(column)
    filename = "/".join(["../geometries", "t_68"])
    with open(filename, "w") as f:
        f.write(json.dumps(geometry))
    return 

def cubes():
    byte_color = [38.0, 38.0, 217.0, 255.0]
    geometry = []
    positions = [[10.0, 0.0, 0.0]]
    for position in positions:
            vertices = vertices_cube(position, 1.0, byte_color, 0.05)
            geometry.extend(vertices)
    filename = "/".join(["../geometries", "stage_cubes"])
    with open(filename, "w") as f:
        f.write(json.dumps(geometry))
    return 

def jail():
    geometry = []
    column = column_geometry(56.0, 1.0, [0.0, 0.0, 0.0])
    geometry.extend(column)
    column = column_geometry(1.0, 30.0, [0.0, 0.0, 1.0])
    geometry.extend(column)
    column = column_geometry(20.0, 1.0, [0.0, 0.0, 31.0])
    geometry.extend(column)
    column = column_geometry(1.0, 2.0, [19.0, 0.0, 29.0])
    geometry.extend(column)
    column = column_geometry(17.0, 1.0, [3.0, 0.0, 28.0])
    geometry.extend(column)
    column = column_geometry(1.0, 24.0, [3.0, 0.0, 4.0])
    geometry.extend(column)
    column = column_geometry(50.0, 1.0, [3.0, 0.0, 3.0])
    geometry.extend(column)
    column = column_geometry(1.0, 24.0, [52.0, 0.0, 4.0])
    geometry.extend(column)
    column = column_geometry(17.0, 1.0, [36.0, 0.0, 28.0])
    geometry.extend(column)
    column = column_geometry(1.0, 2.0, [36.0, 0.0, 29.0])
    geometry.extend(column)
    column = column_geometry(20.0, 1.0, [36.0, 0.0, 31.0])
    geometry.extend(column)
    column = column_geometry(1.0, 30.0, [55.0, 0.0, 1.0])
    geometry.extend(column)
    gateway = column_geometry_color(16.0, 2.0, [20.0, 0.0, 29.0], [236.0, 183.0, 210.0, 255.0])
    geometry.extend(gateway)
    filename = "/".join(["../geometries", "jail"])
    with open(filename, "w") as f:
        f.write(json.dumps(geometry))
    return 

def run():
    jail()
    return 

