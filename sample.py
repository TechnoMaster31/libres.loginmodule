
import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Pygame Window")

# Clock to control frame rate
clock = pygame.time.Clock()

# Rectangle properties
rect_x, rect_y = 100, 100
rect_width, rect_height = 50, 50
rect_speed_x, rect_speed_y = 5, 3

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the rectangle
    rect_x += rect_speed_x
    rect_y += rect_speed_y

    # Bounce off edges
    if rect_x <= 0 or rect_x + rect_width >= WIDTH:
        rect_speed_x = -rect_speed_x
    if rect_y <= 0 or rect_y + rect_height >= HEIGHT:
        rect_speed_y = -rect_speed_y

    # Clear screen
    screen.fill(WHITE)

    # Draw the rectangle
    pygame.draw.rect(screen, BLUE, (rect_x, rect_y, rect_width, rect_height))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()