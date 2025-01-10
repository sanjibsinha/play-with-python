class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self):
        # Simple enemy movement logic
        import random
        direction = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        self.x += direction[0]
        self.y += direction[1]

# end of file