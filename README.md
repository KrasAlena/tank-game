# Tank Game
<img src="tank.png" width="40" height="40">

### Overview

This is a simple tank game implemented in Python using the command line interface.

### How to Play

1. Run the game by executing the Python script.
2. Comment this line in info() method:
```python
print(f'Target coordinates: {self.target_loc_x}, {self.target_loc_y}')
```

_________________
2.	Enter your name when prompted.
_________________
3.	Use the following commands to control the tank:

| Keyboard | Description              |
|----------|--------------------------|
| **l**    | Move the tank left       |
| **r**    | Move the tank right      |
| **f**    | Move the tank forward    |
| **b**    | Move the tank back       |
| **i**    | Display tank information |
| **sl**   | Steer the tank left      |
| **sr**   | Steer the tank right     |
| **sf**   | Steer the tank forward   |
| **sb**   | Steer the tank back      |
| **shot**   | Make a shot              |
| **print**   | Print game statistics   |

### Game Rules

- The tank starts with an initial score of **100**.
- Each movement (left, right, forward, back) reduces the score by **2**.
- Steering (sl, sr, sf, sb) reduces the score by **1**.
- The shot is fired at the nearest cell in the direction the tank is turning.
- A successful shot increases the score by **100**.
- Missing a target reduces the score by **10**.

### Winning and Losing

- The game ends when the player’s score drops to or below 0.
- At the end of the game, statistics are displayed, including the player’s name, targets hit, and total shots.

### Notes

> The game uses a 7x7 grid for the map.
> 
> The tank is represented by arrow symbol on the map. The direction of the arrow indicates the direction in which the tank is turning.

#### *Enjoy playing and try to achieve the highest score!*


