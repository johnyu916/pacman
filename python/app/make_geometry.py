import json
from plugins.jsonsyrup import SyrupEncoder
import math
import os.path
from random import random
from time import time
import numpy

from wafflecore.compute import new_id, vertices_cube, cuboid_new, copy_vertices_color
from wafflecore.standard import array_in_string
from test import test_eyes

def column_geometry_color(x_length, z_length, offset, byte_color):
    geometry = {}
    geometry = []
    for i in range(int(x_length)):
            for j in range(int(z_length)):
                        position = [(i + offset[0]), offset[1], (j + offset[2])]
                        vertices = vertices_cube(position, 1.0, byte_color, 0.05)
                        geometry.extend(vertices)
    return geometry

def column_geometry_color_extend(x_length, z_length, offset, byte_color, geometry):
    geometry.extend(column_geometry_color(x_length, z_length, offset, byte_color))
    return 

def column_geometry(x_length, z_length, offset):
    geometry = {}
    geometry = column_geometry_color(x_length, z_length, offset, [38.0, 38.0, 217.0, 255.0])
    return geometry

def column(x_length, z_length):
    geometry = column_geometry(x_length, z_length, [0.0, 0.0, 0.0])
    name = "".join(["blue", str(int(x_length)), "by", str(int(z_length))])
    filename = "/".join(["../geometries", name])
    with open(filename, "w") as f:
        f.write(json.dumps(geometry, cls=SyrupEncoder))
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
        f.write(json.dumps(geometry, cls=SyrupEncoder))
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
        f.write(json.dumps(geometry, cls=SyrupEncoder))
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
        f.write(json.dumps(geometry, cls=SyrupEncoder))
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
        f.write(json.dumps(geometry, cls=SyrupEncoder))
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
        f.write(json.dumps(geometry, cls=SyrupEncoder))
    return 

def keep_color(r, g, b):
    yes = False
    if ((((r > 0.86) and (r < 0.87)) and ((g > 0.86) and (g < 0.87))) and ((b > 0.86) and (b < 0.87))):
            yes = True
            return yes
    if ((((r > 0.14) and (r < 0.15)) and ((g > 0.14) and (g < 0.15))) and ((b > 0.85) and (b < 0.86))):
            yes = True
            return yes
    return yes

def shadow_copy(vertices, byte_color):
    new_vertices = []
    new_vertices = []
    color = []
    for digit in byte_color:
            color.append((digit / 255.0))
    for vertex in vertices:
            if keep_color(vertex[6], vertex[7], vertex[8]):
                        new_vertex = [vertex[0], vertex[1], vertex[2], vertex[3], vertex[4], vertex[5], vertex[6], vertex[7], vertex[8], vertex[9]]
            else:
                        new_vertex = [vertex[0], vertex[1], vertex[2], vertex[3], vertex[4], vertex[5], color[0], color[1], color[2], color[3]]
            new_vertices.append(new_vertex)
    return new_vertices

def enemy_copy():
    names = ["head_eyes_down", "head_eyes_left", "head_eyes_right", "head_eyes_up", "legs_0", "legs_1"]
    colors = [[[217.0, 29.0, 5.0, 255.0], "shadow"], [[147.0, 254.0, 222.0, 255.0], "bashful"], [[236.0, 183.0, 219.0, 255.0], "speedy"], [[236.0, 182.0, 81.0, 255.0], "pokey"]]
    dir = "../geometries"
    for name in names:
            filepath = "/".join([dir, name])
            if os.path.isfile(filepath):
                        text = None
                        with open(filepath) as f:
                            text = f.read()
                        vertices = json.loads(text)
                        for color in colors:
                                        byte_color = color[0]
                                        character = color[1]
                                        new_vertices = shadow_copy(vertices, byte_color)
                                        new_name = "_".join([character, name])
                                        filename = "/".join(["../geometries", new_name])
                                        with open(filename, "w") as f:
                                            f.write(json.dumps(new_vertices, cls=SyrupEncoder))
    return 

def ghost_geometry_copy(vertices):
    new_vertices = []
    white = [1.0, 1.0, 1.0, 1.0]
    red = [(217.0 / 255.0), (29.0 / 255.0), (5.0 / 255.0), 1.0]
    new_vertices = []
    blue = (200.0 / 255.0)
    for vertex in vertices:
            if (vertex[8] > blue):
                        new_vertex = [vertex[0], vertex[1], vertex[2], vertex[3], vertex[4], vertex[5], white[0], white[1], white[2], white[3]]
            else:
                        new_vertex = [vertex[0], vertex[1], vertex[2], vertex[3], vertex[4], vertex[5], red[0], red[1], red[2], red[3]]
            new_vertices.append(new_vertex)
    return new_vertices

def ghost_copy():
    dir = "../geometries"
    names = ["ghost_head", "ghost_legs_0", "ghost_legs_1"]
    for name in names:
            filepath = "/".join([dir, name])
            if os.path.isfile(filepath):
                        text = None
                        with open(filepath) as f:
                            text = f.read()
                        vertices = json.loads(text)
                        new_vertices = ghost_geometry_copy(vertices)
                        new_name = "_".join(["white", name])
                        filename = "/".join(["../geometries", new_name])
                        with open(filename, "w") as f:
                            f.write(json.dumps(new_vertices, cls=SyrupEncoder))
    return 

def change_filename():
    dirs = ["../things", "../animations", "../geometries"]
    for dir in dirs:
            names = os.listdir(dir)
            for name in names:
                        filepath = "/".join([dir, name])
                        if (os.path.isfile(filepath) and (is_extension(name, "json") == False)):
                                        text = None
                                        with open(filepath) as f:
                                            text = f.read()
                                        new_name = ".".join([name, "json"])
                                        filename = "/".join([dir, new_name])
                                        with open(filename, "w") as f:
                                            f.write(text)
    return 

def make_outside(name, byte_color):
    geometry = []
    column_geometry_color_extend(40.0, 1.0, [0.0, 0.0, 159.0], byte_color, geometry)
    column_geometry_color_extend(1.0, 24.0, [40.0, 0.0, 160.0], byte_color, geometry)
    column_geometry_color_extend(36.0, 1.0, [4.0, 0.0, 184.0], byte_color, geometry)
    column_geometry_color_extend(2.0, 1.0, [2.0, 0.0, 185.0], byte_color, geometry)
    column_geometry_color_extend(1.0, 2.0, [1.0, 0.0, 186.0], byte_color, geometry)
    column_geometry_color_extend(1.0, 72.0, [1.0, 0.0, 188.0], byte_color, geometry)
    column_geometry_color_extend(1.0, 2.0, [1.0, 0.0, 260.0], byte_color, geometry)
    column_geometry_color_extend(2.0, 1.0, [2.0, 0.0, 262.0], byte_color, geometry)
    column_geometry_color_extend(216.0, 1.0, [4.0, 0.0, 263.0], byte_color, geometry)
    column_geometry_color_extend(2.0, 1.0, [220.0, 0.0, 262.0], byte_color, geometry)
    column_geometry_color_extend(1.0, 2.0, [222.0, 0.0, 260.0], byte_color, geometry)
    column_geometry_color_extend(1.0, 72.0, [223.0, 0.0, 188.0], byte_color, geometry)
    column_geometry_color_extend(1.0, 2.0, [222.0, 0.0, 186.0], byte_color, geometry)
    column_geometry_color_extend(2.0, 1.0, [220.0, 0.0, 185.0], byte_color, geometry)
    column_geometry_color_extend(36.0, 1.0, [184.0, 0.0, 184.0], byte_color, geometry)
    column_geometry_color_extend(1.0, 24.0, [183.0, 0.0, 160.0], byte_color, geometry)
    column_geometry_color_extend(40.0, 1.0, [184.0, 0.0, 159.0], byte_color, geometry)
    column_geometry_color_extend(40.0, 1.0, [0.0, 0.0, 136.0], byte_color, geometry)
    column_geometry_color_extend(1.0, 24.0, [40.0, 0.0, 112.0], byte_color, geometry)
    column_geometry_color_extend(36.0, 1.0, [4.0, 0.0, 111.0], byte_color, geometry)
    column_geometry_color_extend(2.0, 1.0, [2.0, 0.0, 110.0], byte_color, geometry)
    column_geometry_color_extend(1.0, 2.0, [1.0, 0.0, 108.0], byte_color, geometry)
    column_geometry_color_extend(1.0, 88.0, [1.0, 0.0, 20.0], byte_color, geometry)
    column_geometry_color_extend(1.0, 2.0, [1.0, 0.0, 18.0], byte_color, geometry)
    column_geometry_color_extend(2.0, 1.0, [2.0, 0.0, 17.0], byte_color, geometry)
    column_geometry_color_extend(216.0, 1.0, [4.0, 0.0, 16.0], byte_color, geometry)
    column_geometry_color_extend(2.0, 1.0, [220.0, 0.0, 17.0], byte_color, geometry)
    column_geometry_color_extend(1.0, 2.0, [222.0, 0.0, 18.0], byte_color, geometry)
    column_geometry_color_extend(1.0, 88.0, [223.0, 0.0, 20.0], byte_color, geometry)
    column_geometry_color_extend(1.0, 2.0, [222.0, 0.0, 108.0], byte_color, geometry)
    column_geometry_color_extend(2.0, 1.0, [220.0, 0.0, 110.0], byte_color, geometry)
    column_geometry_color_extend(36.0, 1.0, [184.0, 0.0, 111.0], byte_color, geometry)
    column_geometry_color_extend(1.0, 24.0, [183.0, 0.0, 112.0], byte_color, geometry)
    column_geometry_color_extend(40.0, 1.0, [184.0, 0.0, 136.0], byte_color, geometry)
    squares = [[4.0, 188.0], [4.0, 259.0], [107.0, 259.0], [109.0, 229.0], [114.0, 229.0], [116.0, 259.0], [219.0, 259.0], [219.0, 188.0], [4.0, 107.0], [4.0, 68.0], [18.0, 66.0], [18.0, 61.0], [4.0, 59.0], [4.0, 20.0], [219.0, 20.0], [219.0, 59.0], [205.0, 61.0], [205.0, 66.0], [219.0, 68.0], [219.0, 107.0]]
    for square in squares:
            column_geometry_color_extend(1.0, 1.0, [square[0], 0.0, square[1]], byte_color, geometry)
    filename = ".".join([name, "json"])
    filename = "/".join(["../geometries", filename])
    with open(filename, "w") as f:
        f.write(json.dumps(geometry, cls=SyrupEncoder))
    return 

def make_white_stage(name):
    dir = "../things"
    filename = ".".join([name, "json"])
    filepath = "/".join([dir, filename])
    with open(filepath) as f:
        text = f.read()
    thing = json.loads(text)
    if array_in_string(thing.keys(), "children_names"):
            new_children_names = []
            for child_name in thing["children_names"]:
                        make_white_stage(child_name)
                        new_name = "_".join(["white", child_name])
                        new_children_names.append(new_name)
            thing["children_names"] = new_children_names
    if array_in_string(thing.keys(), "geometry_name"):
            geometry_name = thing["geometry_name"]
            filename = ".".join([geometry_name, "json"])
            filepath = "/".join(["../geometries", filename])
            with open(filepath) as f:
                text = f.read()
            geometry = json.loads(text)
            new_geometry = copy_vertices_color(geometry, [255.0, 255.0, 255.0, 255.0])
            new_text = json.dumps(new_geometry, cls=SyrupEncoder)
            new_name = "_".join(["white", geometry_name])
            filename = ".".join([new_name, "json"])
            filepath = "/".join(["../geometries", filename])
            with open(filepath, "w") as f:
                f.write(new_text)
            thing["geometry_name"] = new_name
    new_name = "_".join(["white", name])
    thing["name"] = new_name
    filename = ".".join([new_name, "json"])
    new_type = "".join(["White", thing["type"]])
    thing["type"] = new_type
    filepath = "/".join([dir, filename])
    text = json.dumps(thing, cls=SyrupEncoder)
    with open(filepath, "w") as f:
        f.write(text)
    return 

def set_thing_geometry_name():
    dir = "../things"
    names = os.listdir(dir)
    for name in names:
            filepath = "/".join([dir, name])
            if (os.path.isfile(filepath) and is_extension(name, "json")):
                        with open(filepath) as f:
                            text = f.read()
                        print json.dumps(["reading file", name], cls=SyrupEncoder)
                        thing = json.loads(text)
                        if array_in_string(thing.keys(), "geometry_names"):
                                        thing["geometry_name"] = thing["geometry_names"][0]
                        text = json.dumps(thing, cls=SyrupEncoder)
                        with open(filepath, "w") as f:
                            f.write(text)
    return 

def dot_geometry():
    byte_color = [236.0, 183.0, 152.0, 255.0]
    vertices = column_geometry_color(1.0, 1.0, [0.0, 0.0, 0.0], byte_color)
    filename = "/".join(["../geometries", "dot.json"])
    with open(filename, "w") as f:
        f.write(json.dumps(vertices, cls=SyrupEncoder))
    return 

def color_pink_number():
    filepath = "../geometries/pink_100.json"
    text = ""
    with open(filepath) as f:
        text = f.read()
    vertices = json.loads(text)
    new_vertices = copy_vertices_color(vertices, [236.0, 183.0, 219.0, 255.0])
    with open(filepath, "w") as f:
        f.write(text)
    return 

def test():
    test_eyes()
    return 

def run():
    make_white_stage("stage")
    return 

