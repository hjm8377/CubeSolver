corner = (((0, 2, 0), (2, 0, 0), (1, 0, 2)),
          ((2, 0, 2), (0, 2, 2), (3, 0, 0)),
          ((2, 2, 0), (1, 2, 2), (5, 0, 0)),
          ((2, 2, 2), (3, 2, 0), (5, 0, 2)),
          ((0, 0, 0), (1, 0, 0), (4, 0, 2)),
          ((0, 0, 2), (3, 0, 2), (4, 0, 0)),
          ((5, 2, 0), (1, 2, 0), (4, 2, 2)),
          ((5, 2, 2), (3, 2, 2), (4, 2, 0)))

edge = (((0, 0, 1), (4, 0, 1)),
        ((0, 1, 0), (1, 0, 1)),
        ((0, 1, 2), (3, 0, 1)),
        ((0, 2, 1), (2, 0, 1)),
        ((1, 1, 0), (4, 1, 2)),
        ((1, 1, 2), (2, 1, 0)),
        ((1, 2, 1), (5, 1, 0)),
        ((2, 1, 2), (3, 1, 0)),
        ((2, 2, 1), (5, 0, 1)),
        ((3, 1, 2), (4, 1, 0)),
        ((3, 2, 1), (5, 1, 2)),
        ((4, 2, 1), (5, 2, 1)))

edge_flag = {
    'y': {
        'r': 0,
        'g': 1,
        'o': 2,
        'b': 3
    },
    'r': {
        'g': 4,
        'b': 5
    },
    'o': {
        'g': 6,
        'b': 7
    },
    'w': {
            'r': 8,
            'g': 9,
            'o': 10,
            'b': 11
    }
}


def color_to_num(c):
    """색 문자를 넘겨주면 해당색을 숫자로 변환"""
    if c == 'y':
        return 0
    elif c == 'r':
        return 5
    elif c == 'g':
        return 10
    elif c == 'o':
        return 7
    elif c == 'b':
        return 12
    elif c == 'w':
        return 2


def compare_three_faces(c1, c2, c3):
    """세가지 색을 넘겨 받아서 인접한 면의 색으로만 이루어져 있는지를 판단해줌"""
    a1 = color_to_num(c1)
    a2 = color_to_num(c2)
    a3 = color_to_num(c3)

    if abs(a1 - a2) == 2 or abs(a2 - a3) == 2 or abs(a3 - a1) == 2:
        return False
    elif abs(a1 - a2) == 0 or abs(a2 - a3) == 0 or abs(a3 - a1) == 0:
        return False
    else:
        return True


def print_planar(cube):
    if cube is None:
        raise Exception("CubeError")

    for j in range(3):
        a, b, c = cube[0][j][0], cube[0][j][1], cube[0][j][2]
        print("     ", end="    ")
        print(a, b, c)
    print("")

    for i in range(3):
        for j in range(4):
            a, b, c = cube[j + 1][i][0], cube[j + 1][i][1], cube[j + 1][i][2]
            print(a, b, c, end="    ")
        print("")

    print("")
    for j in range(3):
        a, b, c = cube[5][j][0], cube[5][j][1], cube[5][j][2]
        print("     ", end="    ")
        print(a, b, c)
    print("")
