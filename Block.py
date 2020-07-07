"""
find_edge
:param : cube, color1, color2
:return : color 1 기준 엣지 조각 위치
          { ex. DF, FR }

find_corner
:param : cube, color1, color2, color3
:return : 코너조각 위치
          { 기준 없이
            DFL, DFR, BDL, BDR, BRU, BLU, FLU, FRU 중 하나 반환
          }
"""

"""
엣지 조각 위치
001-401     010-101     012-301     021-201
110-412     112-210     121-510     212-310
221-501     312-410     321-512     421-521
"""


def find_edge(cube, c1, c2):
    if cube[0][0][1] == c1 or cube[4][0][1] == c1:
        if cube[4][0][1] == c2 or cube[0][0][1] == c2:
            if c1 == cube[0][0][1]:
                return 'UB'
            else:
                return 'BU'

    if cube[0][1][0] == c1 or cube[1][0][1] == c1:
        if cube[1][0][1] == c2 or cube[0][1][0] == c2:
            if c1 == cube[0][1][0]:
                return 'UL'
            else:
                return 'LU'

    if cube[0][1][2] == c1 or cube[3][0][1] == c1:
        if cube[3][0][1] == c2 or cube[0][1][2] == c2:
            if c1 == cube[0][1][2]:
                return 'UR'
            else:
                return 'RU'

    if cube[0][2][1] == c1 or cube[2][0][1] == c1:
        if cube[2][0][1] == c2 or cube[0][2][1] == c2:
            if c1 == cube[0][2][1]:
                return 'UF'
            else:
                return 'FU'

    if cube[1][1][0] == c1 or cube[4][1][2] == c1:
        if cube[4][1][2] == c2 or cube[1][1][0] == c2:
            if c1 == cube[1][1][0]:
                return 'LB'
            else:
                return 'BL'

    if cube[1][1][2] == c1 or cube[2][1][0] == c1:
        if cube[2][1][0] == c2 or cube[1][1][2] == c2:
            if c1 == cube[1][1][2]:
                return 'LF'
            else:
                return 'FL'

    if cube[1][2][1] == c1 or cube[5][1][0] == c1:
        if cube[5][1][0] == c2 or cube[1][2][1] == c2:
            if c1 == cube[1][2][1]:
                return 'LD'
            else:
                return 'DL'

    if cube[2][1][2] == c1 or cube[3][1][0] == c1:
        if cube[3][1][0] == c2 or cube[2][1][2] == c2:
            if c1 == cube[2][1][2]:
                return 'FR'
            else:
                return 'RF'

    if cube[2][2][1] == c1 or cube[5][0][1] == c1:
        if cube[5][0][1] == c2 or cube[2][2][1] == c2:
            if c1 == cube[2][2][1]:
                return 'FD'
            else:
                return 'DF'

    if cube[3][1][2] == c1 or cube[4][1][0] == c1:
        if cube[4][1][0] == c2 or cube[3][1][2] == c2:
            if c1 == cube[3][1][2]:
                return 'RB'
            else:
                return 'BR'

    if cube[3][2][1] == c1 or cube[5][1][2] == c1:
        if cube[5][1][2] == c2 or cube[3][2][1] == c2:
            if c1 == cube[3][2][1]:
                return 'RD'
            else:
                return 'DR'

    if cube[4][2][1] == c1 or cube[5][2][1] == c1:
        if cube[5][2][1] == c2 or cube[4][2][1] == c2:
            if c1 == cube[4][2][1]:
                return 'BD'
            else:
                return 'DB'


def color_face(arr, i):
    if i == 0:
        return arr[0]
    elif i == 1:
        return arr[1]
    else:
        exit(120)


def find_corner(cube, c1, c2, c3):
    # DFL, DFR, BDL, BDR, BRU, BLU, FLU, FRU

    # BLU
    if cube[0][0][0] == c1 or cube[1][0][0] == c1 or cube[4][0][2] == c1:
        if cube[0][0][0] == c2 or cube[1][0][0] == c2 or cube[4][0][2] == c2:
            if cube[0][0][0] == c3 or cube[1][0][0] == c3 or cube[4][0][2] == c3:
                return 'BLU'

    # BRU
    if cube[0][0][2] == c1 or cube[4][0][0] == c1 or cube[3][0][2] == c1:
        if cube[0][0][2] == c2 or cube[4][0][0] == c2 or cube[3][0][2] == c2:
            if cube[0][0][2] == c3 or cube[4][0][0] == c3 or cube[3][0][2] == c3:
                return 'BRU'

    # FLU
    if cube[0][2][0] == c1 or cube[2][0][0] == c1 or cube[1][0][2] == c1:
        if cube[0][2][0] == c2 or cube[2][0][0] == c2 or cube[1][0][2] == c2:
            if cube[0][2][0] == c3 or cube[2][0][0] == c3 or cube[1][0][2] == c3:
                return 'FLU'

    # FRU
    if cube[0][2][2] == c1 or cube[3][0][0] == c1 or cube[2][0][2] == c1:
        if cube[0][2][2] == c2 or cube[3][0][0] == c2 or cube[2][0][2] == c2:
            if cube[0][2][2] == c3 or cube[3][0][0] == c3 or cube[2][0][2] == c3:
                return 'FRU'

    # DFL
    if cube[2][2][0] == c1 or cube[5][0][0] == c1 or cube[1][2][2] == c1:
        if cube[2][2][0] == c2 or cube[5][0][0] == c2 or cube[1][2][2] == c2:
            if cube[2][2][0] == c3 or cube[5][0][0] == c3 or cube[1][2][2] == c3:
                return 'DFL'

    # DFR
    if cube[2][2][2] == c1 or cube[3][2][0] == c1 or cube[5][0][2] == c1:
        if cube[2][2][2] == c2 or cube[3][2][0] == c2 or cube[5][0][2] == c2:
            if cube[2][2][2] == c3 or cube[3][2][0] == c3 or cube[5][0][2] == c3:
                return 'DFR'

    # BDL
    if cube[1][2][0] == c1 or cube[5][2][0] == c1 or cube[4][2][2] == c1:
        if cube[1][2][0] == c2 or cube[5][2][0] == c2 or cube[4][2][2] == c2:
            if cube[1][2][0] == c3 or cube[5][2][0] == c3 or cube[4][2][2] == c3:
                return 'BDL'

    # BDR 322 420 522
    if cube[3][2][2] == c1 or cube[4][2][0] == c1 or cube[5][2][2] == c1:
        if cube[3][2][2] == c2 or cube[4][2][0] == c2 or cube[5][2][2] == c2:
            if cube[3][2][2] == c3 or cube[4][2][0] == c3 or cube[5][2][2] == c3:
                return 'BDR'


def FRU_w(cube):
    if cube[2][0][2] == 'w':
        return 'F'
    elif cube[3][0][0] == 'w':
        return 'R'
    elif cube[0][2][2] == 'w':
        return 'U'
    else:
        exit('FRU_error')
