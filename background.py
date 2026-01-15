class Background:
    def __init__(self, img, speed, width):
        self.img = img

    def update(self):
        pass  # arkaplan SABİT

    def draw(self, screen):
        screen.blit(self.img, (0, 0))
