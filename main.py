from Cube.Cube import print_cube, draw_cube
from Cube.Rotation import Rotation
from ColorDetector import ColorDetection
from time import sleep
import Solver
import copy
import cv2
import serial
import multiprocessing
import numpy as np


def move_method(m, n):
    move = Rotation()
    move.move(m, n)


def solution_method(z):
    cube = copy.deepcopy(z)

    solver = Solver.CubeSolver(cube)
    sol, cube, step_sol = solver.solution()

    print_cube(cube)

    sol = solution_normalize(sol)

    try:
        ser = serial.Serial('COM2', 115200)
        sleep(2)
        ser.write(sol)
        sleep(1)
    except:
        exit("Can't Find Robot")


def solution_normalize(sol):
    for i in range(len(sol)):
        if len(sol[i]) == 1:
            sol[i] += 'o'

    s = ''.join(sol)
    s = s.replace("'", "p")
    s = s.replace("2", "t")

    return s


if __name__ == "__main__":
    c = ColorDetection.ColorDetection()
    # Serial = Serial.Serial()
    CUBE = [[[] for _ in range(3)] for _ in range(6)]
    k = 0

    cap = cv2.VideoCapture(0)  # 웹캠
    cap.set(3, 1280)
    cap.set(4, 720)  # 해상도 설정

    while True:
        try:
            ret, image = cap.read()  # image == 현재 화면
            # http://egloos.zum.com/eyes33/v/6091120
            # https://webnautes.tistory.com/1255
            blur = cv2.GaussianBlur(image, (3, 3), 0)
            hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
            c.draw_roi_box(image)  # 영상에 구역 그리기
            c.Roi(hsv)    # hsv 영상에 구역 나누기
        except cv2.error:
            image = np.zeros((720, 405, 3), np.uint8)

        for x in range(3):
            for y in range(3):
                ROI = c.roi[x][y]
                c.hue_value[x][y], c.s_value[x][y] = c.average_hs(ROI)

        c.print_color(image)
        cv2.putText(image, str(k), (50, 50), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0))

        # image resize
        image = cv2.resize(image, dsize=(720, 405), interpolation=cv2.INTER_AREA)
        planar = draw_cube(CUBE)
        final = cv2.hconcat([image, planar])

        cv2.imshow('Rubik\'s Color Detection', final)
        if cv2.waitKey(30) & 0xFF == 27:  # Esc 누르면 종료
            break
        elif cv2.waitKeyEx(30) & 0xFF == ord('q'):
            if k <= 6:
                CUBE[k] = copy.deepcopy(c.color)
                k += 1
                planar = draw_cube(CUBE)
                print(CUBE)

                if k == 6:
                    cap.release()

        if image[0][0][0] == 0:
            break

    processing = multiprocessing.Process(target=solution_method, args=(CUBE,))
    processing.start()
    processing.join()

    cv2.waitKey(0)
    # cap.release()
    cv2.destroyAllWindows()
