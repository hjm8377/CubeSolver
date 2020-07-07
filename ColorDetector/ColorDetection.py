import cv2
import numpy as np
from collections import Counter
import itertools
from copy import deepcopy
from Cube import Rotation
from ColorDetector.ColorUtil import *


class ColorDetection:

    def __init__(self):
        self.h_roi = [[0 for col in range(3)] for row in range(3)]
        self.v_roi = [[0 for col1 in range(3)] for row1 in range(3)]
        self.s_roi = [[0 for col2 in range(3)] for row2 in range(3)]
        self.color = [['w', 'w', 'w'],
                      ['w', 'w', 'w'],
                      ['w', 'w', 'w']]

    def h_Roi(self, frame):
        # roi 영역 추출
        for i in range(0, 3):
            for j in range(0, 3):
                self.h_roi[i][j] = frame[250 + i * 100: 300 + i * 100, 500 + j * 100: 550 + j * 100]

    def v_Roi(self, frame):
        # roi 영역 추출
        for i in range(0, 3):
            for j in range(0, 3):
                self.v_roi[i][j] = frame[250 + i * 100: 300 + i * 100, 500 + j * 100: 550 + j * 100]

    def s_Roi(self, frame):
        # roi 영역 추출
        for i in range(0, 3):
            for j in range(0, 3):
                self.s_roi[i][j] = frame[250 + i * 100: 300 + i * 100, 500 + j * 100: 550 + j * 100]

    def draw_roi_box(self, frame):
        # roi 영역 박스 그리기
        for i in range(0, 3):
            for j in range(0, 3):
                cv2.rectangle(frame, (500 + j * 100, 250 + i * 100), (550 + j * 100, 300 + i * 100), (0, 0, 0), 3)

    def color_detect(self, h_roi, v_roi, s_roi, p, m):
        dstv = cv2.inRange(v_roi, 0, 255)
        listfv = np.array(dstv).flatten()
        cntv = Counter(listfv)
        maxiv = cntv.most_common(1)

        dsts = cv2.inRange(s_roi, 0, 70)
        listfs = np.array(dsts).flatten()
        cnts = Counter(listfs)
        maxis = cnts.most_common(1)

        dst = cv2.inRange(h_roi, 0, 10)
        dst1 = cv2.inRange(h_roi, 170, 180)
        cv2.bitwise_or(dst, dst1, dst)
        listf = np.array(dst).flatten()
        cnt = Counter(listf)
        maxi = cnt.most_common(1)
        if (maxi[0][1] / 2500) * 100 > 90 and maxi[0][0] == 255:
            self.color[p][m] = 'r'
        elif maxiv[0][0] == 255 and maxis[0][0] == 255:
            self.color[p][m] = 'w'

        dst = cv2.inRange(h_roi, 9, 18)
        listf = list(itertools.chain.from_iterable(dst))
        cnt = Counter(listf)
        maxi = cnt.most_common(1)
        if (maxi[0][1] / 2500) * 100 > 90 and maxi[0][0] == 255 and maxis[0][0] != 255:
            self.color[p][m] = 'o'

        dst = cv2.inRange(h_roi, 18, 40)
        listf = list(itertools.chain.from_iterable(dst))
        cnt = Counter(listf)
        maxi = cnt.most_common(1)
        if (maxi[0][1] / 2500) * 100 > 90 and maxi[0][0] == 255 and maxis[0][0] != 255:
            self.color[p][m] = 'y'

        dst = cv2.inRange(h_roi, 40, 100)
        listf = list(itertools.chain.from_iterable(dst))
        cnt = Counter(listf)
        maxi = cnt.most_common(1)
        if (maxi[0][1] / 2500) * 100 > 90 and maxi[0][0] == 255 and maxis[0][0] != 255:
            self.color[p][m] = 'g'

        dst = cv2.inRange(h_roi, 100, 140)
        listf = list(itertools.chain.from_iterable(dst))
        cnt = Counter(listf)
        maxi = cnt.most_common(1)
        if (maxi[0][1] / 2500) * 100 > 90 and maxi[0][0] == 255 and maxis[0][0] != 255:
            self.color[p][m] = 'b'

    def color_to_rgb(self, name):
        color = {
            'r': (204, 0, 0),
            'o': (255, 128, 0),
            'b': (0, 0, 255),
            'g': (0, 204, 0),
            'w': (255, 255, 255),
            'y': (255, 204, 0)
        }

        return color[name]

    def print_color(self, frame):
        for i in range(3):
            for j in range(3):
                if self.color[i][j] == 'b':
                    cv2.rectangle(frame, (500 + j * 100, 250 + i * 100), (550 + j * 100, 300 + i * 100), self.color_to_rgb('b'), -1)
                    cv2.putText(frame, "B", (525 + j * 100, 275 + i * 100), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0))
                    self.color[i][j] = 'b'
                elif self.color[i][j] == 'y':
                    cv2.rectangle(frame, (500 + j * 100, 250 + i * 100), (550 + j * 100, 300 + i * 100), self.color_to_rgb('y'), -1)
                    cv2.putText(frame, "Y", (525 + j * 100, 275 + i * 100), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0))
                    self.color[i][j] = 'y'
                elif self.color[i][j] == 'g':
                    cv2.rectangle(frame, (500 + j * 100, 250 + i * 100), (550 + j * 100, 300 + i * 100), self.color_to_rgb('g'), -1)
                    cv2.putText(frame, "G", (525 + j * 100, 275 + i * 100), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0))
                    self.color[i][j] = 'g'
                elif self.color[i][j] == 'r':
                    cv2.rectangle(frame, (500 + j * 100, 250 + i * 100), (550 + j * 100, 300 + i * 100), self.color_to_rgb('r'), -1)
                    cv2.putText(frame, "R", (525 + j * 100, 275 + i * 100), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0))
                    self.color[i][j] = 'r'
                elif self.color[i][j] == 'o':
                    cv2.rectangle(frame, (500 + j * 100, 250 + i * 100), (550 + j * 100, 300 + i * 100), self.color_to_rgb('o'), -1)
                    cv2.putText(frame, "O", (525 + j * 100, 275 + i * 100), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0))
                    self.color[i][j] = 'o'
                elif self.color[i][j] == 'w':
                    cv2.rectangle(frame, (500 + j * 100, 250 + i * 100), (550 + j * 100, 300 + i * 100), self.color_to_rgb('w'), -1)
                    cv2.putText(frame, "W", (525 + j * 100, 275 + i * 100), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0))
                    self.color[i][j] = 'w'

    def face_sort(self, cube):
        """cube 리스트를 리턴"""
        tmp_cube = deepcopy(cube)
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

    def filtering_cubearr(self, cube):
        """인자로 넘겨받은 cube는 면 정렬이 된 리스트"""
        r = Rotation.Rotation()

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
                                tmp = deepcopy(cube)
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
            if check_edge(arr[i]) == 0:
                tmp_arr.append(arr[i])

        return tmp_arr

    def complete_cube(self, cube):
        """인자로 넘겨받은 cube는 edge조각으로 걸러진 리스트"""
        for l in range(len(cube)):
            tmp_sum = 0
            for num in range(len(corner)):
                (block1, block2, block3) = (corner[num])
                (a, b, c) = block1
                (d, e, f) = block2
                (g, h, i) = block3

                if compare_three_faces(cube[l][a][b][c], cube[l][d][e][f], cube[l][g][h][i]) is True:
                    tmp_sum += 1

            if tmp_sum == 8:
                # print_planar(cube[l])
                return cube[l]

        return 1

    def check_overlap(self, cube, face):
        """중복있으면 1리턴 아니면 0리턴"""
        r = Rotation.Rotation()
        for i in range(6):
            for j in range(4):
                if self.compare(face, cube[i]):
                    # print("중복입니다.")
                    return 1
                r.clockwise(face)

        return 0

    def del_face(self, cube, face_num):
        for i in range(3):
            cube[face_num][i] = deepcopy([])

    @staticmethod
    def compare(k1, k2):
        if k1[0] == [] or k2[0] == []:
            return False

        s = 0
        for i in range(3):
            for j in range(3):
                if k1[i][j] == k2[i][j]:
                    s = s + 1

        if s == 9:
            return True

        return False


if __name__ == "__main__":
    c = ColorDetection()
    CUBE = [[[] for _ in range(3)] for _ in range(6)]
    k = [0]

    cap = cv2.VideoCapture(0)  # 웹캠
    cap.set(3, 1080)
    cap.set(4, 720)  # 해상도 설정

    while cap.isOpened():
        ret, image = cap.read()  # image == 현재 화면
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)

        c.draw_roi_box(image)
        c.h_Roi(h)
        c.s_Roi(s)
        c.v_Roi(v)

        for i in range(3):
            for j in range(3):
                c.color_detect(c.h_roi[i][j], c.v_roi[i][j], c.s_roi[i][j], i, j)

        c.print_color(image)

        # image resize
        image = cv2.resize(image, dsize=(720, 405), interpolation=cv2.INTER_AREA)

        cv2.imshow('Rubik\'s Color Detection', image)

        if cv2.waitKey(1) == 27:  # Esc 누르면 종료
            break

    cap.release()
    cv2.destroyAllWindows()
