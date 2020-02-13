from Cube import Rotation
import Block


class SecondLayerSolver:
    STEP = {
        'RF': ["R2", "U2", "F", "R2", "F'", "U2", "R'", "U", "R'"],
        'FR': [],

        'FU': ["U", "R", "U'", "R'", "U'", "F'", "U", "F"],
        'UF': ["U2", "F'", "U", "F", "U", "R", "U'", "R'"],

        'LF': ["F2", "U2", "F2", "U2", "F2", "R2", "U2", "F", "R2", "F'", "U2", "R'", "U", "R'"],
        'FL': ["F2", "U2", "F2", "U2", "F2"],

        'RU': ["U2", "R", "U'", "R'", "U'", "F'", "U", "F"],
        'UR': ["U'", "F'", "U", "F", "U", "R", "U'", "R'"],

        'BU': ["U2", "U", "R", "U'", "R'", "U'", "F'", "U", "F"],
        'UB': ["F'", "U", "F", "U", "R", "U'", "R'"],

        'LU': ["R", "U'", "R'", "U'", "F'", "U", "F"],
        'UL': ["U", "F'", "U", "F", "U", "R", "U'", "R'"],

        'BL': ["L", "U'", "L'", "U'", "B'", "U", "B", "U2", "F'", "U", "F", "U", "R", "U'", "R'"],
        'LB': ["L", "U'", "L'", "U'", "B'", "U", "B", "U", "R", "U'", "R'", "U'", "F'", "U", "F"],

        'BR': ["R2", "U2", "R2", "U2", "R2"],
        'RB': ["R2", "U2", "R2", "U2", "R2", "R2", "U2", "F", "R2", "F'", "U2", "R'", "U", "R'"]
    }

    def step(self, edge):
        return self.STEP[edge]

    def solution(self, cube):
        move = Rotation.Rotation()
        solution = []
        color_arr = "gobr"

        for i in range(4):
            front_color = color_arr[i % 4]
            right_color = color_arr[(i + 1) % 4]
            position = Block.find_edge(cube, front_color, right_color)

            if position == 'FR':
                move.move('Y', cube)
                solution.extend('Y')

            else:
                step_solution = self.step(position)

                for m in step_solution:
                    move.move(m, cube)
                    solution.append(m)

                move.move('Y', cube)
                solution.extend('Y')

        # print("finish SecondLayer")

        return solution, cube
