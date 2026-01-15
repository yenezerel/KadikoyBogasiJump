import random

class Pipe:
    def __init__(self, x, gap, speed, top_img, bottom_img, screen_height):
        self.speed = speed
        self.target_speed = speed
        self.scored = False

        center = random.randint(300, screen_height - 300)

        self.top = top_img.get_rect(midbottom=(x, center - gap // 2))
        self.bottom = bottom_img.get_rect(midtop=(x, center + gap // 2))

    def set_speed(self, speed):
        self.target_speed = speed

    def update(self):
        self.speed += (self.target_speed - self.speed) * 0.08
        self.top.x -= self.speed
        self.bottom.x -= self.speed

    def draw(self, screen, top_img, bottom_img):
        screen.blit(top_img, self.top)
        screen.blit(bottom_img, self.bottom)

    def off_screen(self):
        return self.top.right < 0
