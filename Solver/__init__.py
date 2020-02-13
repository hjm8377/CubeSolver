import copy
from Solver import WhiteCrossSolver
from Solver import FirstLayerSolver
from Solver import SecondLayerSolver
from Solver import YellowCrossSolver
from Solver import YellowFaceSolver
from Solver import ThirdLayerCornerSolver
from Solver import ThirdLayerEdgeSolver
from Cube.Cube import solution_smoother, solution_minimize
from Cube import Rotation
from Cube.Cube import print_cube


# WhiteCross - FirstLayer - SecondLayer - YellowCross - YellowFace - ThirdLayer
class CubeSolver:
    def __init__(self, cube):
        self.cube = cube

    @staticmethod
    def move_method(m, solution, cube):
        move = Rotation.Rotation()
        solution.append(m)
        move.move(m, cube)

    def cube_init(self, solution, cube):
        while True:
            if cube[0][1][1] == 'y' and cube[2][1][1] == 'g':
                break

            if cube[0][1][1] == 'y' or cube[0][1][1] == 'w':
                while cube[2][1][1] != 'g':
                    self.move_method('Y', solution, cube)
                while cube[0][1][1] != 'y':
                    self.move_method('X', solution, cube)

            elif cube[0][1][1] == 'b' or cube[0][1][1] == 'g':
                while cube[2][1][1] != 'y':
                    self.move_method('Y', solution, cube)
                while cube[0][1][1] != 'y':
                    self.move_method('X', solution, cube)

            elif cube[0][1][1] == 'r' or cube[0][1][1] == 'o':
                if cube[0][1][1] == 'g' or 'y':
                    self.move_method('X', solution, cube)

    def solution(self):
        a = [0, 0, 0, 0, 0, 0, 0, 0]
        cube = copy.deepcopy(self.cube)

        # cube init
        sol = []
        self.cube_init(sol, cube)
        print("init : \n", sol)
        solution = sol
        a[0] = sol
        # print_cube(cube)

        sol, cube = WhiteCrossSolver.WhiteCrossSolver().solution(cube)
        # print("original \n", sol)
        sol = solution_minimize(sol)
        # print("minimize \n", sol)
        sol = solution_smoother(sol)
        print("white_cross_solution : \n", sol)
        solution += sol
        a[1] = sol
        # print_cube(cube)

        sol, cube = FirstLayerSolver.FirstLayerSolver().solution(cube)
        sol = solution_minimize(sol)
        sol = solution_smoother(sol)
        print("first_layer_solution : \n", sol)
        solution += sol
        a[2] = sol
        # print_cube(cube)

        sol, cube = SecondLayerSolver.SecondLayerSolver().solution(cube)
        sol = solution_minimize(sol)
        sol = solution_smoother(sol)
        print("second_layer_solution : \n", sol)
        solution += sol
        a[3] = sol
        # print_cube(cube)

        sol, cube = YellowCrossSolver.YellowCrossSolver().solution(cube)
        sol = solution_smoother(sol)
        print("yellow_cross_solution : \n", sol)
        solution += sol
        a[4] = sol
        # print_cube(cube)

        sol, cube = YellowFaceSolver.YellowFaceSolver().solution(cube)
        sol = solution_smoother(sol)
        print("yellow_face_solution : \n", sol)
        solution += sol
        a[5] = sol
        # print_cube(cube)

        sol, cube = ThirdLayerCornerSolver.ThirdLayerCornerSolver().solution(cube)
        sol = solution_smoother(sol)
        print("third_layer_corner_solution : \n", sol)
        solution += sol
        a[6] = sol
        # print_cube(cube)

        sol, cube = ThirdLayerEdgeSolver.ThirdLayerEdgeSolver().solution(cube)
        sol = solution_smoother(sol)
        print("third_layer_edge_solution : \n", sol)
        solution += sol
        a[7] = sol
        # print_cube(cube)

        print("Finish!!!")

        return solution, cube, a


def move_method(m, c):
    move = Rotation.Rotation()
    move.move(m, c)

"""
# CREATE CUBE 3 DIMENSION LIST 6*3*3
CUBE = [[[] for _ in range(3)]for _ in range(6)]

# init CUBE
s = 'yrgobw'    # U L F R B D   0 1 2 3 4 5
for i in range(6):
    for j in range(3):
        for _ in range(3):
            CUBE[i][j].append(s[i])

cube = copy.deepcopy(CUBE)

scramble3 = ["R", "U", "R'", "U'", "X"]

for m in scramble3:
    move_method(m, cube)

print_cube(cube)

solver = CubeSolver(cube)
solution, cube, step_sol = solver.solution()

print_cube(cube)
"""