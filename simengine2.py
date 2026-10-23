import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Window dimensions
WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Missile Defense Simulation - Workspace")

# Colors (RGB)
BLACK = (10, 10, 15)
GREEN = (0, 255, 100)
RED = (255, 50, 50)
BLUE = (50, 150, 255)
GRAY = (40, 40, 50)

# Clock for controlling frame rate (FPS)
clock = pygame.time.Clock()
FPS = 60

# Simple container to hold our visual entities for Step 1
# (Later, your radar and launcher modules will feed data into lists like this)
threats = []
defenders = []

# Spawn a few test visual dots to verify the workspace works
for _ in range(3):
    threats.append({
        "x": random.randint(100, WIDTH - 100),
        "y": random.randint(50, 300),
        "vx": random.choice([-1, 1]) * random.uniform(0.5, 1.5),
        "vy": random.uniform(0.5, 1.5)
    })

# Main simulation loop
running = True
while running:
    # 1. Event Handling (Closing the window, keyboard inputs, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            # Press SPACE to spawn a new threat manually
            elif event.key == pygame.K_SPACE:
                threats.append({
                    "x": random.randint(100, WIDTH - 100),
                    "y": 50,
                    "vx": random.uniform(-1, 1),
                    "vy": random.uniform(1.0, 2.0)
                })

    # 2. Update Positions (Simulating basic movement for visual check)
    for t in threats:
        t["x"] += t["vx"]
        t["y"] += t["vy"]

    # 3. Drawing / Rendering Workspace
    screen.fill(BLACK)

    # Draw a tactical grid or center line for aesthetics
    pygame.draw.line(screen, GRAY, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 1)
    pygame.draw.line(screen, GRAY, (0, HEIGHT // 2), (WIDTH, HEIGHT // 2), 1)

    # Draw threats as red dots
    for t in threats:
        pygame.draw.circle(screen, RED, (int(t["x"]), int(t["y"])), 6)
        # Draw a tiny label or trail effect placeholder here if desired

    # Draw a placeholder for the defense base at the bottom center
    base_pos = (WIDTH // 2, HEIGHT - 50)
    pygame.draw.rect(screen, BLUE, (base_pos[0] - 15, base_pos[1] - 10, 30, 20))

    # 4. Refresh Screen
    pygame.display.flip()
    
    # Cap the frame rate to maintain steady simulation speed
    clock.tick(FPS)

pygame.quit()
sys.exit()