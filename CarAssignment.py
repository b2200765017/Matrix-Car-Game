def check(ipt):
    for num in ipt[1:]:
        if num.startswith("5_"):
            if int(num.split("_")[1]):
                continue
        if not 0 <= int(num) <= 8:
            return False
    return True


def matrix(N):
    global matris
    matris = [[0] * N for _ in range(N)]


def show(matris):
    print("+" * (N+2), end="")
    for x in matris:
        for y in range(len(x)):
            if x[y] == 0:
                x[y] = " "
            else:
                x[y] = "*"
        print("\n+", end="")
        for y in x:
            print(y, end="")
        print("+", end="")
    print("\n"+("+" * (N+2))+"\n", end="")


class vehicle:
    def __init__(self, brush, positionX, positionY, turn):
        self.positionX = positionX
        self.positionY = positionY
        self.brush = brush
        self.turn = turn

    def rotate(self, number):
        direction = ["right", "down", "left", "up"]
        if number == 3:
            if self.turn != direction[3]:
                self.turn = direction[direction.index(self.turn)+1]
            else:
                self.turn = direction[0]
        elif number == 4:
            if self.turn != direction[0]:
                self.turn = direction[direction.index(self.turn)-1]
            else:
                self.turn = direction[3]
        elif number == 7:
            if self.turn == direction[0] or self.turn == direction[1]:
                self.turn = direction[direction.index(self.turn)+2]
            else:
                self.turn = direction[direction.index(self.turn)-2]

    def move_right(self):
        if self.positionX+1 <= N - 1:
            if self.brush == 1:
                matris[self.positionY][self.positionX] = 1
            self.positionX += 1
        else:
            if self.brush == 1:
                matris[self.positionY][self.positionX] = 1
            self.positionX = 0

    def move_left(self):
        if self.positionX-1 >= 0:
            if self.brush == 1:matris[self.positionY][self.positionX] = 1
            self.positionX -=  1
        else:
            if self.brush == 1:matris[self.positionY][self.positionX] = 1
            self.positionX = N-1

    def move_up(self):
        if self.positionY-1 >= 0:
            if self.brush == 1:
                matris[self.positionY][self.positionX] = 1
            self.positionY -= 1
        else:
            if self.brush == 1:
                matris[self.positionY][self.positionX] = 1
            self.positionY = N-1

    def move_down(self):
        if self.positionY+1 <= N - 1:
            if self.brush == 1:
                matris[self.positionY][self.positionX] = 1
            self.positionY += 1
        else:
            if self.brush == 1:
                matris[self.positionY][self.positionX] = 1
            self.positionY = 0

    def move_up_toX(self, x):
        for time in range(x):
            if self.turn == "right":
                vehicle.move_right(self)
            elif self.turn == "left":
                vehicle.move_left(self)
            elif self.turn == "up":
                vehicle.move_up(self)
            elif self.turn == "down":
                vehicle.move_down(self)
        if self.brush == 1:
            matris[self.positionY][self.positionX] = 1

    def jump(self):
        if self.brush == 1:
            matris[self.positionY][self.positionX] = 1
        for time in range(3):
            if self.turn == "right":
                if self.positionX + 1 <= N - 1:
                    self.positionX += 1
                else:
                    self.positionX = 0
            elif self.turn == "left":
                if self.positionX - 1 >= 0:
                    self.positionX -= 1
                else:
                    self.positionX = N - 1
            elif self.turn == "up":
                if self.positionY - 1 >= 0:
                    self.positionY -= 1
                else:
                    self.positionY = N - 1
            elif self.turn == "down":
                if self.positionY + 1 <= N:
                    self.positionY += 1
                else:
                    self.positionY = 0
            self.brush = 0


def main():
    program = 1
    print("""<---------Rules-------->
1. BRUSH DOWN
2. BRUSH UP
3. VEHICLE ROTATES RIGHT
4. VEHICLE ROTATES LEFT
5. MOVE UP TO X
6. JUMP
7. REVERSE DIRECTION
8. VIEW THE MATRIX
0. EXIT""")
    while program == 1:
        global inpt
        inpt = input("Please enter the commands with a plus sign (+) between them.\n").split("+")
        while not check(inpt):
            inpt = input("You entered an incorrect command. Please try again!\n").split("+")
        car = vehicle(0, 0, 0, "right")
        global N
        N = int(inpt[0])
        matrix(N)
        for command in inpt[1:]:
            if str(command).startswith("5_"):
                command = command.split("_")
                car.move_up_toX(int(command[1]))
                continue
            command = int(command)
            if command == 1:
                car.brush = 1
            elif command == 2:
                car.brush = 0
            elif command == 3:
                car.rotate(3)
            elif command == 4:
                car.rotate(4)
            elif command == 6:
                car.jump()
            elif command == 7:
                car.rotate(7)
            elif command == 8:
                show(matris)
            elif command == 0:
                program = 0


main()
