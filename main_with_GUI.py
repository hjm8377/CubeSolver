from Cube.Cube import print_cube, draw_cube
from ColorDetector import ColorDetection
import Solver
import copy

from tkinter import *
from tkinter import messagebox
import PIL.Image
import PIL.ImageTk
import cv2

import multiprocessing
import numpy as np

from Graphic.cubie import *

from ColorDetector.ColorUtil import *

solution = []
full = [[[] for _ in range(3)] for _ in range(6)]

def init(window):

    window.iconbitmap(default="src/cube.ico")
    frame_button = Frame(window, bg="white")
    frame_button.pack(side="bottom")

    btn_start = Button(frame_button, width=10, text="solving", fg="green", bg="white", relief="raised", overrelief="flat",
                       command=lambda: start_(window, btn_start))
    btn_start.grid(row=0, column=0)

    # btn_free = Button(frame_button, width=10, text="free mode", fg="blue", bg="white", relief="raised", overrelief="flat",
                      # command=lambda: cube_graphic())
    # btn_free.grid(row=0, column=1)

    btn_exit = Button(frame_button, width=10, text="exit", fg="red", bg="white", relief="raised", overrelief="flat",
                      command=exit)
    btn_exit.grid(row=0, column=2, sticky="w")

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

    def show_frame():
        try:
            ret, image = cap.read()
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            h, s, v = cv2.split(hsv)

            c.draw_roi_box(image)
            c.h_Roi(h)
            c.s_Roi(s)
            c.v_Roi(v)
        except cv2.error:
            image = np.zeros((720, 405, 3), np.uint8)

        for i in range(3):
            for j in range(3):
                c.color_detect(c.h_roi[i][j], c.v_roi[i][j], c.s_roi[i][j], i, j)

        c.print_color(image)
        cv2.putText(image, str(k), (50, 50), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0))

        # image resize
        image = cv2.resize(image, dsize=(750, 405), interpolation=cv2.INTER_AREA)
        planar = draw_cube(CUBE)
        final = cv2.hconcat([image, planar])

        img = PIL.Image.fromarray(final)
        imgtk = PIL.ImageTk.PhotoImage(image=img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        lmain.after(10, show_frame)

    def prev(num, cubie):
        if num[0] <= 0:
            messagebox.showinfo(title="Caution", message="인식된 면이 없습니다!")
        if num[0] > 0:
            num[0] -= 1
            c.del_face(cubie, num[0])
            # print(cubie)

    def next_(num, cubie, detector):
        global full
        if num[0] < 6:
            if c.check_overlap(cubie, detector.color) == 0:
                cubie[num[0]] = copy.deepcopy(detector.color)
                num[0] += 1
            elif c.check_overlap(cubie, detector.color) == 1:
                messagebox.showinfo(title="Caution", message="중복 인식된 면 입니다!")
            # print(cubie)
        if num[0] == 6:
            cap.release()
            full = copy.deepcopy(c.face_sort(CUBE))
            full = copy.deepcopy(c.complete_cube(c.filtering_cubearr(full)))
            steps = solution_method(full)
            btn_prev["state"] = DISABLED
            num[0] += 1
        if num[0] == 7:
            btn_next.config(text="완료", command=lambda: exit_graph(k, solution, steps))
        if num[0] > 7:
            top.destroy()

    def exit_(num):
        num[0] = 0
        btn["state"] = NORMAL
        top.destroy()

    def exit_graph(num, sol, steps):
        procs = []
        num[0] = 0
        btn["state"] = NORMAL
        # print(sol)

        # print(full)
        CUBIE = Cubie(full, 'solving', sol, steps)
        proc_graph = multiprocessing.Process(target=CUBIE.run())
        procs.append(proc_graph)
        proc_graph.start()
        proc_graph.join()

    top = Toplevel(window)
    top.title("Color Detector")
    top.iconbitmap(default="src/cube.ico")

    top.protocol("WM_DELETE_WINDOW", lambda: exit_(k))
    top.bind("<Destroy>")

    frame_image = Frame(top)
    frame_image.grid(row=0, column=0, padx=10, pady=2)

    frame_btn = Frame(top, bg="white")
    frame_btn.grid(row=1)

    btn_prev = Button(frame_btn, width=10, text="del", fg="blue", bg="white", relief="raised", overrelief="flat",
                      command=lambda: prev(k, CUBE))
    btn_prev.grid(row=0, column=0)

    btn_next = Button(frame_btn, width=10, text="next", fg="green", bg="white", relief="raised", overrelief="flat",
                      command=lambda: next_(k, CUBE, c))
    btn_next.grid(row=0, column=1)
    # top.bind("<Key>", lambda: next_(k, CUBE, c))

    btn_exit = Button(frame_btn, width=10, text="exit", fg="red", bg="white", relief="raised", overrelief="flat",
                      command=lambda: exit_(k))
    btn_exit.grid(row=0, column=2, sticky="w")

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
        # print(CUBE)
    else:
        return


def solution_method(z):
    global solution
    cube = copy.deepcopy(z)

    solver = Solver.CubeSolver(cube)
    solution, cube, step_sol = solver.solution()

    # print_cube(cube)
    print(solution)

    return step_sol


def cube_graphic():
    c = Cubie()
    c.run()


if __name__ == "__main__":
    root = Tk()

    root.config(background="white")
    root.title("Rubik's cube solver")

    init(root)

    root.mainloop()
