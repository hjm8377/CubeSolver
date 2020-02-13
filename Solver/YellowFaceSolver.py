from Cube import Rotation
import copy


class YellowFaceSolver:

    #  0     1
    #     y
    #  3     2

    #  1    8  |  7    6  |  5    4  |  3    2
    #     L    |     F    |     R    |    B

    @staticmethod
    def yellow_face_checker(cube):
        y = 'y'
        y_face = [0, 0, 0, 0]
        y_face[0] = cube[0][0][0]
        y_face[1] = cube[0][0][2]
        y_face[2] = cube[0][2][2]
        y_face[3] = cube[0][2][0]

        face = [0, 0, 0, 0, 0, 0, 0, 0]
        face[0] = copy.deepcopy(cube[1][0][0])
        face[1] = copy.deepcopy(cube[4][0][2])
        face[2] = copy.deepcopy(cube[4][0][0])
        face[3] = copy.deepcopy(cube[3][0][2])
        face[4] = copy.deepcopy(cube[3][0][0])
        face[5] = copy.deepcopy(cube[2][0][2])
        face[6] = copy.deepcopy(cube[2][0][0])
        face[7] = copy.deepcopy(cube[1][0][2])

        if y_face[0] != y and y_face[1] != y and y_face[2] != y and y_face[3] != y:
            if face[1] == y and face[2] == y and face[5] == y and face[6] == y:
                return 49
            if face[0] == y and face[2] == y and face[5] == y and face[7] == y:
                return 50
            else:
                return 0

        elif y_face[0] != y and y_face[1] != y and y_face[2] == y and y_face[3] == y:
            if face[1] == y and face[2] == y:
                return 51
            else:
                return 0

        elif y_face[0] != y and y_face[1] == y and y_face[2] == y and y_face[3] != y:
            if face[1] == y and face[6] == y:
                return 52
            else:
                return 0

        elif y_face[0] == y and y_face[1] != y and y_face[2] == y and y_face[3] != y:
            if face[3] == y and face[6] == y:
                return 53
            else:
                return 0

        elif y_face[0] == y and y_face[1] != y and y_face[2] != y and y_face[3] != y:
            if face[2] == y and face[4] == y and face[6] == y:
                return 54
            else:
                return 0

        elif y_face[0] != y and y_face[1] != y and y_face[2] != y and y_face[3] == y:
            if face[1] == y and face[3] == y and face[5] == y:
                return 55
            else:
                return 0

        elif y_face[0] == y and y_face[1] == y and y_face[2] == y and y_face[3] == y :
            return None

        else:
            return 0

    @staticmethod
    def OLL(num):
        if num == 49:
            return ["R", "U2", "R'", "U'", "R", "U", "R'", "U'", "R", "U'", "R'"]
        elif num == 50:
            return ["R", "U2", "R2", "U'", "R2", "U'", "R2", "U2", "R"]
        elif num == 51:
            return ["R2", "D'", "R", "U2", "R'", "D", "R", "U2", "R"]
        elif num == 52:
            return ["F", "R", "F'", "L", "F", "R'", "F'", "L'"]
        elif num == 53:
            return ["F", "R'", "F'", "L", "F", "R", "F'", "L'"]
        elif num == 54:
            return ["R'", "U'", "R", "U'", "R'", "U2", "R"]
        elif num == 55:
            return ["R", "U", "R'", "U", "R", "U2", "R'"]
        else:
            exit("Yellow Face Solver Error")

    def move_method(self, m, solution, cube):
        move = Rotation.Rotation()
        solution.append(m)
        move.move(m, cube)

    def solution(self, cube):
        move = Rotation.Rotation()
        solution = []
        a = self.yellow_face_checker(cube)

        while True:
            if self.yellow_face_checker(cube) == 0:
                self.move_method("U", solution, cube)
            else:
                break

        if self.yellow_face_checker(cube) is not None:
            OLL = self.OLL(self.yellow_face_checker(cube))

            for m in OLL:
                self.move_method(m, solution, cube)

        # print("finish yellow face")

        # Cube.print_cube(cube)

        return solution, cube
