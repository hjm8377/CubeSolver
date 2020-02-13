from sys import exit
import cv2
import threading
import copy
from Cube.Cube import color_to_bgr

try:
    import sys
except ImportError as err:
    exit(err)


class ColorDetection:
    # 3*3 배열
    roi = [[0 for col in range(3)] for row in range(3)]
    hue_value = [[0 for _ in range(3)] for _ in range(3)]
    s_value = [[0 for _ in range(3)] for _ in range(3)]
    color = [['w', 'w', 'w'],
             ['w', 'w', 'w'],
             ['w', 'w', 'w']]

    def Roi(self, frame):
        # roi 영역 추출
        for i in range(0, 3):
            for j in range(0, 3):
                self.roi[i][j] = frame[250 + i * 100: 300 + i * 100, 500 + j * 100: 550 + j * 100]

    def draw_roi_box(self, frame):
        # roi 영역 박스 그리기
        for i in range(0, 3):
            for j in range(0, 3):
                cv2.rectangle(frame, (500 + j * 100, 250 + i * 100), (550 + j * 100, 300 + i * 100), (0, 0, 0), 3)

    def average_hs(self, hsv_roi):
        red_high = 0
        red_low = 0

        h = 0
        s = 0
        num = 0

        for i in range(len(hsv_roi)):
            if i % 10 == 0:
                for j in range(len(hsv_roi[i])):
                    if j % 10 == 0 or j % 5 == 0:
                        chunk = hsv_roi[i][j]
                        if 150 < chunk[0] <= 180:
                            num += 1
                            h += 2
                            s += chunk[1]
                        else:
                            num += 1
                            h += chunk[0]
                            s += chunk[1]

        h /= num
        s /= num

        return int(h), int(s)

    def print_color(self, frame):

        def color_to_rgb(name):
            color = {
                'r': (204, 0, 0),
                'o': (255, 128, 0),
                'b': (0, 0, 255),
                'g': (0, 204, 0),
                'w': (255, 255, 255),
                'y': (255, 204, 0)
            }

            return color[name]

        for i in range(3):
            for j in range(3):
                if 100 < self.hue_value[i][j] <= 140 and self.s_value[i][j] > 70:
                    cv2.rectangle(frame, (500 + j * 100, 250 + i * 100), (550 + j * 100, 300 + i * 100), color_to_rgb('b'), -1)
                    cv2.putText(frame, "B", (525 + j * 100, 275 + i * 100), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0))
                    self.color[i][j] = 'b'
                elif (18 < self.hue_value[i][j] <= 40) and self.s_value[i][j] > 70:
                    cv2.rectangle(frame, (500 + j * 100, 250 + i * 100), (550 + j * 100, 300 + i * 100), color_to_rgb('y'), -1)
                    cv2.putText(frame, "Y", (525 + j * 100, 275 + i * 100), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0))
                    self.color[i][j] = 'y'
                elif 40 < self.hue_value[i][j] <= 100 and self.s_value[i][j] > 70:
                    cv2.rectangle(frame, (500 + j * 100, 250 + i * 100), (550 + j * 100, 300 + i * 100), color_to_rgb('g'), -1)
                    cv2.putText(frame, "G", (525 + j * 100, 275 + i * 100), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0))
                    self.color[i][j] = 'g'
                elif (150 < self.hue_value[i][j] <= 180 or 0 <= self.hue_value[i][j] <= 2) and self.s_value[i][j] > 70:
                    cv2.rectangle(frame, (500 + j * 100, 250 + i * 100), (550 + j * 100, 300 + i * 100), color_to_rgb('r'), -1)
                    cv2.putText(frame, "R", (525 + j * 100, 275 + i * 100), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0))
                    self.color[i][j] = 'r'
                elif 2 < self.hue_value[i][j] <= 18 and self.s_value[i][j] > 70:
                    cv2.rectangle(frame, (500 + j * 100, 250 + i * 100), (550 + j * 100, 300 + i * 100), color_to_rgb('o'), -1)
                    cv2.putText(frame, "O", (525 + j * 100, 275 + i * 100), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0))
                    self.color[i][j] = 'o'
                if 0 <= self.s_value[i][j] <= 70:
                    cv2.rectangle(frame, (500 + j * 100, 250 + i * 100), (550 + j * 100, 300 + i * 100), color_to_rgb('w'), -1)
                    cv2.putText(frame, "W", (525 + j * 100, 275 + i * 100), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0))
                    self.color[i][j] = 'w'

    def print_HSV(self, frame):
        for i in range(3):
            for j in range(3):
                cv2.putText(frame, str(self.hue_value[i][j]), (525 + j * 100, 275 + i * 100),
                            cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0))


if __name__ == "__main__":
    c = ColorDetection()
    CUBE = [[[] for _ in range(3)] for _ in range(6)]
    k = 0

    cap = cv2.VideoCapture(0)  # 웹캠
    cap.set(3, 1080)
    cap.set(4, 720)  # 해상도 설정

    while cap.isOpened():
        ret, image = cap.read()  # image == 현재 화면
        image = cv2.GaussianBlur(image, (3, 3), 0)
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        h, _, _ = cv2.split(hsv)

        c.draw_roi_box(image)  # 영상에 구역 그리기
        c.Roi(hsv)    # hsv 영상에 구역 나누기

        for x in range(3):
            for y in range(3):
                ROI = c.roi[x][y]
                c.hue_value[x][y], c.s_value[x][y] = c.average_hs(ROI)

        c.print_HSV(image)
        # c.print_color(image)
        cv2.putText(image, str(k), (50, 50), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0))

        # image resize
        image = cv2.resize(image, dsize=(720, 405), interpolation=cv2.INTER_AREA)

        cv2.imshow('Rubik\'s Color Detection', image)
        # cv2.imshow('Color Detection HSV', h)

        if cv2.waitKey(1) == 27:  # Esc 누르면 종료
            break
        elif cv2.waitKey(100) == ord('q'):
            if k < 6:
                CUBE[k] = copy.deepcopy(c.color)
                k += 1
                print(CUBE)
            if k > 6:
                break

    cap.release()
    cv2.destroyAllWindows()
