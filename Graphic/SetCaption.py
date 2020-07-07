import pygame


class SetCaption:
    def __init__(self, wc, fs, ss, yc, yf, tc, te):
        self.white_cross = wc
        self.first_step = fs
        self.second_step = ss
        self.yellow_cross = yc
        self.yellow_face = yf
        self.third_corner = tc
        self.third_edge = te

        self.step_arr = list()
        self.first = wc
        self.step_arr.append(self.first)
        self.second = self.first + fs
        self.step_arr.append(self.second)
        self.third = self.second + ss
        self.step_arr.append(self.third)
        self.fourth = self.third + yc
        self.step_arr.append(self.fourth)
        self.fifth = self.fourth + yf
        self.step_arr.append(self.fifth)
        self.sixth = self.fifth + tc
        self.step_arr.append(self.sixth)
        self.seventh = self.sixth + te
        self.step_arr.append(self.seventh)

        self.sum_for_cap = wc + fs + ss + yc + yf + tc + te
        self.flag = 0

    def step_name(self, step):
        if step == 0:
            return "White Cross", self.white_cross, 0
        elif step == 1:
            return "First Layer", self.first_step, self.first
        elif step == 2:
            return "Second Layer", self.second_step, self.second
        elif step == 3:
            return "Yellow Cross", self.yellow_cross, self.third
        elif step == 4:
            return "Yellow Face", self.yellow_face, self.fourth
        elif step == 5:
            return "Third Layer's Corners", self.third_corner, self.fifth
        elif step == 6:
            return "Third Layer's Edges", self.third_edge, self.sixth

    def set_caption(self, summation):
        for i in range(7):
            if self.step_arr[i] >= summation:
                if summation == 0:
                    # print("setup")
                    pygame.display.set_caption('Rubik\'s cube solver')
                else:
                    step_name, step, before = self.step_name(i)
                    if summation - before > 0:
                        string = step_name + " (" + str(step) + "/" + str(summation - before) + ")" + \
                                 "      (Progress [" + str(round((summation / self.sum_for_cap) * 100, 2)) + "%])"
                        # print(string)
                        if summation == self.sum_for_cap:
                            if self.flag == 0:
                                pygame.display.set_caption(string)
                                pygame.time.delay(500)
                                pygame.display.set_caption("Finish!!!")
                                pygame.time.delay(500)
                                pygame.display.set_caption('Rubik\'s cube solver')
                                self.flag = 1
                            elif self.flag == 1:
                                pygame.display.set_caption('Rubik\'s cube solver')
                        else:
                            pygame.display.set_caption(string)
