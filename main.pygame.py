import pygame
import sys

# Settings
WIDTH, HEIGHT = 800, 600
TILE_SIZE = 40
GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE

# Colors
SKY = (135, 206, 235)
GRASS = (50, 200, 30)
DIRT = (139, 69, 19)
PLAYER = (255, 255, 0)
WHITE = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Minecraft 2D")

# World grid: 0=empty, 1=grass, 2=dirt
world = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
for y in range(GRID_HEIGHT):
    for x in range(GRID_WIDTH):
        if y > GRID_HEIGHT // 2:
            world[y][x] = 2  # dirt
        elif y == GRID_HEIGHT // 2:
            world[y][x] = 1  # grass

player_x, player_y = GRID_WIDTH // 2, GRID_HEIGHT // 2

clock = pygame.time.Clock()

def draw_world():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            if world[y][x] == 1:
                pygame.draw.rect(screen, GRASS, rect)
            elif world[y][x] == 2:
                pygame.draw.rect(screen, DIRT, rect)
            pygame.draw.rect(screen, WHITE, rect, 1)  # grid lines

def draw_player():
    rect = pygame.Rect(player_x * TILE_SIZE, player_y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
    pygame.draw.rect(screen, PLAYER, rect)

def main():
    global player_x, player_y
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and player_x > 0:
                    player_x -= 1
                if event.key == pygame.K_RIGHT and player_x < GRID_WIDTH - 1:
                    player_x += 1
                if event.key == pygame.K_UP and player_y > 0:
                    player_y -= 1
                if event.key == pygame.K_DOWN and player_y < GRID_HEIGHT - 1:
                    player_y += 1
                if event.key == pygame.K_1:
                    world[player_y][player_x] = 1  # Place grass
                if event.key == pygame.K_2:
                    world[player_y][player_x] = 2  # Place dirt
                if event.key == pygame.K_0:
                    world[player_y][player_x] = 0  # Remove block

        screen.fill(SKY)
        draw_world()
        draw_player()
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()