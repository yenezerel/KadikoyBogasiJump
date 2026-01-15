# sound.py
import pygame
import sys
import os

def resource_path(relative_path):
    """PyInstaller için path düzeltme"""
    try:
        base_path = sys._MEIPASS  # EXE için geçerli
    except AttributeError:
        base_path = os.path.abspath(".")  # VSC için geçerli
    return os.path.join(base_path, relative_path)

class SoundManager:
    def handle_event(self, event):
        """
        pygame.event ile gelen custom eventleri işleyebilir.
        Örneğin new_record çalındıktan sonra background sesini geri açmak için.
        """
        if event.type == pygame.USEREVENT+1:
            self.bg_channel.set_volume(self.bg_volume)
            pygame.time.set_timer(pygame.USEREVENT+1, 0)
            
    def __init__(self, bg_path, pause_path, new_record_path, level_up_path):
        pygame.mixer.init()
        self.bg_channel = pygame.mixer.Channel(0)
        self.effect_channel = pygame.mixer.Channel(1)
        self.level_channel = pygame.mixer.Channel(2)
        self.pause_channel = pygame.mixer.Channel(3)
        self.bg_volume = 0.5

        # Tüm sesler resource_path ile yükleniyor
        self.bg_music = pygame.mixer.Sound(resource_path(bg_path))
        self.pause_sound = pygame.mixer.Sound(resource_path(pause_path))
        self.new_record_sound = pygame.mixer.Sound(resource_path(new_record_path))
        self.level_up_sound = pygame.mixer.Sound(resource_path(level_up_path))

    def play_background(self, force=False):
        if force or not self.bg_channel.get_busy():
            self.bg_channel.stop()
            self.bg_channel.set_volume(self.bg_volume)
            self.bg_channel.play(self.bg_music, loops=-1)

    def pause_background(self):
        self.bg_channel.pause()
        if not self.pause_channel.get_busy():
            self.pause_channel.play(self.pause_sound, loops=-1)

    def resume_background(self):
        self.pause_channel.stop()
        self.bg_channel.unpause()

    def play_jump(self, jump_sound_path):
        jump_sound = pygame.mixer.Sound(resource_path(jump_sound_path))
        self.effect_channel.play(jump_sound)

    def play_hit(self, hit_sound_path):
        hit_sound = pygame.mixer.Sound(resource_path(hit_sound_path))
        self.effect_channel.play(hit_sound)

    def play_new_record(self):
        self.bg_channel.set_volume(self.bg_volume * 0.3)
        self.effect_channel.play(self.new_record_sound)

    def play_level_up(self):
        self.level_channel.play(self.level_up_sound)

    def stop_pause(self):
        self.pause_channel.stop()

    def reset_sounds(self):
        self.bg_channel.stop()
        self.effect_channel.stop()
        self.level_channel.stop()
        self.pause_channel.stop()
        self.bg_channel.set_volume(self.bg_volume)
