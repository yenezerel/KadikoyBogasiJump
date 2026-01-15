import pygame

class Bird:
    def __init__(self, x, y, frames):
        self.x = x
        self.y = y
        self.vel = 0
        self.gravity = 0.4
        self.jump_power = -8
        self.frames = frames
        self.frame_index = 0
        self.image = self.frames[0]
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def jump(self):
        self.vel = self.jump_power

    def update(self):
        self.vel += self.gravity
        self.y += self.vel
        self.frame_index += 0.15
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]
        self.rect.center = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def out_of_bounds(self, height):
        return self.y < 0 or self.y > height
