class Ground:
    def __init__(self, img, y, speed, width):
        self.img = img
        self.y = y
        self.speed = speed
        self.x1 = 0
        self.x2 = width

    def update(self):
        self.x1 -= self.speed
        self.x2 -= self.speed
        if self.x1 <= -self.img.get_width():
            self.x1 = self.x2 + self.img.get_width()
        if self.x2 <= -self.img.get_width():
            self.x2 = self.x1 + self.img.get_width()

    def draw(self, screen):
        screen.blit(self.img, (self.x1, self.y))
        screen.blit(self.img, (self.x2, self.y))
