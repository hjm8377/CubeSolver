from Cube import Rotation


class ThirdLayerCornerSolver:
    @staticmethod
    def corner_checker(cube):
        face = [0, 0, 0, 0, 0, 0, 0, 0]
        face[0] = cube[1][0][0]
        face[1] = cube[4][0][2]
        face[2] = cube[4][0][0]
        face[3] = cube[3][0][2]
        face[4] = cube[3][0][0]
        face[5] = cube[2][0][2]
        face[6] = cube[2][0][0]
        face[7] = cube[1][0][2]

        for i in range(4):
            if face[1] == face[2] and face[3] == face[4] and face[5] == face[6] and face[7] == face[0]:
                return None
            if face[i * 2 + 1] == face[(i * 2 + 2) % 8]:
                return i * 2 + 1

        return 9


    def search_color(self, num, cube):
        face = [0, 0, 0, 0, 0, 0, 0, 0]
        face[0] = cube[1][0][0]
        face[1] = cube[4][0][2]
        face[2] = cube[4][0][0]
        face[3] = cube[3][0][2]
        face[4] = cube[3][0][0]
        face[5] = cube[2][0][2]
        face[6] = cube[2][0][0]
        face[7] = cube[1][0][2]

        return face[num]

    @staticmethod
    def basic_move():
        return ["R", "U2", "R'", "U'", "R", "U2", "L'", "U", "R'", "U'", "L"]

    def move_method(self, m, solution, cube):
        move = Rotation.Rotation()
        solution.append(m)
        move.move(m, cube)

    def orientation(self, solution, cube):
        if self.corner_checker(cube) == 1:
            self.move_method("U'", solution, cube)
        elif self.corner_checker(cube) == 3:
            self.move_method("U2", solution, cube)
        elif self.corner_checker(cube) == 5:
            self.move_method("U", solution, cube)
        else:
            pass

    def solution(self, cube):
        solution = []

        if self.corner_checker(cube) is None:
            pass
        elif self.corner_checker(cube) is 9:
            for m in ["F", "R", "U'", "R'", "U'", "R", "U", "R'", "F'", "R", "U", "R'", "U'", "R'", "F", "R", "F'"]:
                self.move_method(m, solution, cube)

        else:
            self.orientation(solution, cube)
            for m in self.basic_move():
                self.move_method(m, solution, cube)

        if self.search_color(0, cube) == 'g':
            self.move_method("U'", solution, cube)
        elif self.search_color(0, cube) == 'o':
            self.move_method("U2", solution, cube)
        elif self.search_color(0, cube) == 'b':
            self.move_method("U", solution, cube)
        else:
            pass

        # print("finish third layer corner")

        # Cube.print_cube(cube)

        return solution, cube
