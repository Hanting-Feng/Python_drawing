import random
from idlelib.configdialog import changes

import pygame
win_width = 530
win_height = 880
font_px = 15
pygame.init()
winsur = pygame.display.set_mode((win_width,win_height))
font = pygame.font.SysFont('',23)
bg_suface = pygame.Surface((win_width,win_height), flags = pygame.SRCALPHA)
pygame.Surface.convert(bg_suface)
bg_suface.fill(pygame.Color(0,0,0,28))
winsur.fill((0,0,0))
letter = '0123456789'
texts = [font.render(letter[i],True, (0,255,0)) for i in range(10)]
column = int(win_width / font_px)
drops = [0 for i in range(column)]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            change = pygame.key.get_pressed()
            if change[32]:
                exit()
    pygame.time.delay(30)
    winsur.blit(bg_suface,(0,0))
    for i in range(len(drops)):
        text = random.choice(texts)
        winsur.blit(text,(i * font_px, drops[i] * font_px))
        drops[i] += 1
        if drops[i] * 10 > win_height or random.random() > 0.95:
            drops[i] = 0
    pygame.display.flip()