import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Asteroid Finder")

# Load the player image
player_image = pygame.image.load(r"space.png")  # Replace "player.png" with your own image file path
player_rect = player_image.get_rect()
player_rect.center = (window_width // 2, window_height - 50)

# Load the enemy image
enemy_image = pygame.image.load(r"enemy.jfif")  # Replace "enemy.png" with your own image file path
enemy_rect = enemy_image.get_rect()


# Set up game variables
enemy_rect.x = random.randint(0, window_width)
enemy_rect.y = 0
enemy_speed = 3
score = 0

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player_rect.x += 5

    # Update enemy position
    enemy_rect.y += enemy_speed
    if enemy_rect.y > window_height:
        enemy_rect.x = random.randint(0, window_width)
        enemy_rect.y = 0
        score += 1

    # Collision detection
    if player_rect.colliderect(enemy_rect):
        running = False

    # Fill the window with white color
    window.fill(white)

    # Draw the player image
    window.blit(player_image, player_rect)

    # Draw the enemy image
    window.blit(enemy_image, enemy_rect)

    # Display score
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, black)
    window.blit(text, (10, 10))

    # Update the game display
    pygame.display.update()
    clock.tick(60)

# Quit the game
pygame.quit()
