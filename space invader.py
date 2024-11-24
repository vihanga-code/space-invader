import math
import random
import pygame

# Screen dimensions
sw, sh = 800, 500

# Initial positions and constants
psx, psy = 370, 380
esx, esy = 2, 20
bullet_speed = 10
collision = 27
game_over_threshold = psy - 40

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)
background = pygame.image.load("background.png")

# Images
playerimage = pygame.image.load("player.png")
enemy_image = pygame.image.load("enemay.png")
bullet_image = pygame.image.load("bullet.png")

# Fonts
font = pygame.font.Font("freesansbold.ttf", 32)
over_font = pygame.font.Font("freesansbold.ttf", 64)

# Player variables
px, py = psx, psy
px_change = 0

# Enemy variables
enemies = [
    {
        "x": random.randint(0, sw - 64),
        "y": random.randint(50, 150),
        "dx": esx
    } for _ in range(6)
]

# Bullet variables
bulletX, bulletY, bullet_state = 0, psy, "ready"

# Score
score = 0


def show_score():
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))


def show_gameover():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def draw_player():
    screen.blit(playerimage, (px, py))


def draw_enemy(enemy):
    screen.blit(enemy_image, (enemy["x"], enemy["y"]))


def fire_bullet():
    screen.blit(bullet_image, (bulletX + 16, bulletY + 10))


def is_collision(enemy):
    return math.hypot(enemy["x"] - bulletX, enemy["y"] - bulletY) < collision


# Game loop
running = True
while running:
    # Background
    screen.blit(background, (0, 0))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                px_change = -5
            if event.key == pygame.K_RIGHT:
                px_change = 5
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bulletX = px
                bullet_state = "fire"

        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                px_change = 0

    # Update player position
    px = max(0, min(px + px_change, sw - 64))

    # Enemy logic
    for i in enemies:
        # Check for game over
        if i["y"] >= game_over_threshold and abs(i["x"] - px) < collision:
            for e in enemies:
                e["y"] = 2000
            show_gameover()
            pygame.display.update()
            pygame.time.wait(2000)
            running = False
            break

        # Enemy movement
        i["x"] += i["dx"]
        if i["x"] <= 0 or i["x"] >= sw - 64:
            i["dx"] *= -1
            i["y"] += esy

        # Collision check
        if is_collision(i):
            bulletY = psy
            bullet_state = "ready"
            score += 1
            i.update(x=random.randint(0, sw - 64), y=random.randint(50, 150))

        draw_enemy(i)

    # Bullet movement
    if bullet_state == "fire":
        fire_bullet()
        bulletY -= bullet_speed
        if bulletY <= 0:
            bullet_state = "ready"
            bulletY = psy

    # Draw player and score
    draw_player()
    show_score()

    # Update display
    pygame.display.update()

