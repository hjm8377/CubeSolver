from Cube import Rotation


class YellowCrossSolver:
    @staticmethod
    def yellow_cross_checker(cube):
        #    0
        #  1   3
        #    2
        y = 'y'
        a = ['y', 'y', 'y', 'y']
        a[0] = cube[0][0][1]
        a[1] = cube[0][1][0]
        a[2] = cube[0][2][1]
        a[3] = cube[0][1][2]

        #    y
        #  y   3
        #    2
        if a[0] == y and a[1] == y and a[2] != y and a[3] != y:
            return 1

        #    0
        #  y   3
        #    y
        elif a[0] != y and a[1] == y and a[2] == y and a[3] != y:
            return 2

        #    0
        #  1   y
        #    y
        elif a[0] != y and a[1] != y and a[2] == y and a[3] == y:
            return 3

        #    y
        #  1   y
        #    2
        elif a[0] == y and a[1] != y and a[2] != y and a[3] == y:
            return 4

        #    0
        #  y   y
        #    2
        elif a[0] != y and a[1] == y and a[2] != y and a[3] == y:
            return 5

        #    y
        #  1   3
        #    y
        elif a[0] == y and a[1] != y and a[2] == y and a[3] != y:
            return 6

        #    y
        #  y   y
        #    y
        elif a[0] == y and a[1] == y and a[2] == y and a[3] == y:
            return 7

        #    0
        #  1   3
        #    2
        else:
            return 0
    @staticmethod
    def twist_move():
        return ["R", "U", "R'", "U'"]

    def move_method(self, m, solution, cube):
        move = Rotation.Rotation()
        solution.append(m)
        move.move(m, cube)

    def solution(self, cube):
        solution = []
        twist = self.twist_move()
        checker = self.yellow_cross_checker(cube)

        if checker == 0:
            self.move_method("F", solution, cube)
            for m in twist:
                self.move_method(m, solution, cube)
            self.move_method("F'", solution, cube)
            self.move_method("U2", solution, cube)
            self.move_method("F", solution, cube)
            for m in twist:
                self.move_method(m, solution, cube)
            for m in twist:
                self.move_method(m, solution, cube)
            self.move_method("F'", solution, cube)

        elif checker == 1:
            self.move_method("F", solution, cube)
            for m in twist:
                self.move_method(m, solution, cube)
            for m in twist:
                self.move_method(m, solution, cube)
            self.move_method("F'", solution, cube)

        elif checker == 2:
            self.move_method("U", solution, cube)
            self.move_method("F", solution, cube)
            for m in twist:
                self.move_method(m, solution, cube)
            for m in twist:
                self.move_method(m, solution, cube)
            self.move_method("F'", solution, cube)

        elif checker == 3:
            self.move_method("U2", solution, cube)
            self.move_method("F", solution, cube)
            for m in twist:
                self.move_method(m, solution, cube)
            for m in twist:
                self.move_method(m, solution, cube)
            self.move_method("F'", solution, cube)

        elif checker == 4:
            self.move_method("U'", solution, cube)
            self.move_method("F", solution, cube)
            for m in twist:
                self.move_method(m, solution, cube)
            for m in twist:
                self.move_method(m, solution, cube)
            self.move_method("F'", solution, cube)

        elif checker == 5:
            self.move_method("F", solution, cube)
            for m in twist:
                self.move_method(m, solution, cube)
            self.move_method("F'", solution, cube)

        elif checker == 6:
            self.move_method("U", solution, cube)
            self.move_method("F", solution, cube)
            for m in twist:
                self.move_method(m, solution, cube)
            self.move_method("F'", solution, cube)

        elif checker == 7:
            pass

        # print("finish yellow cross")

        # Cube.print_cube(cube)

        return solution, cube
