from Cube import Rotation
import copy
from Cube import Rotation
from Cube.Cube import print_cube
import Solver


def move_method(m, c):
    move = Rotation.Rotation()
    move.move(m, c)


# CREATE CUBE 3 DIMENSION LIST 6*3*3
CUBE = [[[] for _ in range(3)]for _ in range(6)]

# init CUBE
s = 'yrgobw'    # U L F R B D   0 1 2 3 4 5
for i in range(6):
    for j in range(3):
        for _ in range(3):
            CUBE[i][j].append(s[i])

cube = copy.deepcopy(CUBE)

scramble1 = ["R2", "B2", "D2", "U2", "R2", "D2", "F2", "B'", "D2", "F", "B'", "D2", "F", "R'", "F", "B'", "D", "L", "D2",
             "U", "F'", "L2", "U'", "R2", "D", "X", "X", "Y", "Y"]

scramble2 = ["B'", "F", "U2", "B2", "F", "L2", "B", "L2", "D'", "U'", "L", "R", "D2", "L'", "D", "B2", "F", "R2", "B2",
             "L2", "B", "F", "U", "L2", "R", "D'", "L2", "R'", "D'", "R"]

scramble3 = ["R", "U", "R'", "U'", "L'", "U'", "L", "U", "B", "B'"]

for m in scramble3:
    move_method(m, cube)

# cube = [[['y', 'w', 'w'], ['b', 'b', 'r'], ['y', 'o', 'w']], [['g', 'y', 'o'], ['b', 'y', 'y'], ['b', 'o', 'b']], [['b', 'y', 'r'], ['g', 'o', 'b'], ['y', 'w', 'o']], [['b', 'y', 'o'], ['o', 'w', 'g'], ['g', 'r', 'w']], [['g', 'g', 'r'], ['r', 'r', 'w'], ['r', 'r', 'o']], [['r', 'o', 'y'], ['g', 'g', 'b'], ['w', 'w', 'g']]]
cube = [[['b', 'r', 'g'], ['b', 'y', 'y'], ['r', 'w', 'g']], [['w', 'r', 'y'], ['b', 'r', 'w'], ['w', 'y', 'w']], [['b', 'r', 'o'], ['g', 'g', 'r'], ['b', 'g', 'y']], [['y', 'o', 'r'], ['y', 'o', 'w'], ['g', 'b', 'b']], [['w', 'g', 'o'], ['o', 'b', 'w'], ['o', 'y', 'o']], [['r', 'o', 'r'], ['g', 'w', 'o'], ['g', 'b', 'y']]]
print_cube(cube)

solver = Solver.CubeSolver(cube)
sol, cube, step_sol = solver.solution()

print_cube(cube)
print(sol)



def solution_normalize():
    for i in range(len(sol)):
        if len(sol[i]) == 1:
            sol[i] += 'o'

    s = ''.join(sol)
    s = s.replace("'", "p")
    s = s.replace("2", "t")
