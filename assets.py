import pygame
import os
import sys

def resource_path(relative_path):
    """PyInstaller ile exe yapıldığında dosya yolunu ayarlar"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def load_image(path, size=None):
    """Image yükler ve boyutlandırır"""
    img = pygame.image.load(resource_path(path)).convert_alpha()
    if size:
        img = pygame.transform.smoothscale(img, size)
    return img

def load_sound(path):
    """Sound yükler"""
    return resource_path(path)  # sound path string olarak dönüyor, SoundManager içinde pygame.mixer.Sound ile açılacak
