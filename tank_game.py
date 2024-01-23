class TankGame:
    def __init__(self, N: int = 7):
        """Create a tank game object.

        :param N: the size of the map (grid) NxN to generate for the game.
        """
        self.N = N
        # Hard-coded starting tank location is 2, 1
        self.tank_loc_x = 2
        self.tank_loc_y = 1
        self.tank_symbol = "⥥"

    def print_map(self):
        """Print the current map of the game.

        Example output for a 7x7 map:
           0  1  2  3  4  5  6
        0  .  .  .  .  .  .  .
        1  .  .  T  .  .  .  .
        2  .  .  .  .  .  .  .
        3  .  .  .  .  .  .  .
        4  .  .  .  .  .  .  .
        5  .  .  .  .  .  .  .
        6  .  .  .  .  .  .  .

        where T is the location of the tank,
        where . (the dot) is an empty space on the map,
        where the horizontal axis is the x location of the tank and,
        where the vertical axis is the y location of the tank.
        """
        # Print the numbers for the x axis
        print("   " + "  ".join([str(i) for i in range(self.N)]))

        for i in range(self.N):
            # Print the numbers for the y axis
            print(f'{i} ', end='')
            for j in range(self.N):
                if self.tank_loc_x == j and self.tank_loc_y == i:
                    print(f' {self.tank_symbol} ', end='')
                else:
                    print(" . ", end="")
            print()

    def left(self):
        self.tank_loc_x -= 1
        if self.tank_loc_x < 0:
            self.tank_loc_x = self.N - 1  # Move to the last point on the right
        self.tank_symbol = '⥢'
        return self.tank_loc_x

    def right(self):
        self.tank_loc_x += 1
        if self.tank_loc_x >= self.N:
            self.tank_loc_x = 0
        self.tank_symbol = '⥤'
        return self.tank_loc_x

    def back(self):
        self.tank_loc_y -= 1
        if self.tank_loc_y < 0:
            self.tank_loc_y = self.N - 1
        self.tank_symbol = '⥣'
        return self.tank_loc_y

    def forward(self):
        self.tank_loc_y += 1
        if self.tank_loc_y >= self.N:
            self.tank_loc_y = 0  # Move to the first point at the top
        self.tank_symbol = '⥥'
        return self.tank_loc_y

    def info(self):
        print(f'Current position: x = {self.tank_loc_x}, y = {self.tank_loc_y}\nShots amount: \n'
              f'Right shots: \nLeft shots: \nBack shots: \nForward shots: ')

    def steer_left(self):
        self.tank_symbol = '⥢'
        return

    def steer_right(self):
        self.tank_symbol = '⥤'
        return

    def steer_forward(self):
        self.tank_symbol = '⥥'
        return

    def steer_back(self):
        self.tank_symbol = '⥣'
        return

if __name__ == "__main__":
    # Initialize your game object
    tg = TankGame()
    # Start game loop
    while True:
        tg.print_map()

        command = input('Input a command: ')
        if command.lower() == 'l':
            tg.left()
            print('Tank moved left.')
        elif command.lower() == 'r':
            tg.right()
            print('Tank moved right.')
        elif command.lower() == 'f':
            tg.forward()
            print('Tank moved forward.')
        elif command.lower() == 'b':
            tg.back()
            print('Tank moved back.')
        elif command.lower() == 'i':
            tg.info()
        elif command.lower() == 'sl':
            tg.steer_left()
        elif command.lower() == 'sr':
            tg.steer_right()
        elif command.lower() == 'sf':
            tg.steer_forward()
        elif command.lower() == 'sb':
            tg.steer_back()


        # TODO: Implement handling of commands here

