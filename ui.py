import pygame

def draw_start_box(screen, highscore, width, height):
    box_w, box_h = 270, 105
    box_x = width//2 - box_w//2 + 7
    box_y = height - box_h - 130
    pygame.draw.rect(screen, (224,209,191), (box_x, box_y, box_w, box_h), border_radius=15)
    pygame.draw.rect(screen, (44,48,61), (box_x, box_y, box_w, box_h), width=6, border_radius=15)
    font = pygame.font.Font(None, 36)
    t_high = font.render(f"En Yüksek Skor: {highscore}", True, (44,48,61))
    t_space = font.render("Başlamak için SPACE", True, (44,48,61))
    screen.blit(t_high, (box_x + box_w//2 - t_high.get_width()//2, box_y + 20))
    screen.blit(t_space, (box_x + box_w//2 - t_space.get_width()//2, box_y + 57))

def draw_gameover_box(screen, score, highscore, level, width, height):
    box_w, box_h = 270, 120
    box_x = width//2 - box_w//2 + 7
    box_y = height - box_h - 115
    pygame.draw.rect(screen, (250,205,35), (box_x, box_y, box_w, box_h), border_radius=15)
    pygame.draw.rect(screen, (20,25,28), (box_x, box_y, box_w, box_h), width=2, border_radius=15)
    font = pygame.font.Font(None, 36)
    t_score = font.render(f"Skor: {score}", True, (35,52,88))
    t_high = font.render(f"En Yüksek Skor: {highscore}", True, (35,52,88))
    t_space = font.render("Başlamak için SPACE", True, (35,52,88))
    screen.blit(t_score, (box_x + box_w//2 - t_score.get_width()//2, box_y + 10))
    screen.blit(t_high, (box_x + box_w//2 - t_high.get_width()//2, box_y + 47))
    screen.blit(t_space, (box_x + box_w//2 - t_space.get_width()//2, box_y + 84))

def draw_score_box(screen, score, highscore, level):
    box_w, box_h = 125, 70
    box_x, box_y = 10, 10
    pygame.draw.rect(screen, (239,229,218), (box_x, box_y, box_w, box_h), border_radius=12)
    pygame.draw.rect(screen, (53,57,64), (box_x, box_y, box_w, box_h), width=3, border_radius=12)
    font = pygame.font.Font(None, 36)
    t_score = font.render(f"Skor: {score}", True, (51,51,56))
    t_level = font.render(f"Level: {level}", True, (51,51,56)) 
    screen.blit(t_score, (box_x +17, box_y + 10))
    screen.blit(t_level, (box_x + 15, box_y + 35))

def draw_pause_box(screen, width, height):
    box_w, box_h = 260, 65
    box_x = width//2 - box_w//2 -60
    box_y = height//2 - box_h//2 +105
    pygame.draw.rect(screen, (220,207,189), (box_x, box_y, box_w, box_h), border_radius=15)
    font = pygame.font.Font(None, 34)
    t_pause = font.render("PAUSE", True, (51,51,56))
    t_pauseDev = font.render("ESC veya P ile Devam", True, (51,51,56))
    screen.blit(t_pause, (box_x + 100, box_y + 10))
    screen.blit(t_pauseDev, (box_x + 10, box_y + 40))
