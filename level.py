import random

class LevelManager:
    def __init__(self):
        self.level = 1

        self.levels = {
            1: {"speed": 4, "gap": 250, "base_dist": 700, "chaos": 0.0},
            2: {"speed": 5, "gap": 240, "base_dist": 600, "chaos": 0.0},
            3: {"speed": 6, "gap": 240, "base_dist": 500, "chaos": 0.1},
            4: {"speed": 6, "gap": 240, "base_dist": 400, "chaos": 0.2},
            5: {"speed": 6, "gap": 240, "base_dist": 360, "chaos": 0.3},
            6: {"speed": 6, "gap": 230, "base_dist": 340, "chaos": 0.3},
            7: {"speed": 7, "gap": 230, "base_dist": 340, "chaos": 0.4},
        }

        self.pipe_speed = 4
        self.pipe_gap = 230
        self.pipe_distance = 520

    def update(self, score):
        self.level = min(score // 10 + 1, 7)
        data = self.levels[self.level]

        self.pipe_speed = data["speed"]
        self.pipe_gap = data["gap"]

        # 🎲 KAOTİK X MESAFE
        if random.random() < data["chaos"]:
            self.pipe_distance = random.randint(180, data["base_dist"])
        else:
            self.pipe_distance = data["base_dist"]

    def should_spawn_pipe(self, last_pipe, screen_width):
        if last_pipe is None:
            return True
        return last_pipe.top.x < screen_width - self.pipe_distance

