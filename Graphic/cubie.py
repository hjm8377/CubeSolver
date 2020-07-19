from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from pygame.locals import *

from Graphic.const import *
from Graphic.quat import *
from Graphic.SetCaption import *

from Stack.Stack import *

import copy

moves = ''


class Cubie:
    def __init__(self, COLOR=None, mode='free', args=None, steps=None, s=10):
        pygame.init()
        pygame.font.init()
        self.width = 800
        self.height = 600
        self.size = (self.width, self.height)
        self.COLOR = copy.deepcopy(COLOR)
        self.mode = mode
        self.inc = s
        self.running = True
        self.corner_pieces = copy.deepcopy(corner_pieces)
        self.edge_pieces = copy.deepcopy(edge_pieces)
        self.center_pieces = copy.deepcopy(center_pieces)
        self.cube_surfaces = copy.deepcopy(cube_surfaces)
        self.cube_edges = copy.deepcopy(cube_edges)
        self.edges = copy.deepcopy(edges)
        self.steps = copy.deepcopy(steps)
        self.sum_for_cap = 0

        if self.steps is not None:
            self.white_cross = len(self.steps[1])
            self.first_step = len(self.steps[2])
            self.second_step = len(self.steps[3])
            self.yellow_cross = len(self.steps[4])
            self.yellow_face = len(self.steps[5])
            self.third_corner = len(self.steps[6])
            self.third_edge = len(self.steps[7])
            self.caption = SetCaption(self.white_cross, self.first_step, self.second_step, self.yellow_cross,
                                      self.yellow_face, self.third_corner, self.third_edge)

        if mode == 'free':
            self.flag = 1
            self.COLOR = [[['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']], [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']], [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']], [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']], [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']], [['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']]]
            # print("flag == 1")
        elif mode == 'solving':
            self.flag = 0
            self.stk1 = stack()
            self.stk2 = stack()

            for i in range(len(args) - 1, -1, -1):
                self.stk1.push(args[i])

        self.screen = pygame.display.set_mode((self.width, self.height), DOUBLEBUF | OPENGLBLIT)
        pygame.display.set_caption('Rubik\'s cube solver')

        icon = pygame.image.load('D:\\Git\\Baram Project\\2020_1\\src\\cube.ico')
        pygame.display.set_icon(icon)

        glClearColor(1, 1, 1, 0)

        # 은면 제거
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LESS)
        # glutInit()

        # 원근 투영 설정
        glMatrixMode(GL_PROJECTION)
        gluPerspective(45, (self.width / self.height), 0.5, 40)
        glTranslatef(0.0, 0.0, -17.5)

        # 시점 설정
        gluLookAt(5, 5, 5, 0, 0, 0, 0, 1, 0)

    def new_window(self, width, height):
        pygame.display.set_mode(self.size, DOUBLEBUF | OPENGLBLIT | RESIZABLE)
        gluPerspective(45, (width / height), 0.5, 40)

    def draw_cube(self):
        glLineWidth(GLfloat(6.0))
        glBegin(GL_LINES)
        glColor3fv((0.0, 0.0, 0.0))
        # glColor3fv((1.0, 1.0, 1.0))

        for axis in self.edge_pieces:
            for piece in axis:
                for edge in self.cube_edges:
                    for vertex in edge:
                        glVertex3fv(piece[vertex])
        for piece in self.center_pieces:
            for edge in self.cube_edges:
                for vertex in edge:
                    glVertex3fv(piece[vertex])
        for piece in self.corner_pieces:
            for edge in self.cube_edges:
                for vertex in edge:
                    glVertex3fv(piece[vertex])
        glEnd()
        if self.flag == 1:
            self.draw_stickers()
        elif self.flag == 0:
            self.draw_stickers()

    def draw_stickers(self):
        # center block
        glBegin(GL_QUADS)
        # up
        glColor3fv(color_to_rgb(self.COLOR[0][1][1]))
        for i in [5, 6, 2, 1]:
            glVertex3fv(self.center_pieces[4][i])

        # left
        glColor3fv(color_to_rgb(self.COLOR[1][1][1]))
        for i in [0, 1, 5, 4]:
            glVertex3fv(self.center_pieces[1][i])

        # front
        glColor3fv(color_to_rgb(self.COLOR[2][1][1]))
        for i in [0, 1, 2, 3]:
            glVertex3fv(self.center_pieces[0][i])

        # right
        glColor3fv(color_to_rgb(self.COLOR[3][1][1]))
        for i in [6, 7, 3, 2]:
            glVertex3fv(self.center_pieces[3][i])

        # back
        glColor3fv(color_to_rgb(self.COLOR[4][1][1]))
        for i in [4, 5, 6, 7]:
            glVertex3fv(self.center_pieces[2][i])

        # down
        glColor3fv(color_to_rgb(self.COLOR[5][1][1]))
        for i in [0, 3, 7, 4]:
            glVertex3fv(self.center_pieces[5][i])
        glEnd()

        # edge block
        glBegin(GL_QUADS)
        # 0
        glColor3fv(color_to_rgb(self.COLOR[0][0][1]))
        for i in [1, 2, 6, 5]:
            glVertex3fv(self.edge_pieces[0][2][i])
        glColor3fv(color_to_rgb(self.COLOR[4][0][1]))
        for i in [4, 5, 6, 7]:
            glVertex3fv(self.edge_pieces[0][2][i])

        # 1
        glColor3fv(color_to_rgb(self.COLOR[0][1][0]))
        for i in [1, 2, 6, 5]:
            glVertex3fv(self.edge_pieces[2][1][i])
        glColor3fv(color_to_rgb(self.COLOR[1][0][1]))
        for i in [0, 1, 5, 4]:
            glVertex3fv(self.edge_pieces[2][1][i])

        # 2
        glColor3fv(color_to_rgb(self.COLOR[0][2][1]))
        for i in [1, 2, 6, 5]:
            glVertex3fv(self.edge_pieces[0][1][i])
        glColor3fv(color_to_rgb(self.COLOR[2][0][1]))
        for i in [0, 1, 2, 3]:
            glVertex3fv(self.edge_pieces[0][1][i])

        # 3
        glColor3fv(color_to_rgb(self.COLOR[0][1][2]))
        for i in [1, 2, 6, 5]:
            glVertex3fv(self.edge_pieces[2][2][i])
        glColor3fv(color_to_rgb(self.COLOR[3][0][1]))
        for i in [2, 3, 7, 6]:
            glVertex3fv(self.edge_pieces[2][2][i])

        # 4
        glColor3fv(color_to_rgb(self.COLOR[4][1][2]))
        for i in [4, 5, 6, 7]:
            glVertex3fv(self.edge_pieces[1][1][i])
        glColor3fv(color_to_rgb(self.COLOR[1][1][0]))
        for i in [0, 1, 5, 4]:
            glVertex3fv(self.edge_pieces[1][1][i])

        # 5
        glColor3fv(color_to_rgb(self.COLOR[1][1][2]))
        for i in [0, 1, 5, 4]:
            glVertex3fv(self.edge_pieces[1][0][i])
        glColor3fv(color_to_rgb(self.COLOR[2][1][0]))
        for i in [0, 1, 2, 3]:
            glVertex3fv(self.edge_pieces[1][0][i])

        # 6
        glColor3fv(color_to_rgb(self.COLOR[2][1][2]))
        for i in [0, 1, 2, 3]:
            glVertex3fv(self.edge_pieces[1][3][i])
        glColor3fv(color_to_rgb(self.COLOR[3][1][0]))
        for i in [2, 3, 7, 6]:
            glVertex3fv(self.edge_pieces[1][3][i])

        # 7
        glColor3fv(color_to_rgb(self.COLOR[3][1][2]))
        for i in [2, 3, 7, 6]:
            glVertex3fv(self.edge_pieces[1][2][i])
        glColor3fv(color_to_rgb(self.COLOR[4][1][0]))
        for i in [4, 5, 6, 7]:
            glVertex3fv(self.edge_pieces[1][2][i])

        # 8
        glColor3fv(color_to_rgb(self.COLOR[4][2][1]))
        for i in [4, 5, 6, 7]:
            glVertex3fv(self.edge_pieces[0][3][i])
        glColor3fv(color_to_rgb(self.COLOR[5][2][1]))
        for i in [0, 3, 7, 4]:
            glVertex3fv(self.edge_pieces[0][3][i])

        # 9
        glColor3fv(color_to_rgb(self.COLOR[1][2][1]))
        for i in [0, 1, 5, 4]:
            glVertex3fv(self.edge_pieces[2][0][i])
        glColor3fv(color_to_rgb(self.COLOR[5][1][0]))
        for i in [0, 3, 7, 4]:
            glVertex3fv(self.edge_pieces[2][0][i])

        # 10
        glColor3fv(color_to_rgb(self.COLOR[2][2][1]))
        for i in [0, 1, 2, 3]:
            glVertex3fv(self.edge_pieces[0][0][i])
        glColor3fv(color_to_rgb(self.COLOR[5][0][1]))
        for i in [0, 3, 7, 4]:
            glVertex3fv(self.edge_pieces[0][0][i])

        # 11
        glColor3fv(color_to_rgb(self.COLOR[3][2][1]))
        for i in [2, 3, 7, 6]:
            glVertex3fv(self.edge_pieces[2][3][i])
        glColor3fv(color_to_rgb(self.COLOR[5][1][2]))
        for i in [0, 3, 7, 4]:
            glVertex3fv(self.edge_pieces[2][3][i])
        glEnd()

        # corner block
        glBegin(GL_QUADS)
        # 0
        glColor3fv(color_to_rgb(self.COLOR[5][0][0]))
        for i in [0, 3, 7, 4]:
            glVertex3fv(self.corner_pieces[0][i])
        glColor3fv(color_to_rgb(self.COLOR[1][2][2]))
        for i in [0, 1, 5, 4]:
            glVertex3fv(self.corner_pieces[0][i])
        glColor3fv(color_to_rgb(self.COLOR[2][2][0]))
        for i in [0, 1, 2, 3]:
            glVertex3fv(self.corner_pieces[0][i])

        # 1
        glColor3fv(color_to_rgb(self.COLOR[0][2][0]))
        for i in [1, 2, 6, 5]:
            glVertex3fv(self.corner_pieces[1][i])
        glColor3fv(color_to_rgb(self.COLOR[1][0][2]))
        for i in [0, 1, 5, 4]:
            glVertex3fv(self.corner_pieces[1][i])
        glColor3fv(color_to_rgb(self.COLOR[2][0][0]))
        for i in [0, 1, 2, 3]:
            glVertex3fv(self.corner_pieces[1][i])

        # 2
        glColor3fv(color_to_rgb(self.COLOR[0][2][2]))
        for i in [1, 2, 6, 5]:
            glVertex3fv(self.corner_pieces[2][i])
        glColor3fv(color_to_rgb(self.COLOR[2][0][2]))
        for i in [0, 1, 2, 3]:
            glVertex3fv(self.corner_pieces[2][i])
        glColor3fv(color_to_rgb(self.COLOR[3][0][0]))
        for i in [3, 2, 6, 7]:
            glVertex3fv(self.corner_pieces[2][i])

        # 3
        glColor3fv(color_to_rgb(self.COLOR[5][0][2]))
        for i in [0, 3, 7, 4]:
            glVertex3fv(self.corner_pieces[3][i])
        glColor3fv(color_to_rgb(self.COLOR[3][2][0]))
        for i in [3, 2, 6, 7]:
            glVertex3fv(self.corner_pieces[3][i])
        glColor3fv(color_to_rgb(self.COLOR[2][2][2]))
        for i in [0, 1, 2, 3]:
            glVertex3fv(self.corner_pieces[3][i])

        # 4
        glColor3fv(color_to_rgb(self.COLOR[5][2][0]))
        for i in [0, 3, 7, 4]:
            glVertex3fv(self.corner_pieces[4][i])
        glColor3fv(color_to_rgb(self.COLOR[1][2][0]))
        for i in [0, 1, 5, 4]:
            glVertex3fv(self.corner_pieces[4][i])
        glColor3fv(color_to_rgb(self.COLOR[4][2][2]))
        for i in [4, 5, 6, 7]:
            glVertex3fv(self.corner_pieces[4][i])

        # 5
        glColor3fv(color_to_rgb(self.COLOR[0][0][0]))
        for i in [1, 2, 6, 5]:
            glVertex3fv(self.corner_pieces[5][i])
        glColor3fv(color_to_rgb(self.COLOR[1][0][0]))
        for i in [0, 1, 5, 4]:
            glVertex3fv(self.corner_pieces[5][i])
        glColor3fv(color_to_rgb(self.COLOR[4][0][2]))
        for i in [4, 5, 6, 7]:
            glVertex3fv(self.corner_pieces[5][i])

        # 6
        glColor3fv(color_to_rgb(self.COLOR[0][0][2]))
        for i in [1, 2, 6, 5]:
            glVertex3fv(self.corner_pieces[6][i])
        glColor3fv(color_to_rgb(self.COLOR[3][0][2]))
        for i in [2, 3, 7, 6]:
            glVertex3fv(self.corner_pieces[6][i])
        glColor3fv(color_to_rgb(self.COLOR[4][0][0]))
        for i in [4, 5, 6, 7]:
            glVertex3fv(self.corner_pieces[6][i])

        # 7
        glColor3fv(color_to_rgb(self.COLOR[5][2][2]))
        for i in [0, 3, 7, 4]:
            glVertex3fv(self.corner_pieces[7][i])
        glColor3fv(color_to_rgb(self.COLOR[3][2][2]))
        for i in [2, 3, 7, 6]:
            glVertex3fv(self.corner_pieces[7][i])
        glColor3fv(color_to_rgb(self.COLOR[4][2][0]))
        for i in [4, 5, 6, 7]:
            glVertex3fv(self.corner_pieces[7][i])

        glEnd()

        glBegin(GL_QUADS)
        # 엣지 조각의 안쪽
        edge_black_pat = [
            [0, 1, 2, 3, 4, 5],
            [0, 1, 2, 3, 4, 5],
            [0, 1, 2, 3, 4, 5]
            # [4, 5],
            # [0, 2]
        ]

        glColor3fv((0, 0, 0))

        for i in range(len(edge_black_pat)):
            for face in edge_black_pat[i]:
                for piece in self.edge_pieces[i]:
                    for vertex in self.cube_surfaces[face]:
                        glVertex3fv(piece[vertex])

        corner_color_pat = [
            [0, 1, 5],  # 0
            [0, 1, 4],  # 1
            [0, 3, 4],  # 2
            [0, 3, 5],  # 3
            [2, 1, 5],  # 4
            [2, 1, 4],  # 5
            [2, 3, 4],  # 6
            [2, 3, 5],  # 7
        ]

        corner_black_pat = [
            [2, 3, 4],  # 0
            [2, 3, 5],  # 1
            [2, 1, 5],  # 2
            [2, 1, 4],  # 3
            [0, 3, 4],  # 4
            [0, 3, 5],  # 5
            [0, 1, 5],  # 6
            [0, 1, 4],  # 7
        ]

        for i in range(len(corner_color_pat)):
            for face in corner_color_pat[i]:
                glColor3fv(cube_colors[face])
                for vertex in self.cube_surfaces[face]:
                    glVertex3fv(self.corner_pieces[i][vertex])
        glColor3fv((0, 0, 0))
        for i in range(len(corner_black_pat)):
            for face in corner_black_pat[i]:
                for vertex in self.cube_surfaces[face]:
                    glVertex3fv(self.corner_pieces[i][vertex])

        glEnd()

    def draw_stickers_none(self):
        glBegin(GL_QUADS)
        i = 0
        for color, surface in zip(cube_colors, self.cube_surfaces):
            glColor3fv(color)
            for vertex in surface:
                glVertex3fv(self.center_pieces[i][vertex])
            j = 0
            for piece in self.center_pieces:
                glColor3fv((0, 0, 0))
                for vertex in surface:
                    glVertex3fv(self.center_pieces[j][vertex])
                j += 1
            i += 1

        for color, surface, face in zip(cube_colors, self.cube_surfaces, self.edges):
            glColor3fv(color)
            for piece in face:
                for vertex in surface:
                    glVertex3fv(self.edge_pieces[piece[0]][piece[1]][vertex])

        # 엣지 조각의 안쪽
        edge_black_pat = [
            [0, 1, 2, 3, 4, 5],
            [0, 1, 2, 3, 4, 5],
            [0, 1, 2, 3, 4, 5]
            # [4, 5],
            # [0, 2]
        ]

        glColor3fv((0, 0, 0))

        for i in range(len(edge_black_pat)):
            for face in edge_black_pat[i]:
                for piece in self.edge_pieces[i]:
                    for vertex in self.cube_surfaces[face]:
                        glVertex3fv(piece[vertex])

        corner_color_pat = [
            [0, 1, 5],  # 0
            [0, 1, 4],  # 1
            [0, 3, 4],  # 2
            [0, 3, 5],  # 3
            [2, 1, 5],  # 4
            [2, 1, 4],  # 5
            [2, 3, 4],  # 6
            [2, 3, 5],  # 7
        ]

        corner_black_pat = [
            [2, 3, 4],  # 0
            [2, 3, 5],  # 1
            [2, 1, 5],  # 2
            [2, 1, 4],  # 3
            [0, 3, 4],  # 4
            [0, 3, 5],  # 5
            [0, 1, 5],  # 6
            [0, 1, 4],  # 7
        ]

        for i in range(len(corner_color_pat)):
            for face in corner_color_pat[i]:
                glColor3fv(cube_colors[face])
                for vertex in self.cube_surfaces[face]:
                    glVertex3fv(self.corner_pieces[i][vertex])
        glColor3fv((0, 0, 0))
        for i in range(len(corner_black_pat)):
            for face in corner_black_pat[i]:
                for vertex in self.cube_surfaces[face]:
                    glVertex3fv(self.corner_pieces[i][vertex])

        glEnd()

    def run(self):
        global moves

        def update():
            if self.running is False:
                return None
            pygame.mouse.get_rel()

            ratio = 1

            # 모델뷰 행렬 계산
            glMatrixMode(GL_MODELVIEW)
            glScalef(ratio, ratio, ratio)

            # 화면 초기화
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            self.draw_cube()
            # glutSolidSphere(3.0, 50, 50)
            # glColor3fv((0, 0, 0))
            # sphere = gluNewQuadric()
            # gluSphere(sphere, 3.0, 50, 50)
            pygame.display.flip()

        while True and self.running is True:
            theta_inc = self.inc
            theta = pi / 2 / theta_inc

            for event in pygame.event.get():
                if event.type is pygame.QUIT:
                    # print()
                    pygame.quit()
                    self.running = False

                # 키보드가 눌릴 때 & mode가 solving일 때
                if (event.type is pygame.KEYDOWN) and (self.flag == 0):
                    if event.key == pygame.K_RIGHT:
                        # print("RIGHT")
                        if self.sum_for_cap < self.white_cross + self.first_step + self.second_step + self.yellow_cross\
                                + self.yellow_face + self.third_corner + self.third_edge:
                            self.sum_for_cap += 1
                        self.caption.set_caption(self.sum_for_cap)
                        # print(self.sum_for_cap)
                        if not self.stk1.is_empty():
                            self.stk2.push(self.stk1.peek())
                        # stk2 top값 그대로

                        if not self.stk1.is_empty() and self.stk1.peek()[0] == 'F':
                            if self.stk1.peek() == 'F':
                                theta *= -1
                            elif self.stk1.peek() == "F'":
                                theta *= 1
                            elif self.stk1.peek() == 'F2':
                                theta *= 2
                            else:
                                theta *= 0

                            for x in range(theta_inc):
                                for i in range(8):
                                    self.center_pieces[0][i] = z_rot(self.center_pieces[0][i], theta)

                                for axis in self.edge_pieces:
                                    for piece in axis:
                                        flag = True
                                        for vertex in piece:
                                            if vertex[2] < 0:
                                                flag = False
                                                break
                                        if flag:
                                            for i in range(8):
                                                piece[i] = z_rot(piece[i], theta)

                                for piece in self.corner_pieces:
                                    flag = True
                                    for vertex in piece:
                                        if vertex[2] < 0:
                                            flag = False
                                            break
                                    if flag:
                                        for i in range(8):
                                            piece[i] = z_rot(piece[i], theta)
                                update()
                            self.stk1.pop()

                        elif not self.stk1.is_empty() and self.stk1.peek()[0] == 'L':
                            if self.stk1.peek() == 'L':
                                theta *= 1
                            elif self.stk1.peek() == "L'":
                                theta *= -1
                            elif self.stk1.peek() == 'L2':
                                theta *= 2
                            else:
                                theta *= 0

                            for x in range(theta_inc):
                                for i in range(8):
                                    self.center_pieces[1][i] = x_rot(self.center_pieces[1][i], theta)

                                for axis in self.edge_pieces:
                                    for piece in axis:
                                        flag = True
                                        for vertex in piece:
                                            if vertex[0] > 0:
                                                flag = False
                                                break
                                        if flag:
                                            for i in range(8):
                                                piece[i] = x_rot(piece[i], theta)

                                for piece in self.corner_pieces:
                                    flag = True
                                    for vertex in piece:
                                        if vertex[0] > 0:
                                            flag = False
                                            break
                                    if flag:
                                        for i in range(8):
                                            piece[i] = x_rot(piece[i], theta)

                                update()
                            self.stk1.pop()

                        elif not self.stk1.is_empty() and self.stk1.peek()[0] == 'B':
                            if self.stk1.peek() == 'B':
                                theta *= 1
                            elif self.stk1.peek() == "B'":
                                theta *= -1
                            elif self.stk1.peek() == "B2":
                                theta *= 2
                            else:
                                theta *= 0

                            for x in range(theta_inc):
                                for i in range(8):
                                    self.center_pieces[2][i] = z_rot(self.center_pieces[2][i], theta)

                                for axis in self.edge_pieces:
                                    for piece in axis:
                                        flag = True
                                        for vertex in piece:
                                            if vertex[2] > 0:
                                                flag = False
                                                break
                                        if flag:
                                            for i in range(8):
                                                piece[i] = z_rot(piece[i], theta)

                                for piece in self.corner_pieces:
                                    flag = True
                                    for vertex in piece:
                                        if vertex[2] > 0:
                                            flag = False
                                            break
                                    if flag:
                                        for i in range(8):
                                            piece[i] = z_rot(piece[i], theta)

                                update()
                            self.stk1.pop()

                        elif not self.stk1.is_empty() and self.stk1.peek()[0] == 'R':
                            if self.stk1.peek() == 'R':
                                theta *= -1
                            elif self.stk1.peek() == "R'":
                                theta *= 1
                            elif self.stk1.peek() == 'R2':
                                theta *= -2
                            else:
                                theta *= 0

                            for x in range(theta_inc):
                                for i in range(8):
                                    self.center_pieces[3][i] = x_rot(self.center_pieces[3][i], theta)

                                for axis in self.edge_pieces:
                                    for piece in axis:
                                        flag = True
                                        for vertex in piece:
                                            if vertex[0] < 0:
                                                flag = False
                                                break
                                        if flag:
                                            for i in range(8):
                                                piece[i] = x_rot(piece[i], theta)

                                for piece in self.corner_pieces:
                                    flag = True
                                    for vertex in piece:
                                        if vertex[0] < 0:
                                            flag = False
                                            break
                                    if flag:
                                        for i in range(8):
                                            piece[i] = x_rot(piece[i], theta)

                                update()
                            self.stk1.pop()

                        elif not self.stk1.is_empty() and self.stk1.peek()[0] == 'U':
                            if self.stk1.peek() == 'U':
                                theta *= -1
                            elif self.stk1.peek() == "U'":
                                theta *= 1
                            elif self.stk1.peek() == 'U2':
                                theta *= 2
                            else:
                                theta *= 0

                            for x in range(theta_inc):
                                for i in range(8):
                                    self.center_pieces[4][i] = y_rot(self.center_pieces[4][i], theta)

                                for axis in self.edge_pieces:
                                    for piece in axis:
                                        flag = True
                                        for vertex in piece:
                                            if vertex[1] < 0:
                                                flag = False
                                                break
                                        if flag:
                                            for i in range(8):
                                                piece[i] = y_rot(piece[i], theta)

                                for piece in self.corner_pieces:
                                    flag = True
                                    for vertex in piece:
                                        if vertex[1] < 0:
                                            flag = False
                                            break
                                    if flag:
                                        for i in range(8):
                                            piece[i] = y_rot(piece[i], theta)

                                update()
                            self.stk1.pop()

                        elif not self.stk1.is_empty() and self.stk1.peek()[0] == 'D':
                            if self.stk1.peek() == 'D':
                                theta *= 1
                            elif self.stk1.peek() == "D'":
                                theta *= -1
                            elif self.stk1.peek() == "D2":
                                theta *= 2
                            else:
                                theta *= 0

                            for x in range(theta_inc):
                                for i in range(8):
                                    self.center_pieces[5][i] = y_rot(self.center_pieces[5][i], theta)

                                for axis in self.edge_pieces:
                                    for piece in axis:
                                        flag = True
                                        for vertex in piece:
                                            if vertex[1] > 0:
                                                flag = False
                                                break
                                        if flag:
                                            for i in range(8):
                                                piece[i] = y_rot(piece[i], theta)

                                for piece in self.corner_pieces:
                                    flag = True
                                    for vertex in piece:
                                        if vertex[1] > 0:
                                            flag = False
                                            break
                                    if flag:
                                        for i in range(8):
                                            piece[i] = y_rot(piece[i], theta)

                                update()
                            self.stk1.pop()

                        elif not self.stk1.is_empty() and self.stk1.peek()[0] == 'X':
                            if self.stk1.peek() == 'X':
                                theta *= -1
                            elif self.stk1.peek() == "X'":
                                theta *= 1
                            else:
                                theta *= 0

                            for x in range(theta_inc):
                                for i in range(8):
                                    for j in range(6):
                                        self.center_pieces[j][i] = x_rot(self.center_pieces[j][i], theta)
                                    for k in range(8):
                                        self.corner_pieces[k][i] = x_rot(self.corner_pieces[k][i], theta)
                                    for l in range(4):
                                        for m in range(3):
                                            self.edge_pieces[m][l][i] = x_rot(self.edge_pieces[m][l][i], theta)

                                update()
                            self.stk1.pop()

                        elif not self.stk1.is_empty() and self.stk1.peek()[0] == 'Y':
                            if self.stk1.peek() == 'Y':
                                theta *= -1
                            elif self.stk1.peek() == "Y'":
                                theta *= 1
                            else:
                                theta *= 0

                            for x in range(theta_inc):
                                for i in range(8):
                                    for j in range(6):
                                        self.center_pieces[j][i] = y_rot(self.center_pieces[j][i], theta)
                                    for k in range(8):
                                        self.corner_pieces[k][i] = y_rot(self.corner_pieces[k][i], theta)
                                    for l in range(4):
                                        for m in range(3):
                                            self.edge_pieces[m][l][i] = y_rot(self.edge_pieces[m][l][i], theta)

                                update()
                            self.stk1.pop()

                    if event.key == pygame.K_LEFT:
                        # print("LEFT")
                        if self.sum_for_cap > 0:
                            self.sum_for_cap -= 1
                        self.caption.set_caption(self.sum_for_cap)
                        # print(self.sum_for_cap)
                        if not self.stk2.is_empty():
                            self.stk1.push(self.stk2.peek())
                        # stk2 top값의 반대로

                        if not self.stk2.is_empty() and self.stk2.peek()[0] == 'F':
                            if self.stk2.peek() == 'F':
                                theta *= 1
                            elif self.stk2.peek() == "F'":
                                theta *= -1
                            elif self.stk2.peek() == 'F2':
                                theta *= 2
                            else:
                                theta *= 0

                            for x in range(theta_inc):
                                for i in range(8):
                                    self.center_pieces[0][i] = z_rot(self.center_pieces[0][i], theta)

                                for axis in self.edge_pieces:
                                    for piece in axis:
                                        flag = True
                                        for vertex in piece:
                                            if vertex[2] < 0:
                                                flag = False
                                                break
                                        if flag:
                                            for i in range(8):
                                                piece[i] = z_rot(piece[i], theta)

                                for piece in self.corner_pieces:
                                    flag = True
                                    for vertex in piece:
                                        if vertex[2] < 0:
                                            flag = False
                                            break
                                    if flag:
                                        for i in range(8):
                                            piece[i] = z_rot(piece[i], theta)
                                update()
                            self.stk2.pop()

                        elif not self.stk2.is_empty() and self.stk2.peek()[0] == 'L':
                            if self.stk2.peek() == 'L':
                                theta *= -1
                            elif self.stk2.peek() == "L'":
                                theta *= 1
                            elif self.stk2.peek() == 'L2':
                                theta *= 2
                            else:
                                theta *= 0

                            for x in range(theta_inc):
                                for i in range(8):
                                    self.center_pieces[1][i] = x_rot(self.center_pieces[1][i], theta)

                                for axis in self.edge_pieces:
                                    for piece in axis:
                                        flag = True
                                        for vertex in piece:
                                            if vertex[0] > 0:
                                                flag = False
                                                break
                                        if flag:
                                            for i in range(8):
                                                piece[i] = x_rot(piece[i], theta)

                                for piece in self.corner_pieces:
                                    flag = True
                                    for vertex in piece:
                                        if vertex[0] > 0:
                                            flag = False
                                            break
                                    if flag:
                                        for i in range(8):
                                            piece[i] = x_rot(piece[i], theta)

                                update()
                            self.stk2.pop()

                        elif not self.stk2.is_empty() and self.stk2.peek()[0] == 'B':
                            if self.stk2.peek() == "B'":
                                theta *= 1
                            elif self.stk2.peek() == 'B':
                                theta *= -1
                            elif self.stk2.peek() == "B2":
                                theta *= 2
                            else:
                                theta *= 0

                            for x in range(theta_inc):
                                for i in range(8):
                                    self.center_pieces[2][i] = z_rot(self.center_pieces[2][i], theta)

                                for axis in self.edge_pieces:
                                    for piece in axis:
                                        flag = True
                                        for vertex in piece:
                                            if vertex[2] > 0:
                                                flag = False
                                                break
                                        if flag:
                                            for i in range(8):
                                                piece[i] = z_rot(piece[i], theta)

                                for piece in self.corner_pieces:
                                    flag = True
                                    for vertex in piece:
                                        if vertex[2] > 0:
                                            flag = False
                                            break
                                    if flag:
                                        for i in range(8):
                                            piece[i] = z_rot(piece[i], theta)

                                update()
                            self.stk2.pop()

                        elif not self.stk2.is_empty() and self.stk2.peek()[0] == 'R':
                            if self.stk2.peek() == 'R':
                                theta *= 1
                            elif self.stk2.peek() == "R'":
                                theta *= -1
                            elif self.stk2.peek() == 'R2':
                                theta *= -2
                            else:
                                theta *= 0

                            for x in range(theta_inc):
                                for i in range(8):
                                    self.center_pieces[3][i] = x_rot(self.center_pieces[3][i], theta)

                                for axis in self.edge_pieces:
                                    for piece in axis:
                                        flag = True
                                        for vertex in piece:
                                            if vertex[0] < 0:
                                                flag = False
                                                break
                                        if flag:
                                            for i in range(8):
                                                piece[i] = x_rot(piece[i], theta)

                                for piece in self.corner_pieces:
                                    flag = True
                                    for vertex in piece:
                                        if vertex[0] < 0:
                                            flag = False
                                            break
                                    if flag:
                                        for i in range(8):
                                            piece[i] = x_rot(piece[i], theta)

                                update()
                            self.stk2.pop()

                        elif not self.stk2.is_empty() and self.stk1.peek()[0] == 'U':
                            if self.stk2.peek() == 'U':
                                theta *= 1
                            elif self.stk2.peek() == "U'":
                                theta *= -1
                            elif self.stk2.peek() == 'U2':
                                theta *= 2
                            else:
                                theta *= 0

                            for x in range(theta_inc):
                                for i in range(8):
                                    self.center_pieces[4][i] = y_rot(self.center_pieces[4][i], theta)

                                for axis in self.edge_pieces:
                                    for piece in axis:
                                        flag = True
                                        for vertex in piece:
                                            if vertex[1] < 0:
                                                flag = False
                                                break
                                        if flag:
                                            for i in range(8):
                                                piece[i] = y_rot(piece[i], theta)

                                for piece in self.corner_pieces:
                                    flag = True
                                    for vertex in piece:
                                        if vertex[1] < 0:
                                            flag = False
                                            break
                                    if flag:
                                        for i in range(8):
                                            piece[i] = y_rot(piece[i], theta)

                                update()
                            self.stk2.pop()

                        elif not self.stk2.is_empty() and self.stk2.peek()[0] == 'D':
                            if self.stk2.peek() == 'D':
                                theta *= -1
                            elif self.stk2.peek() == "D'":
                                theta *= 1
                            elif self.stk2.peek() == "D2":
                                theta *= 2
                            else:
                                theta *= 0

                            for x in range(theta_inc):
                                for i in range(8):
                                    self.center_pieces[5][i] = y_rot(self.center_pieces[5][i], theta)

                                for axis in self.edge_pieces:
                                    for piece in axis:
                                        flag = True
                                        for vertex in piece:
                                            if vertex[1] > 0:
                                                flag = False
                                                break
                                        if flag:
                                            for i in range(8):
                                                piece[i] = y_rot(piece[i], theta)

                                for piece in self.corner_pieces:
                                    flag = True
                                    for vertex in piece:
                                        if vertex[1] > 0:
                                            flag = False
                                            break
                                    if flag:
                                        for i in range(8):
                                            piece[i] = y_rot(piece[i], theta)

                                update()
                            self.stk2.pop()

                        elif not self.stk2.is_empty() and self.stk2.peek()[0] == 'X':
                            if self.stk2.peek() == 'X':
                                theta *= 1
                            elif self.stk2.peek() == "X'":
                                theta *= -1
                            else:
                                theta *= 0

                            for x in range(theta_inc):
                                for i in range(8):
                                    for j in range(6):
                                        self.center_pieces[j][i] = x_rot(self.center_pieces[j][i], theta)
                                    for k in range(8):
                                        self.corner_pieces[k][i] = x_rot(self.corner_pieces[k][i], theta)
                                    for l in range(4):
                                        for m in range(3):
                                            self.edge_pieces[m][l][i] = x_rot(self.edge_pieces[m][l][i], theta)

                                update()
                            self.stk2.pop()

                        elif not self.stk2.is_empty() and self.stk2.peek()[0] == 'Y':
                            if self.stk2.peek() == 'Y':
                                theta *= 1
                            elif self.stk2.peek() == "Y'":
                                theta *= -1
                            else:
                                theta *= 0

                            for x in range(theta_inc):
                                for i in range(8):
                                    for j in range(6):
                                        self.center_pieces[j][i] = y_rot(self.center_pieces[j][i], theta)
                                    for k in range(8):
                                        self.corner_pieces[k][i] = y_rot(self.corner_pieces[k][i], theta)
                                    for l in range(4):
                                        for m in range(3):
                                            self.edge_pieces[m][l][i] = y_rot(self.edge_pieces[m][l][i], theta)

                                update()
                            self.stk2.pop()

                if (event.type is pygame.KEYUP) and (self.flag == 0):
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                        theta_inc = self.inc
                        theta = pi / 2 / theta_inc

                # 키보드가 눌릴 때 & mode가 free일 때
                if (event.type is pygame.KEYDOWN) and (self.flag == 1):

                    # x축에 대해 전체 회전
                    if event.key is pygame.K_UP:    # 위 화살표
                        inc_x = pi / 100
                    if event.key is pygame.K_DOWN:  # 아래 화살표
                        inc_x = -pi / 100

                    # x축에 대해 전체 회전

                    if event.key is pygame.K_LEFT:  # 왼쪽 화살표
                        inc_y = pi / 100
                    if event.key is pygame.K_RIGHT:  # 오른쪽 화살표
                        inc_y = -pi / 100

                    if event.key is pygame.K_f:     # f
                        if pygame.key.get_mods() & KMOD_SHIFT:  # 쉬프트와 같이 입력 (대문자)
                            theta *= -1
                        else:   # 소문자
                            theta *= 1

                        for x in range(theta_inc):
                            for i in range(8):
                                self.center_pieces[0][i] = z_rot(self.center_pieces[0][i], theta)

                            for axis in self.edge_pieces:
                                for piece in axis:
                                    flag = True
                                    for vertex in piece:
                                        if vertex[2] < 0:
                                            flag = False
                                            break
                                    if flag:
                                        for i in range(8):
                                            piece[i] = z_rot(piece[i], theta)

                            for piece in self.corner_pieces:
                                flag = True
                                for vertex in piece:
                                    if vertex[2] < 0:
                                        flag = False
                                        break
                                if flag:
                                    for i in range(8):
                                        piece[i] = z_rot(piece[i], theta)

                            update()

                    if event.key == pygame.K_l:
                        if pygame.key.get_mods() & KMOD_SHIFT:
                            theta *= 1
                        else:
                            theta *= -1

                        for x in range(theta_inc):
                            for i in range(8):
                                self.center_pieces[1][i] = x_rot(self.center_pieces[1][i], theta)

                            for axis in self.edge_pieces:
                                for piece in axis:
                                    flag = True
                                    for vertex in piece:
                                        if vertex[0] > 0:
                                            flag = False
                                            break
                                    if flag:
                                        for i in range(8):
                                            piece[i] = x_rot(piece[i], theta)

                            for piece in self.corner_pieces:
                                flag = True
                                for vertex in piece:
                                    if vertex[0] > 0:
                                        flag = False
                                        break
                                if flag:
                                    for i in range(8):
                                        piece[i] = x_rot(piece[i], theta)

                            update()

                    if event.key == pygame.K_b:
                        if pygame.key.get_mods() & KMOD_SHIFT:
                            theta *= 1
                        else:
                            theta *= -1

                        for x in range(theta_inc):
                            for i in range(8):
                                self.center_pieces[2][i] = z_rot(self.center_pieces[2][i], theta)

                            for axis in self.edge_pieces:
                                for piece in axis:
                                    flag = True
                                    for vertex in piece:
                                        if vertex[2] > 0:
                                            flag = False
                                            break
                                    if flag:
                                        for i in range(8):
                                            piece[i] = z_rot(piece[i], theta)

                            for piece in self.corner_pieces:
                                flag = True
                                for vertex in piece:
                                    if vertex[2] > 0:
                                        flag = False
                                        break
                                if flag:
                                    for i in range(8):
                                        piece[i] = z_rot(piece[i], theta)

                            update()

                    if event.key == pygame.K_r:
                        if pygame.key.get_mods() & KMOD_SHIFT:
                            theta *= -1
                        else:
                            theta *= 1

                        for x in range(theta_inc):
                            for i in range(8):
                                self.center_pieces[3][i] = x_rot(self.center_pieces[3][i], theta)

                            for axis in self.edge_pieces:
                                for piece in axis:
                                    flag = True
                                    for vertex in piece:
                                        if vertex[0] < 0:
                                            flag = False
                                            break
                                    if flag:
                                        for i in range(8):
                                            piece[i] = x_rot(piece[i], theta)

                            for piece in self.corner_pieces:
                                flag = True
                                for vertex in piece:
                                    if vertex[0] < 0:
                                        flag = False
                                        break
                                if flag:
                                    for i in range(8):
                                        piece[i] = x_rot(piece[i], theta)

                            update()

                    if event.key == pygame.K_u:
                        if pygame.key.get_mods() & KMOD_SHIFT:
                            theta *= -1
                        else:
                            theta *= 1

                        for x in range(theta_inc):
                            for i in range(8):
                                self.center_pieces[4][i] = y_rot(self.center_pieces[4][i], theta)

                            for axis in self.edge_pieces:
                                for piece in axis:
                                    flag = True
                                    for vertex in piece:
                                        if vertex[1] < 0:
                                            flag = False
                                            break
                                    if flag:
                                        for i in range(8):
                                            piece[i] = y_rot(piece[i], theta)

                            for piece in self.corner_pieces:
                                flag = True
                                for vertex in piece:
                                    if vertex[1] < 0:
                                        flag = False
                                        break
                                if flag:
                                    for i in range(8):
                                        piece[i] = y_rot(piece[i], theta)

                            update()

                    if event.key == pygame.K_d:
                        if pygame.key.get_mods() & KMOD_SHIFT:
                            theta *= 1
                        else:
                            theta *= -1

                        for x in range(theta_inc):
                            for i in range(8):
                                self.center_pieces[5][i] = y_rot(self.center_pieces[5][i], theta)

                            for axis in self.edge_pieces:
                                for piece in axis:
                                    flag = True
                                    for vertex in piece:
                                        if vertex[1] > 0:
                                            flag = False
                                            break
                                    if flag:
                                        for i in range(8):
                                            piece[i] = y_rot(piece[i], theta)

                            for piece in self.corner_pieces:
                                flag = True
                                for vertex in piece:
                                    if vertex[1] > 0:
                                        flag = False
                                        break
                                if flag:
                                    for i in range(8):
                                        piece[i] = y_rot(piece[i], theta)

                            update()

                if event.type is pygame.KEYUP:   # 키보드를 뗄 때
                    # 멈추기
                    if event.key is pygame.K_UP or event.key is pygame.K_DOWN:
                        inc_x = 0.0
                    if event.key is pygame.K_LEFT or event.key is pygame.K_RIGHT or event.key is pygame.K_d \
                            or event.key is pygame.K_l or event.key is pygame.K_f:
                        inc_y = 0.0

            update()


if __name__ == "__main__":
    Color = [[['w', 'b', 'y'], ['r', 'o', 'g'], ['w', 'b', 'y']], [['o', 'y', 'o'], ['g', 'w', 'o'], ['o', 'w', 'b']], [['g', 'w', 'r'], ['y', 'b', 'g'], ['y', 'r', 'g']], [['g', 'w', 'g'], ['r', 'y', 'y'], ['w', 'y', 'r']], [['o', 'o', 'b'], ['g', 'g', 'o'], ['w', 'w', 'b']], [['r', 'b', 'r'], ['r', 'r', 'b'], ['y', 'o', 'b']]]
    solution = ['X', 'Y', 'X', 'U', 'F2', "R'", "U'", 'B2', 'B', 'U', "B'", 'R', 'U', "R'", 'U', "R'", "U'", 'R', 'U2', 'L', 'U2', "L'", "U'", 'L', 'U', "L'", 'U', 'F', 'U', "F'", 'F2', 'U2', 'F2', 'U2', 'F2', 'R2', 'U2', 'F', 'R2', "F'", 'U2', "R'", 'U', "R'", 'U', 'B', "U'", "B'", "U'", "R'", 'U', 'R', 'U2', 'L', "U'", "L'", "U'", "B'", 'U', 'B', 'U', "L'", 'U', 'L', 'U', 'F', "U'", "F'", 'F', 'R', 'U', "R'", "U'", "F'", "U'", 'R', 'U2', "R'", "U'", 'R', 'U2', "L'", 'U', "R'", "U'", 'L', 'U2', "R'", "U'", 'R', "U'", 'R', 'U', 'R', "U'", "R'", 'U', 'R', 'U', 'R2', "U'", "R'", 'U2']
    # print(Color)
    cube = Cubie(Color, 'solving', solution, None)
    cube.run()
