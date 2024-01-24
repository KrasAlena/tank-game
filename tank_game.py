import random
from tabulate import tabulate
class TankGame:
    def __init__(self, N: int = 7, initial_score: int = 100):
        """Create a tank game object.

        :param N: the size of the map (grid) NxN to generate for the game.
        """
        self.N = N
        # Hard-coded starting tank location is 2, 1
        self.tank_loc_x = 2
        self.tank_loc_y = 1
        self.tank_symbol = "⥥"
        self.shots = {'left': 0, 'right': 0, 'forward': 0, 'back': 0}
        self.target_loc_x, self.target_loc_y = self.generate_target_location()
        self.player_score = initial_score
        self.target_hit = 0

    def generate_target_location(self):
        while True:
            target_x = random.randint(0, self.N - 1)
            target_y = random.randint(0, self.N - 1)

            if (target_x, target_y) != (self.tank_loc_x, self.tank_loc_y):
                return target_x, target_y

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
                    print(' . ', end='')
            print()
        print(f'SCORE: {self.player_score}')

    def left(self):
        self.tank_loc_x -= 1
        if self.tank_loc_x < 0:
            self.tank_loc_x = self.N - 1  # Move to the last point on the right
        self.tank_symbol = '⥢'
        self.print_map()
        return self.tank_loc_x

    def right(self):
        self.tank_loc_x += 1
        if self.tank_loc_x >= self.N:
            self.tank_loc_x = 0
        self.tank_symbol = '⥤'
        self.print_map()
        return self.tank_loc_x

    def back(self):
        self.tank_loc_y -= 1
        if self.tank_loc_y < 0:
            self.tank_loc_y = self.N - 1
        self.tank_symbol = '⥣'
        self.print_map()
        return self.tank_loc_y

    def forward(self):
        self.tank_loc_y += 1
        if self.tank_loc_y >= self.N:
            self.tank_loc_y = 0  # Move to the first point at the top
        self.tank_symbol = '⥥'
        self.print_map()
        return self.tank_loc_y

    def info(self):
        print(f'Tank direction: {self.get_tank_direction()}')
        print(f'Tank coordinates: ({self.tank_loc_x}, {self.tank_loc_y})')
        print(f'Total shots: {sum(self.shots.values())}')
        for direction, count in self.shots.items():
            print(f'Shots {direction}: {count}')
        print(f'Target coordinates: {self.target_loc_x}, {self.target_loc_y}')

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

    def shot(self):
        # Increment the count of shots in the tank's current direction
        self.shots[self.get_tank_direction()] += 1

        shot_positions = self.get_shot_positions()
        if (self.target_loc_x, self.target_loc_y) in shot_positions:
            print('Hit!')
            self.target_hit += 1
            self.player_score += 100
            self.generate_target_location()
        else:
            print('Oops..')
            self.player_score -= 10



    def get_tank_direction(self):
        # Determine the tank's current direction based on its symbol
        if self.tank_symbol == '⥤':
            return 'right'
        elif self.tank_symbol == '⥢':
            return 'left'
        elif self.tank_symbol == '⥥':
            return 'forward'
        elif self.tank_symbol == '⥣':
            return 'back'

    def get_shot_positions(self):
        # Return the positions where shots occurred based on the tank's current direction
        direction = self.get_tank_direction()

        if direction == 'left':
            return [(self.tank_loc_x - i, self.tank_loc_y) for i in range(1, self.shots[direction] + 1) if
                    (self.tank_loc_x - i) >= 0]
        elif direction == 'right':
            return [(self.tank_loc_x + i, self.tank_loc_y) for i in range(1, self.shots[direction] + 1) if
                    (self.tank_loc_x + i) < self.N]
        elif direction == 'forward':
            return [(self.tank_loc_x, self.tank_loc_y + i) for i in range(1, self.shots[direction] + 1) if
                    (self.tank_loc_y - i) >= 0]
        elif direction == 'back':
            return [(self.tank_loc_x, self.tank_loc_y - i) for i in range(1, self.shots[direction] + 1) if
                    (self.tank_loc_y + i) < self.N]


    def print_stats(self):
        stats_data = [
            # ['Player', self.player_name],
            ['Targets hit', self.target_hit],
            ['Total shots', sum(self.shots.values())]
        ]
        print(tabulate(stats_data, headers=['Stat', 'Value'], tablefmt='pretty'))


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
        elif command.lower() == "shot":
            tg.shot()
        elif command.lower() == 'print':
            tg.print_stats()




