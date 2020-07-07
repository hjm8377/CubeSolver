from Cube.Rotation import Rotation
from ColorDetector.ColorUtil import *
import copy

tmp_cube = [[['b', 'r', 'g'], ['b', 'y', 'y'], ['r', 'w', 'g']], [['w', 'r', 'y'], ['b', 'r', 'w'], ['w', 'y', 'w']], [['b', 'r', 'o'], ['g', 'g', 'r'], ['b', 'g', 'y']], [['y', 'o', 'r'], ['y', 'o', 'w'], ['g', 'b', 'b']], [['w', 'g', 'o'], ['o', 'b', 'w'], ['o', 'y', 'o']], [['r', 'o', 'r'], ['g', 'w', 'o'], ['g', 'b', 'y']]]
ex_cube = [[['r', 'b', 'o'], ['r', 'y', 'g'], ['b', 'r', 'g']], [['b', 'w', 'y'], ['o', 'r', 'b'], ['r', 'r', 'g']], [['y', 'o', 'b'], ['o', 'g', 'g'], ['w', 'y', 'y']], [['g', 'y', 'b'], ['g', 'o', 'b'], ['y', 'y', 'o']], [['w', 'g', 'w'], ['w', 'b', 'r'], ['r', 'y', 'o']], [['g', 'w', 'o'], ['b', 'w', 'w'], ['w', 'o', 'r']]]


def face_sort(cube):
    """cube 리스트를 리턴"""
    tmp_cube = copy.deepcopy(cube)
    tmp = [[[] for _ in range(3)] for _ in range(6)]

    for i in range(6):
        if tmp_cube[i][1][1] == 'y':
            tmp[0] = tmp_cube[i]
        elif tmp_cube[i][1][1] == 'w':
            tmp[5] = tmp_cube[i]
        elif tmp_cube[i][1][1] == 'r':
            tmp[1] = tmp_cube[i]
        elif tmp_cube[i][1][1] == 'g':
            tmp[2] = tmp_cube[i]
        elif tmp_cube[i][1][1] == 'o':
            tmp[3] = tmp_cube[i]
        else:
            tmp[4] = tmp_cube[i]

    return tmp

def filtering_cubearr(cube):
    """인자로 넘겨받은 cube는 면 정렬이 된 리스트"""
    r = Rotation()

    arr = list()
    for i in range(4):
        r.clockwise(cube[0])
        for j in range(4):
            r.clockwise(cube[1])
            for k in range(4):
                r.clockwise(cube[2])
                for l in range(4):
                    r.clockwise(cube[3])
                    for m in range(4):
                        r.clockwise(cube[4])
                        for n in range(4):
                            r.clockwise(cube[5])
                            tmp = copy.deepcopy(cube)
                            arr.append(tmp)

    def check_edge(cube_arr):
        edge_sum = [0 for _ in range(12)]
        for num in range(12):
            (block1, block2) = (edge[num])
            (a, b, c) = block1
            (d, e, f) = block2

            c1 = cube_arr[a][b][c]
            c2 = cube_arr[d][e][f]

            try:
                edge_sum[edge_flag[c1][c2]] += 1
            except KeyError:
                try:
                    edge_sum[edge_flag[c2][c1]] += 1
                except KeyError:
                    # print("error!")
                    return 1

        for num in range(12):
            if edge_sum[num] != 1:
                return 1

        return 0

    tmp_arr = list()

    for i in range(4096):
        # print(check_edge(arr[i]))
        if check_edge(arr[i]) == 0:
            tmp_arr.append(arr[i])

    return tmp_arr


def complete_cube(cube):
    """인자로 넘겨받은 cube는 edge조각으로 걸러진 리스트"""
    # print(len(cube))
    for l in range(len(cube)):
        print_planar(cube[l])
        tmp_sum = 0
        for num in range(len(corner)):
            (block1, block2, block3) = (corner[num])
            (a, b, c) = block1
            (d, e, f) = block2
            (g, h, i) = block3

            if compare_three_faces(cube[l][a][b][c], cube[l][d][e][f], cube[l][g][h][i]) is True:
                tmp_sum += 1
            else:
                break
        print(tmp_sum)
        if tmp_sum == 8:
            # print_planar(cube[l])
            return cube[l]

    return 1


r = Rotation()
cube = copy.deepcopy(ex_cube)

# print_planar(cube)

full = face_sort(ex_cube)

full = complete_cube(filtering_cubearr(full))

print(full)
