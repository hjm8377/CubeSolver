from Cube.Cube import print_cube, draw_cube
from ColorDetector import ColorDetection
import Solver
import copy

from tkinter import *
from tkinter import messagebox
import PIL.Image
import PIL.ImageTk
import cv2
from time import sleep
import serial
import multiprocessing
import numpy as np

COM = 'COM4'


def init(window):
    window.iconbitmap(default="src/cube.ico")
    frame_button = Frame(window, bg="white")
    frame_button.pack(side="bottom")

    btn_start = Button(frame_button, width=10, text="start", fg="green", bg="white", relief="raised", overrelief="flat",
                       command=lambda: start_(window, btn_start))
    btn_start.grid(row=0, column=0)

    btn_exit = Button(frame_button, width=10, text="exit", fg="red", bg="white", relief="raised", overrelief="flat",
                      command=exit)
    btn_exit.grid(row=0, column=1, sticky="w")

    label_text = "Rubik's cube solver"
    label = Label(window, text=label_text, bg="white")
    label.img = PhotoImage(file='src/cube_icon.gif').subsample(7)
    label.config(image=label.img, compound='left')
    label.config(font=('namun_gothic', 18, 'bold'))
    label.pack(side="top")


def start_(window, btn):
    btn["state"] = DISABLED

    c = ColorDetection.ColorDetection()
    CUBE = [[[] for _ in range(3)] for _ in range(6)]
    k = [0]

    try:
        ser = serial.Serial(port=COM, baudrate=9600)
        sleep(2)
        ser.write('S'.encode())
        sleep(1)
    except:
        messagebox.showwarning("Error", "Can't Find Robot!")
        # exit("Can't Find Robot")

    def show_frame():
        try:
            ret, frame = cap.read()
            blur = cv2.GaussianBlur(frame, (3, 3), 0)
            hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            c.draw_roi_box(image)
            c.Roi(hsv)
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

        img = PIL.Image.fromarray(final)
        imgtk = PIL.ImageTk.PhotoImage(image=img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        lmain.after(10, show_frame)

    def next_(num, cubie, detector):
        if num[0] < 6:
            cubie[num[0]] = copy.deepcopy(detector.color)
            num[0] += 1
            print(cubie)
            try:
                ser = serial.Serial(port=COM, baudrate=9600)
                sleep(2)
                ser.write('N'.encode())
                sleep(1)
            except:
                messagebox.showwarning("Error", "Can't Find Robot!")
                # exit("Can't Find Robot")
        if num[0] == 6:
            cap.release()
            btn_next.config(text="완료", command=lambda: exit_(k))
            processing = multiprocessing.Process(target=solution_method, args=(CUBE,))
            processing.start()
            processing.join()
        if num[0] > 6:
            top.destroy()

    def exit_(num):
        num[0] = 0
        top.destroy()
        btn["state"] = NORMAL

    top = Toplevel(window)
    top.title("Color Detector")
    top.iconbitmap(default="src/cube.ico")

    top.protocol("WM_DELETE_WINDOW", lambda: exit_(k))
    top.bind("<Destroy>")

    frame_image = Frame(top)
    frame_image.grid(row=0, column=0, padx=10, pady=2)

    frame_btn = Frame(top, bg="white")
    frame_btn.grid(row=1)

    btn_next = Button(frame_btn, width=10, text="next", fg="green", bg="white", relief="raised", overrelief="flat", command=lambda: next_(k, CUBE, c))
    btn_next.grid(row=0, column=0)
    # top.bind("<Key>", lambda: next_(k, CUBE, c))

    btn_exit = Button(frame_btn, width=10, text="exit", fg="red", bg="white", relief="raised", overrelief="flat", command=lambda: exit_(k))
    btn_exit.grid(row=0, column=1, sticky="w")

    lmain = Label(frame_image)
    lmain.grid(row=0, column=0)

    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)

    show_frame()
    top.mainloop()


def key(k, CUBE, c):
    if k <= 6:
        CUBE[k] = copy.deepcopy(c.color)
        k += 1
        print(CUBE)
    else:
        return


def solution_method(z):
    cube = copy.deepcopy(z)

    solver = Solver.CubeSolver(cube)
    sol, cube, step_sol = solver.solution()

    print_cube(cube)

    sol = solution_normalize(sol)
    print(sol)

    try:
        ser = serial.Serial(port=COM, baudrate=9600)
        sleep(2)
        ser.write(sol.encode())
        sleep(1)
    except:
        messagebox.showwarning("Error", "Can't Find Robot!")
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
    root = Tk()

    root.config(background="white")
    root.title("Rubik's cube solver")
    init(root)

    root.mainloop()
