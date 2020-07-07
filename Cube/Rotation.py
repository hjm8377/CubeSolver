class Rotation:
    @staticmethod
    def clockwise(arr):
        tmp = arr[0][0]
        arr[0][0] = arr[2][0]
        arr[2][0] = arr[2][2]
        arr[2][2] = arr[0][2]
        arr[0][2] = tmp

        tmp = arr[0][1]
        arr[0][1] = arr[1][0]
        arr[1][0] = arr[2][1]
        arr[2][1] = arr[1][2]
        arr[1][2] = tmp

    @staticmethod
    def count_clockwise(arr):
        tmp = arr[0][0]
        arr[0][0] = arr[0][2]
        arr[0][2] = arr[2][2]
        arr[2][2] = arr[2][0]
        arr[2][0] = tmp

        tmp = arr[0][1]
        arr[0][1] = arr[1][2]
        arr[1][2] = arr[2][1]
        arr[2][1] = arr[1][0]
        arr[1][0] = tmp

    @staticmethod
    def change_face(cube, i, j):
        # i면과 j면 맞바꾸기
        tmp = cube[i]
        cube[i] = cube[j]
        cube[j] = tmp

    @staticmethod
    def center_color(arr):
        return arr[1][1]

    @staticmethod
    def center_num(cube, color):
        for i in range(6):
            if cube[i][1][1] == color:
                return i

    def U(self, cube):
        self.clockwise(cube[0])
        tmp = cube[1][0][0], cube[1][0][1], cube[1][0][2]
        cube[1][0][0], cube[1][0][1], cube[1][0][2] = cube[2][0][0], cube[2][0][1], cube[2][0][2]
        cube[2][0][0], cube[2][0][1], cube[2][0][2] = cube[3][0][0], cube[3][0][1], cube[3][0][2]
        cube[3][0][0], cube[3][0][1], cube[3][0][2] = cube[4][0][0], cube[4][0][1], cube[4][0][2]
        cube[4][0][0], cube[4][0][1], cube[4][0][2] = tmp

    def D(self, cube):
        self.clockwise(cube[5])
        tmp = cube[1][2][0], cube[1][2][1], cube[1][2][2]
        cube[1][2][0], cube[1][2][1], cube[1][2][2] = cube[4][2][0], cube[4][2][1], cube[4][2][2]
        cube[4][2][0], cube[4][2][1], cube[4][2][2] = cube[3][2][0], cube[3][2][1], cube[3][2][2]
        cube[3][2][0], cube[3][2][1], cube[3][2][2] = cube[2][2][0], cube[2][2][1], cube[2][2][2]
        cube[2][2][0], cube[2][2][1], cube[2][2][2] = tmp

    def R(self, cube):
        self.clockwise(cube[3])
        tmp = cube[0][0][2], cube[0][1][2], cube[0][2][2]
        cube[0][0][2], cube[0][1][2], cube[0][2][2] = cube[2][0][2], cube[2][1][2], cube[2][2][2]
        cube[2][0][2], cube[2][1][2], cube[2][2][2] = cube[5][0][2], cube[5][1][2], cube[5][2][2]
        cube[5][0][2], cube[5][1][2], cube[5][2][2] = cube[4][2][0], cube[4][1][0], cube[4][0][0]
        cube[4][2][0], cube[4][1][0], cube[4][0][0] = tmp

    def L(self, cube):
        self.clockwise(cube[1])
        tmp = cube[0][0][0], cube[0][1][0], cube[0][2][0]
        cube[0][0][0], cube[0][1][0], cube[0][2][0] = cube[4][2][2], cube[4][1][2], cube[4][0][2]
        cube[4][2][2], cube[4][1][2], cube[4][0][2] = cube[5][0][0], cube[5][1][0], cube[5][2][0]
        cube[5][0][0], cube[5][1][0], cube[5][2][0] = cube[2][0][0], cube[2][1][0], cube[2][2][0]
        cube[2][0][0], cube[2][1][0], cube[2][2][0] = tmp

    def F(self, cube):
        self.clockwise(cube[2])
        tmp = cube[0][2][0], cube[0][2][1], cube[0][2][2]
        cube[0][2][0], cube[0][2][1], cube[0][2][2] = cube[1][2][2], cube[1][1][2], cube[1][0][2]
        cube[1][2][2], cube[1][1][2], cube[1][0][2] = cube[5][0][2], cube[5][0][1], cube[5][0][0]
        cube[5][0][2], cube[5][0][1], cube[5][0][0] = cube[3][0][0], cube[3][1][0], cube[3][2][0]
        cube[3][0][0], cube[3][1][0], cube[3][2][0] = tmp

    def B(self, cube):
        self.clockwise(cube[4])
        tmp = cube[0][0][0], cube[0][0][1], cube[0][0][2]
        cube[0][0][0], cube[0][0][1], cube[0][0][2] = cube[3][0][2], cube[3][1][2], cube[3][2][2]
        cube[3][0][2], cube[3][1][2], cube[3][2][2] = cube[5][2][2], cube[5][2][1], cube[5][2][0]
        cube[5][2][2], cube[5][2][1], cube[5][2][0] = cube[1][2][0], cube[1][1][0], cube[1][0][0]
        cube[1][2][0], cube[1][1][0], cube[1][0][0] = tmp

    def Y(self, cube):
        tmp = cube[1]
        cube[1] = cube[2]
        cube[2] = cube[3]
        cube[3] = cube[4]
        cube[4] = tmp
        self.clockwise(cube[0])
        self.count_clockwise(cube[5])

    def X(self, cube):
        tmp = cube[0]
        cube[0] = cube[2]
        cube[2] = cube[5]
        c = cube[4]
        for i in range(3):
            c[i] = list(reversed(c[i]))
        c = list(reversed(c))
        cube[5] = c
        c = tmp
        for i in range(3):
            c[i] = list(reversed(c[i]))
        c = list(reversed(c))
        cube[4] = c
        self.clockwise(cube[3])
        self.count_clockwise(cube[1])

    def R_(self, cube):
        for _ in range(3):
            self.R(cube)

    def L_(self, cube):
        for _ in range(3):
            self.L(cube)

    def U_(self, cube):
        for _ in range(3):
            self.U(cube)

    def D_(self, cube):
        for _ in range(3):
            self.D(cube)

    def F_(self, cube):
        for _ in range(3):
            self.F(cube)

    def B_(self, cube):
        for _ in range(3):
            self.B(cube)

    def Y_(self, cube):
        for _ in range(3):
            self.Y(cube)

    def twist(self, cube):
        self.R(cube)
        self.U(cube)
        self.R(cube)
        self.R(cube)
        self.R(cube)
        self.U(cube)
        self.U(cube)
        self.U(cube)

    def twist_all(self, cube):
        for _ in range(6):
            self.R(cube)
            self.U(cube)
            self.R(cube)
            self.R(cube)
            self.R(cube)
            self.U(cube)
            self.U(cube)
            self.U(cube)

    def move(self, m, cube):
        if m == "U":
            self.U(cube)
        elif m == "D":
            self.D(cube)
        elif m == "R":
            self.R(cube)
        elif m == "L":
            self.L(cube)
        elif m == "F":
            self.F(cube)
        elif m == "B":
            self.B(cube)

        elif m == "U'":
            self.U_(cube)
        elif m == "D'":
            self.D_(cube)
        elif m == "R'":
            self.R_(cube)
        elif m == "L'":
            self.L_(cube)
        elif m == "F'":
            self.F_(cube)
        elif m == "B'":
            self.B_(cube)

        elif m == "U2":
            self.U(cube)
            self.U(cube)
        elif m == "D2":
            self.D(cube)
            self.D(cube)
        elif m == "R2":
            self.R(cube)
            self.R(cube)
        elif m == "L2":
            self.L(cube)
            self.L(cube)
        elif m == "F2":
            self.F(cube)
            self.F(cube)
        elif m == "B2":
            self.B(cube)
            self.B(cube)

        elif m == "Y":
            self.Y(cube)
        elif m == "Y2":
            self.Y(cube)
            self.Y(cube)
        elif m == "Y'":
            self.Y_(cube)

        elif m == "X":
            self.X(cube)

        else:
            print("move error")
            exit(120)


def setface(CUBE):
    flag = [[[] for _ in range(3)] for _ in range(6)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                flag[i][j][k] = 0
    cube = CUBE
    
    print(cube)
