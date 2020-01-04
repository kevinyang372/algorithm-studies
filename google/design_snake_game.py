# Design a Snake game that is played on a device with screen size = width x height. Play the game online if you are not familiar with the game.

# The snake is initially positioned at the top left corner (0,0) with length = 1 unit.

# You are given a list of food's positions in row-column order. When a snake eats the food, its length and the game's score both increase by 1.

# Each food appears one by one on the screen. For example, the second food will not appear until the first food was eaten by the snake.

# When a food does appear on the screen, it is guaranteed that it will not appear on a block occupied by the snake.

# Example:

# Given width = 3, height = 2, and food = [[1,2],[0,1]].

# Snake snake = new Snake(width, height, food);

# Initially the snake appears at position (0,0) and the food at (1,2).

# |S| | |
# | | |F|

# snake.move("R"); -> Returns 0

# | |S| |
# | | |F|

# snake.move("D"); -> Returns 0

# | | | |
# | |S|F|

# snake.move("R"); -> Returns 1 (Snake eats the first food and right after that, the second food appears at (0,1) )

# | |F| |
# | |S|S|

# snake.move("U"); -> Returns 1

# | |F|S|
# | | |S|

# snake.move("L"); -> Returns 2 (Snake eats the second food)

# | |S|S|
# | | |S|

# snake.move("U"); -> Returns -1 (Game over because snake collides with border)

class SnakeGame(object):

    def __init__(self, width, height, food):
        self.score = 0
        self.width = width
        self.height = height
        
        self.x = self.y = 0
        self.food = food[::-1]
        self.snake = collections.deque([(0, 0)])
        self.p = set([(0, 0)])
        

    def move(self, direction):
        if direction == 'U':
            dx, dy = -1, 0
        elif direction == 'R':
            dx, dy = 0, 1
        elif direction == 'D':
            dx, dy = 1, 0
        else:
            dx, dy = 0, -1
        
        if 0 <= self.x + dx < self.height and 0 <= self.y + dy < self.width:
            last = self.snake.popleft()
            self.p.remove(last)
            
            if (self.x + dx, self.y + dy) in self.p: return -1
            
            self.snake.append((self.x + dx, self.y + dy))
            self.p.add((self.x + dx, self.y + dy))
            
            if self.food and (self.x + dx, self.y + dy) == tuple(self.food[-1]):
                self.food.pop()
                self.score += 1
                
                self.snake.appendleft(last)
                self.p.add(last)
                
            self.x, self.y = self.x + dx, self.y + dy
            return self.score
                
        return -1