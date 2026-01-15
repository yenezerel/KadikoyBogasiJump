import pygame, sys
from assets import load_image, load_sound
from bird import Bird
from pipe import Pipe
from background import Background
from ground import Ground
from level import LevelManager
from score import load_highscore, save_highscore, reset_highscore
from sound import SoundManager
from ui import draw_start_box, draw_gameover_box, draw_score_box, draw_pause_box

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 1200, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("KADIKÖY BOĞASI")
CLOCK = pygame.time.Clock()
FPS = 60

# ================== ASSETS ==================
bg_img = load_image("images/arkaplan.jpg", (WIDTH, HEIGHT))
giris_bg = load_image("images/giris.png", (WIDTH, HEIGHT))
bird_frames = [load_image("images/bird.png", (50, 50))]
pipe_img = load_image("images/pipe.png", (120, 500))
pipe_top_img = pygame.transform.flip(pipe_img, False, True)
ground_img = load_image("images/ground.png", (1200, 80))
win_bg = load_image("images/istebu.png", (WIDTH, HEIGHT))
lose_bg = load_image("images/hayir.png", (WIDTH, HEIGHT))
pause_bg = load_image("images/pause.png", (WIDTH, HEIGHT))

jump_sound_path = "effect/jump.wav"
hit_sound_path = "effect/hit.wav"

# ================== OBJECTS ==================
bird = Bird(200, HEIGHT//2, bird_frames)
ground = Ground(ground_img, HEIGHT-80, 3, 1200)
background = Background(bg_img, 1, WIDTH)
level_manager = LevelManager()
sound_manager = SoundManager(
    "effect/background.wav",
    "effect/pause.wav",
    "effect/new_record.wav",
    "effect/level_up.wav"
)

pipes = []
score = 0
highscore = load_highscore()
new_record_played = False

# ================== GAME STATE ==================
START, PLAY, PAUSE, GAME_OVER = 0,1,2,3
state = START

# ================== RESET ==================
def reset_game():
    global bird, pipes, score, state, new_record_played
    bird.y = HEIGHT//2
    bird.vel = 0
    pipes.clear()
    score = 0
    state = START
    new_record_played = False
    sound_manager.reset_sounds()
    sound_manager.play_background(force=True)

# ================== MAIN LOOP ==================
while True:
    for event in pygame.event.get():
        sound_manager.handle_event(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if state == START and event.key == pygame.K_SPACE:
                state = PLAY
                sound_manager.play_background(force=True)

            elif state == PLAY:
                if event.key == pygame.K_SPACE:
                    bird.jump()
                    sound_manager.play_jump(jump_sound_path)
                elif event.key in [pygame.K_ESCAPE, pygame.K_p]:
                    state = PAUSE
                    sound_manager.pause_background()

            elif state == PAUSE:
                if event.key in [pygame.K_ESCAPE, pygame.K_p]:
                    state = PLAY
                    sound_manager.resume_background()

            elif state == GAME_OVER and event.key == pygame.K_SPACE:
                reset_game()

            elif event.key == pygame.K_r:  # highscore reset
                reset_highscore()
                highscore = 0

    SCREEN.fill((0,0,0))

    if state in [PLAY, PAUSE]:
        background.update()
        background.draw(SCREEN)
        ground.update()
        ground.draw(SCREEN)

    if state == PLAY:
        bird.update()
        bird.draw(SCREEN)
        level_manager.update(score)
        pipe_speed = level_manager.pipe_speed
        pipe_gap = level_manager.pipe_gap

        if level_manager.should_spawn_pipe(pipes[-1] if pipes else None, WIDTH):
            pipes.append(
                Pipe(WIDTH + 50, pipe_gap, pipe_speed, pipe_top_img, pipe_img, HEIGHT)
            )

        for p in pipes:
            p.set_speed(level_manager.pipe_speed)
            p.update()
            p.draw(SCREEN, pipe_top_img, pipe_img)

            if not p.scored and p.top.right < bird.x:
                p.scored = True
                score += 1
                if score == max(highscore - 2, 1):
                    sound_manager.play_level_up()

        pipes = [p for p in pipes if not p.off_screen()]

        # Çarpışma
        hit = False
        for p in pipes:
            if bird.rect.colliderect(p.top) or bird.rect.colliderect(p.bottom):
                hit = True
        if bird.out_of_bounds(HEIGHT):
            hit = True

        if hit:
            sound_manager.stop_pause()
            is_new_record = save_highscore(score)  # highscore güncellendi mi?
            state = GAME_OVER
            new_record_played = False

        draw_score_box(SCREEN, score, highscore, level_manager.level)

    elif state == START:
        highscore = load_highscore()
        SCREEN.blit(giris_bg, (0,0))
        draw_start_box(SCREEN, highscore, WIDTH, HEIGHT)

    elif state == GAME_OVER:
        if score > highscore:
            SCREEN.blit(win_bg, (0,0))
            if not new_record_played:
                sound_manager.play_new_record()
                new_record_played = True
        else:
            SCREEN.blit(lose_bg, (0,0))
            if not new_record_played:
                sound_manager.play_hit(hit_sound_path)
                new_record_played = True

        draw_gameover_box(SCREEN, score, highscore, level_manager.level, WIDTH, HEIGHT)

    elif state == PAUSE:
        bird.draw(SCREEN)
        for p in pipes:
            SCREEN.blit(pause_bg, (0,0))
        draw_score_box(SCREEN, score, highscore, level_manager.level)
        draw_pause_box(SCREEN, WIDTH, HEIGHT)

    pygame.display.update()
    CLOCK.tick(FPS)
