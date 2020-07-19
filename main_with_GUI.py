from Cube.Cube import draw_cube
from ColorDetector import ColorDetection
import Solver

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import PIL.Image
import PIL.ImageTk
import cv2

import multiprocessing
import numpy as np

from Graphic.cubie import *

from configparser import ConfigParser
from ini import create_config

from ini.Language import *
import webbrowser

solution = []
full = [[[] for _ in range(3)] for _ in range(6)]
inifile = './ini/setting.ini'

if not inifile:
    create_config.run()

parser = ConfigParser()
parser.read(inifile)

setting_speed = parser.getint('settings', 'rotation_speed')
rotation_speed = abs(setting_speed - 99)
language = parser.get('settings', 'language')
firstlang = parser.get('settings', 'language')
print(setting_speed, rotation_speed, language)


def init(window):
    global language

    window.iconbitmap(default="src/cube.ico")
    frame_button = Frame(window, bg="white")
    frame_button.pack(side="bottom")

    def close():
        window.quit()
        window.destroy()

    def setwindow():
        global rotation_speed
        global language
        parser = ConfigParser()
        parser.read(inifile)

        def change_speed(self):
            global rotation_speed
            speed = speed_scale.get()
            parser.set('settings', 'rotation_speed', str(speed))
            speed -= 99
            rotation_speed = copy.deepcopy(abs(speed))

        def change_lang(eventObject):
            global language
            # print("combobox updated to ", lang_combo.get())
            language = lang_combo.get()
            parser.set('settings', 'language', language)

        def write_ini():
            global language
            global firstlang
            with open(inifile, 'w') as f:
                parser.write(f)

            if firstlang != language:
                messagebox.showwarning(Warning_[language], lang_warning[language])
                setting.destroy()
            else:
                setting.destroy()

        setting = Toplevel(window)
        setting.title(Setting[language])
        setting.geometry("400x150")
        setting.resizable(False, False)
        setting.grab_set()

        scale_frame = Frame(setting, width=400, height=30, relief="solid")
        scale_frame.pack()

        speed_label = Label(scale_frame, text=Rotation_Speed[language])
        speed_label.config(font=('namun_gothic', 9))
        speed_label.grid(row=0, column=0)

        var = IntVar()
        speed_scale = Scale(scale_frame, variable=var, orient="horizontal", showvalue=True, tickinterval=50,
                            to=100, length=300, resolution=5, command=change_speed)
        speed_scale.set(99 - rotation_speed)
        speed_scale.grid(row=0, column=1)

        lang_frame = Frame(setting, width=400, height=30, relief="solid")
        lang_frame.pack()

        lang_label = Label(lang_frame, text=Language[language])
        lang_label.config(font=('namun_gothic', 9))
        lang_label.pack(side='left', padx=0)

        lang_combo = ttk.Combobox(lang_frame, values=["English", "Korean"])
        if language == 'English':
            lang_combo.current(0)
        elif language == 'Korean':
            lang_combo.current(1)
        lang_combo.pack(side='left')
        lang_combo.bind("<<ComboboxSelected>>", change_lang)

        btnCancel = Button(setting, width=10, text=Cancel[language], relief="raised", overrelief="flat",
                           command=lambda: setting.destroy())
        btnCancel.pack(side='right')

        btnOK = Button(setting, width=10, text=Ok[language], relief="raised", overrelief="flat",
                       command=lambda: write_ini())
        btnOK.pack(side='right')

    def howwindow():
        how = Toplevel(window)
        how.title(How[language])
        how.geometry("300x120")
        how.resizable(False, False)
        how.grab_set()

        label = Label(how, text=howText[language])
        label.config(font=('namun_gothic', 9))
        label.pack(side='top', padx=0)

        btnOK = Button(how, width=10, text=Ok[language], relief="raised", overrelief="flat",
                       command=lambda: how.destroy())
        btnOK.pack(side='bottom')

    def Infowindow():
        def callback(url):
            webbrowser.open_new(url)

        info = Toplevel(window)
        info.title(Info[language])
        info.geometry("400x170")
        info.resizable(False, False)

        ilabel = Label(info)
        ilabel.img = PhotoImage(file='src/cube_icon.gif').subsample(15)
        ilabel.config(image=ilabel.img)
        ilabel.grid(row=0, column=0)

        nlabel = Label(info, text='Rubik\'s Cube Sover', font='namun_gothic')
        nlabel.grid(row=0, column=1)

        slabel = Label(info, text=sText[language] + '\n' + Made[language])
        slabel.config(font=('namun_gothic', 10))
        slabel.grid(row=1, column=1)

        frame_btn = Frame(info, width=400, height=20, pady=20)
        frame_btn.grid(row=2, column=1)

        btnh = Button(frame_btn, text=Homepage[language])
        btnh.pack(side='right')
        btnh.bind("<Button-1>", lambda e: callback("https://github.com/hjm8377/CubeSolver"))

    menubar = Menu(window)

    # 설정
    setmenu = Menu(menubar, tearoff=0)
    setmenu.add_command(label=Setting[language], command=setwindow)
    setmenu.add_separator()
    setmenu.add_command(label=Exit[language], command=close)
    menubar.add_cascade(label=Set[language], menu=setmenu)

    # 도움
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label=How[language], command=howwindow)
    helpmenu.add_command(label=Info[language], command=Infowindow)
    menubar.add_cascade(label=Help[language], menu=helpmenu)

    window.config(menu=menubar)

    btn_start = Button(frame_button, width=10, text=Solving[language], fg="green", bg="white", relief="raised", overrelief="flat",
                       command=lambda: start_(window, btn_start))
    btn_start.grid(row=0, column=0)

    # btn_free = Button(frame_button, width=10, text="free mode", fg="blue", bg="white", relief="raised", overrelief="flat",
                      # command=lambda: cube_graphic())
    # btn_free.grid(row=0, column=1)

    btn_exit = Button(frame_button, width=10, text=Exit[language], fg="red", bg="white", relief="raised", overrelief="flat",
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
            btn_next.config(text=Complete[language], command=lambda: exit_graph(k, solution, steps))
        if num[0] > 7:
            top.destroy()

    def exit_(num):
        num[0] = 0
        btn_next["state"] = DISABLED
        btn["state"] = NORMAL
        top.destroy()

    def exit_graph(num, sol, steps):
        procs = []
        num[0] = 0
        btn["state"] = NORMAL
        # print(sol)

        # print(full)
        CUBIE = Cubie(full, 'solving', sol, steps, rotation_speed)
        proc_graph = multiprocessing.Process(target=CUBIE.run())
        procs.append(proc_graph)
        proc_graph.start()
        proc_graph.join()

    top = Toplevel(window)
    top.grab_set()
    top.title("Color Detector")
    top.iconbitmap(default="src/cube.ico")
    top.geometry()

    top.protocol("WM_DELETE_WINDOW", lambda: exit_(k))
    top.bind("<Destroy>")

    frame_image = Frame(top)
    frame_image.grid(row=0, column=0, padx=10, pady=2)

    frame_btn = Frame(top, bg="white")
    frame_btn.grid(row=1)

    btn_prev = Button(frame_btn, width=10, text=Previous[language], fg="blue", bg="white", relief="raised", overrelief="flat",
                      command=lambda: prev(k, CUBE))
    btn_prev.grid(row=0, column=0)

    btn_next = Button(frame_btn, width=10, text=Next[language], fg="green", bg="white", relief="raised", overrelief="flat",
                      command=lambda: next_(k, CUBE, c))
    btn_next.grid(row=0, column=1)
    # top.bind("<Key>", lambda: next_(k, CUBE, c))

    btn_exit = Button(frame_btn, width=10, text=Exit[language], fg="red", bg="white", relief="raised", overrelief="flat",
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


def main():
    root = Tk()

    root.config(background="white")
    root.title("Rubik's cube solver")

    init(root)

    root.mainloop()


if __name__ == "__main__":
    main()
