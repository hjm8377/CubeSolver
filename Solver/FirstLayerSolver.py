from Cube import Rotation
import Block


class FirstLayerSolver:
    # DFL, DFR, BDL, BDR, BRU, BLU, FLU, FRU
    FIRST_STEP = {
        'DFL': ["L'", "U'", "L"],
        'DFR': ["R", "U", "R'", "U'"],
        'BDL': ["L", "U2", "L'"],
        'BDR': ["B", "U", "B'"],
        'BRU': ["U"],
        'BLU': ["U2"],
        'FLU': ["U'"],
        'FRU': []
    }

    SECOND_STEP = {
        'F': ["F'", "U'", "F"],
        'R': ["R", "U", "R'"],
        'U': ["R", "U2", "R'", "U'", "R", "U", "R'"]
    }

    def w_D(self, cube):
        if cube[5][0][2] is 'w':
            return 'D'
        return None

    def first_step(self, goal_cube):
        return self.FIRST_STEP[goal_cube]

    def second_step(self, white_face):
        return self.SECOND_STEP[white_face]

    def solution(self, cube):
        move = Rotation.Rotation()
        solution = []
        color_arr = "gobr"

        # 코너 조각 4개
        for i in range(4):
            front_color = color_arr[i % 4]
            right_color = color_arr[(i + 1) % 4]
            goal_cube = Block.find_corner(cube, 'w', front_color, right_color)
            w = self.w_D(cube)

            if goal_cube is 'DFR' and self.w_D(cube) is 'D':
                pass
            else:
                step_solution = self.first_step(goal_cube)

                for m in step_solution:
                    move.move(m, cube)

                if len(step_solution) > 0:
                    solution.extend(step_solution)

                w_face = Block.FRU_w(cube)
                step_solution = self.second_step(w_face)

                for mv in step_solution:
                    move.move(mv, cube)
                solution.extend(step_solution)

            solution.append('Y')
            move.move('Y', cube)

        # print("finish FirstLayer")

        return solution, cube