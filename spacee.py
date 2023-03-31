import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Load images
player_image = pygame.image.load("player.png")
player_rect = player_image.get_rect()
player_rect.centerx = WIDTH // 2
player_rect.bottom = HEIGHT - 10

enemy_image = pygame.image.load("enemy.png")
enemy_rect = enemy_image.get_rect()
enemy_rect.centerx = WIDTH // 2
enemy_rect.top = 10

shot_image = pygame.image.load("shot.png")

# Game variables
shots = []
score = 0
font = pygame.font.Font(None, 30)
high_scores = []

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shot = pygame.Rect(player_rect.centerx - 3, player_rect.top, 6, 18)
                shots.append(shot)

    screen.fill((0, 0, 100))  # Change background to white

    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= 1
    if keys[pygame.K_RIGHT]:
        player_rect.x += 1

    # Move enemy
    enemy_rect.y += 1
    if enemy_rect.bottom > HEIGHT:
        enemy_rect.y = 0
        enemy_rect.x = random.randint(0, WIDTH - enemy_rect.width)

    # Move shots
    for shot in shots:
        shot.top -= 10
        if shot.bottom < 0:
            shots.remove(shot)

    # Check for collisions
    for shot in shots:
        if enemy_rect.colliderect(shot):
            enemy_rect.left = random.randint(0, WIDTH - enemy_rect.width)
            enemy_rect.top = 0
            shots.remove(shot)
            score += 1

    # Check for intersection
    if player_rect.colliderect(enemy_rect):
        running = False

    # Draw score
    score_text = font.render("Score: {}".format(score), True, (0, 0, 0))
    screen.blit(score_text, (WIDTH - 100, 10))

    # Draw images to screen
    screen.blit(player_image, player_rect)
    screen.blit(enemy_image, enemy_rect)
    for shot in shots:
        screen.blit(shot_image, shot)

    pygame.display.update()

    # Check for game over
    if enemy_rect.colliderect(player_rect):
        name = pygame.font.Font(None, 50).render("Enter your name:", True, (0, 0, 0))
        screen.blit(name, (WIDTH // 2 - 150, HEIGHT // 2 - 50))
        pygame.quit()
