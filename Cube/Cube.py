import cv2
import copy
import numpy as np


def print_cube(arr):
    for i in range(6):
        for x, y, z in arr[i]:
            print(x, y, z)
        print('\n')


def draw_cube(arr):
    # 빈화면
    padding = 10
    width = 520
    height = 405
    bpp = 3

    img = np.zeros((height, width, bpp), np.uint8)

    x, y = 120 + padding, 30
    draw_square(img, x, y, arr[0])

    for i in range(4):
        x, y = 30 + i * 90 + padding * i, 120 + padding
        draw_square(img, x, y, arr[i + 1])

    x, y = 120 + padding, 210 + padding * 2
    draw_square(img, x, y, arr[5])

    return img


def draw_square(img, x, y, color):
    for i in range(3):
        for j in range(3):
            if color == [[], [], []]:
                pass
            else:
                cv2.rectangle(img, (x + j*30, y + i*30), (x + j*30 + 30, y + i*30 + 30), color_to_bgr(color[i][j]), -1)


def color_to_bgr(name):
    color = {
        'r': (204, 0, 0),
        'o': (255, 128, 0),
        'b': (0, 0, 255),
        'g': (0, 204, 0),
        'w': (255, 255, 255),
        'y': (255, 204, 0)
    }

    return color[name]


def solution_smoother(sol):
    for _ in range(10):
        for i in range(len(sol) - 1):
            a = [[0, 0], [0, 0]]

            try:
                a[0][0] = ord(sol[i + 1][0])
            except IndexError:
                break

            try:
                a[0][0] = ord(sol[i][0])
                a[0][1] = ord(sol[i][1])
            except IndexError:
                a[0][1] = ord(sol[i][0])
                a[0][1] = 0

            try:
                a[1][0] = ord(sol[i + 1][0])
                a[1][1] = ord(sol[i + 1][1])
            except IndexError:
                a[1][0] = ord(sol[i + 1][0])
                a[1][1] = 0

            # U', U
            if a[0][1] != ord('2'):
                # ex) U, U -> U2 or U', U' -> U2
                if a[0][0] == a[1][0] and a[0][1] == a[1][1]:
                    c = a[0][0]
                    del sol[i]
                    sol[i] = chr(c) + '2'
                # ex) U, U' / U', U / U, U2 /  U', U2
                elif a[0][0] == a[1][0] and a[0][1] != a[1][1]:
                    # ex) U, U' / U', U -> del
                    if (a[0][1] == ord("'") and a[1][1] == 0) or (a[0][1] == 0 and a[1][1] == ord("'")):
                        del sol[i]
                        del sol[i]
                    # ex) U, U2 -> U'
                    elif a[0][1] == 0 and a[1][1] == ord('2'):
                        c = a[0][0]
                        del sol[i]
                        sol[i] = chr(c) + "'"
                    # ex) U', U2 -> U
                    elif a[0][1] == ord("'") and a[1][1] == ord('2'):
                        c = a[0][0]
                        del sol[i]
                        sol[i] = chr(c)
                else:
                    pass

            # U2, U
            elif a[0][1] == ord('2') or a[1][1] == ord('2'):
                # ex) U2, U2  -> del
                if a[0][0] == a[1][0] and a[0][1] == a[1][1]:
                    c = a[0][0]
                    del sol[i]
                    del sol[i]
                # ex) U2, U / U2, U'
                elif a[0][0] == a[1][0] and a[0][1] != a[1][1]:
                    # ex) U2, U - > U'
                    if a[0][1] == ord('2') and a[1][1] == 0:
                        c = a[0][0]
                        del sol[i]
                        sol[i] = chr(c) + "'"
                    # ex) U2, U' -> U
                    elif a[0][1] == ord('2') and a[1][1] == ord("'"):
                        c = a[0][0]
                        del sol[i]
                        sol[i] = chr(c)
                    else:
                        pass

            else:
                pass

    return sol


# solving example
# ["F'", "U'", 'F',
# 'Y', 'R', 'U', "R'", "U'", "F'", "U'", 'F',
# 'Y', 'R', 'U', "R'", "U'", "F'", "U'", 'F',
# 'Y', 'R', 'U', "R'", "U'", "F'", "U'", 'F', 'Y']
def solution_minimize(sol):

    s = ''.join(sol)
    s = s.split('Y')

    s[1] = s[1].replace("L", "f").replace("R", "b").replace("F", "r").replace("B", "l")
    s[1] = s[1].upper()

    s[2] = s[2].replace("L", "r").replace("R", "l").replace("F", "b").replace("B", "f")
    s[2] = s[2].upper()

    s[3] = s[3].replace("L", "b").replace("R", "f").replace("F", "l").replace("B", "R")
    s[3] = s[3].upper()

    s = string_to_solution(s)

    return s


def string_to_solution(string):
    final = []

    for i in range(4):
        tmp_sol = list(string[i])
        for j in range(len(tmp_sol) - 1):
            if tmp_sol[j] is "'" or tmp_sol[j] is "2":
                if j is (len(tmp_sol) - 2):
                    final.append(tmp_sol[j + 1])
                else:
                    pass
            else:
                if tmp_sol[j + 1] is "'":
                    final.append(tmp_sol[j] + "'")
                elif tmp_sol[j + 1] is "2":
                    final.append(tmp_sol[j] + "2")
                else:
                    if j is (len(tmp_sol) - 2):
                        final.append(tmp_sol[j])
                        final.append(tmp_sol[j + 1])
                    else:
                        final.append(tmp_sol[j])
    return final

