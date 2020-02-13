from Cube import Rotation
import Block


class WhiteCrossSolver:

    STEPS = {
        'U': {
            'R': [],
            'L': [],
            'F': [],
            'B': []
        },
        'D': {
            'R': ['R2'],
            'L': ['L2'],
            'F': [],
            'B': ['B2']
        },
        'R': {
            'U': ["R'", "F'", "R"],
            'D': ["R", "F'"],
            'F': ["F'"],
            'B': ["B", "U", "B'"]
        },
        'L': {
            'U': ["L", "F", "L'"],
            'D': ["L'", "F"],
            'F': ["F"],
            'B': ["B'", "U", "B"]
        },
        'B':  {
            'U': ["B", "L", "U'", "L'", "B'"],
            'D': ["B", "R'", "U", "R"],
            'R': ["R'", "U", "R"],
            'L': ["L", "U'", "L'"]
        },
        'F': {
            'U': ["F", "R", "U", "R'"],
            'D': ["F", "L'", "U'", "L"],
            'R': ["R", "U", "R'"],
            'L': ["L'", "U'", "L"]
        }
    }

    def step(self, white_facing, color_facing):
        return self.STEPS[white_facing][color_facing]

    def solution(self, cube):
        move = Rotation.Rotation()
        solution = []
        for color in 'gobr':
            position = Block.find_edge(cube, 'w', color)    # (w, color) 위치

            if position is not 'DF':
                white_facing = Block.color_face(position, 0)
                color_facing = Block.color_face(position, 1)
                step_solution = self.step(white_facing, color_facing)

                for m in step_solution:
                    move.move(m, cube)
                solution.extend(step_solution)

                positions = Block.find_edge(cube, 'w', color)
                w_face = Block.color_face(positions, 0)
                c_face = Block.color_face(positions, 1)

                while w_face != 'U' or c_face != 'F':
                    solution.extend("U")
                    move.move("U", cube)
                    positions = Block.find_edge(cube, 'w', color)
                    w_face = Block.color_face(positions, 0)
                    c_face = Block.color_face(positions, 1)

                move.move('F2', cube)
                solution.append('F2')
            move.move('Y', cube)
            solution.extend('Y')

        # print("finish cross")

        # Cube.print_cube(cube)

        return solution, cube
