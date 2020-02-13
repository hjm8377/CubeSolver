from Cube import Rotation


class ThirdLayerEdgeSolver:

    STEP = {
        'Ua': ["R'", "U", "R'", "U'", "R'", "U'", "R'", "U", "R", "U", "R2"],
        'Ub': ["R2", "U'", "R'", "U'", "R", "U", "R", "U", "R", "U'", "R"],
        'Z': ["R'", "U'", "R", "U'", "R", "U", "R", "U'", "R'", "U", "R", "U", "R2", "U'", "R'", "U2"],
        'H': ["R2", "U2", "R2", "U2", "R2", "U", "R2", "U2", "R2", "U2", "R2", "U'"]
    }

    @staticmethod
    def check_third_layer(cube):
        # Ua, Ub 에서 맞는 쪽 찾기
        # 없다면 Z, H
        a = [0, 0, 0]
        for i in range(4):
            for j in range(3):
                a[j] = cube[i + 1][0][j]
            if a[0] == a[1] and a[1] == a[2]:
                return i + 1

        return 5

    @staticmethod
    def check_U_a_b(cube):
        if cube[4][0][1] == cube[3][1][1]:
            return 'Ua'
        elif cube[4][0][1] == cube[1][1][1]:
            return 'Ub'

    @staticmethod
    def check_H_Z(cube):
        if cube[4][0][1] == cube[2][1][1]:
            return 'H'
        elif cube[4][0][1] == cube[3][1][1] or cube[4][0][1] == cube[1][1][1]:
            return 'Z'

    @staticmethod
    def check_Z(cube):
        # right
        if cube[4][0][1] == cube[3][1][1]:
            return 1
        # wrong
        elif cube[4][0][1] == cube[1][1][1]:
            return 0

    def step(self, perm):
        return self.STEP[perm]

    def move_method(self, m, solution, cube):
        move = Rotation.Rotation()
        solution.append(m)
        move.move(m, cube)

    def solution(self, cube):
        solution = []

        # Ua or Ub
        if self.check_third_layer(cube) != 5:
            check = self.check_third_layer(cube)
            # 맞은 줄 위치
            if check == 4:
                self.move_method("Y", solution, cube)
                self.move_method("Y", solution, cube)
            elif check == 1:
                self.move_method("Y", solution, cube)
                self.move_method("Y", solution, cube)
                self.move_method("Y", solution, cube)
            elif check == 2:
                pass
            elif check == 3:
                self.move_method("Y", solution, cube)

            # Ua / Ub 판단
            if self.check_U_a_b(cube) == 'Ua':
                for m in self.step('Ua'):
                    self.move_method(m, solution, cube)
            elif self.check_U_a_b(cube) == 'Ub':
                for m in self.step('Ub'):
                    self.move_method(m, solution, cube)

        # Z or H
        elif self.check_third_layer(cube) == 5:
            # Z / H 판단
            if self.check_H_Z(cube) == 'H':
                for m in self.step('H'):
                    self.move_method(m, solution, cube)
            elif self.check_H_Z(cube) == 'Z':
                if self.check_Z(cube) == 1:
                    for m in self.step('Z'):
                        self.move_method(m, solution, cube)
                else:
                    self.move_method("Y", solution, cube)
                    for m in self.step('Z'):
                        self.move_method(m, solution, cube)

        # print("finish third layer corner")

        # Cube.print_cube(cube)

        return solution, cube
