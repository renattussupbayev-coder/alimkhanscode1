import pygame
import random
import math

pygame.init()

# -------------------
# НАСТРОЙКИ
# -------------------
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Boss Levels Game")

clock = pygame.time.Clock()

# -------------------
# ИГРОК
# -------------------
player = pygame.Rect(450, 500, 40, 40)
player_speed = 5

bullets = []

# -------------------
# УРОВНИ БОССОВ
# -------------------
bosses = [
    ("Rats", 30),
    ("Eagle", 50),
    ("Lion", 80),
    ("Gorilla", 120),
    ("Crocodile", 160),
    ("Rhino", 220),
    ("Elephant", 280),
    ("Mammoth", 350),
    ("T-Rex", 500),
    ("Brachiosaurus", 700),
]

level = 0

boss = pygame.Rect(400, 100, 80, 80)
boss_hp = bosses[level][1]
boss_speed = 2

font = pygame.font.SysFont(None, 36)

# -------------------
# ФУНКЦИИ
# -------------------
def reset_level():
    global boss, boss_hp, boss_speed

    boss = pygame.Rect(random.randint(100, 700), 100, 80, 80)
    boss_hp = bosses[level][1]
    boss_speed = 2 + level * 0.5


def draw_text(text, x, y, color=(255,255,255)):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

# -------------------
# ИГРОВОЙ ЦИКЛ
# -------------------
running = True

while running:
    clock.tick(60)
    screen.fill((20, 20, 30))

    # -------------------
    # СОБЫТИЯ
    # -------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(pygame.Rect(player.x + 18, player.y, 5, 10))

    # -------------------
    # УПРАВЛЕНИЕ
    # -------------------
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player.y -= player_speed
    if keys[pygame.K_s]:
        player.y += player_speed
    if keys[pygame.K_a]:
        player.x -= player_speed
    if keys[pygame.K_d]:
        player.x += player_speed

    # -------------------
    # ПУЛИ
    # -------------------
    for bullet in bullets[:]:
        bullet.y -= 10
        pygame.draw.rect(screen, (255, 255, 0), bullet)

        if bullet.colliderect(boss):
            boss_hp -= 10
            bullets.remove(bullet)

        if bullet.y < 0:
            bullets.remove(bullet)

    # -------------------
    # БОСС ДВИЖЕНИЕ
    # -------------------
    if boss.x < player.x:
        boss.x += boss_speed
    else:
        boss.x -= boss_speed

    if boss.y < player.y:
        boss.y += boss_speed
    else:
        boss.y -= boss_speed

    # -------------------
    # РИСОВАНИЕ
    # -------------------
    pygame.draw.rect(screen, (0, 200, 255), player)   # игрок
    pygame.draw.rect(screen, (200, 50, 50), boss)     # босс

    # -------------------
    # ХП БОССА
    # -------------------
    draw_text(f"Level: {level+1} - {bosses[level][0]}", 20, 20)
    draw_text(f"Boss HP: {boss_hp}", 20, 60)

    # -------------------
    # ПОБЕДА НАД БОССОМ
    # -------------------
    if boss_hp <= 0:
        level += 1

        if level >= len(bosses):
            screen.fill((0, 0, 0))
            draw_text("YOU WIN ALL LEVELS!", 300, 300, (0,255,0))
            pygame.display.update()
            pygame.time.delay(5000)
            running = False
        else:
            reset_level()

    pygame.display.update()

pygame.quit()
