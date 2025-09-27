import pygame
import random
import sys

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 600, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Player
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 40
player_img = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
player_img.fill(GREEN)
player_x = WIDTH // 2 - PLAYER_WIDTH // 2
player_y = HEIGHT - PLAYER_HEIGHT - 10
player_speed = 7

# Bullet
BULLET_WIDTH, BULLET_HEIGHT = 5, 10
bullet_img = pygame.Surface((BULLET_WIDTH, BULLET_HEIGHT))
bullet_img.fill(WHITE)
bullets = []
bullet_speed = 10

# Alien
ALIEN_WIDTH, ALIEN_HEIGHT = 40, 30
alien_img = pygame.Surface((ALIEN_WIDTH, ALIEN_HEIGHT))
alien_img.fill(RED)
aliens = []
alien_speed = 2
alien_spawn_delay = 40
alien_timer = 0

clock = pygame.time.Clock()
score = 0
font = pygame.font.SysFont(None, 36)

def draw_window():
    WIN.fill(BLACK)
    WIN.blit(player_img, (player_x, player_y))
    for bullet in bullets:
        WIN.blit(bullet_img, bullet)
    for alien in aliens:
        WIN.blit(alien_img, alien)
    score_text = font.render(f"Score: {score}", True, WHITE)
    WIN.blit(score_text, (10, 10))
    pygame.display.update()

def main():
    global player_x, bullets, aliens, alien_timer, score
    running = True
    while running:
        clock.tick(60)
        alien_timer += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - PLAYER_WIDTH:
            player_x += player_speed
        if keys[pygame.K_SPACE]:
            if len(bullets) < 5:
                bullets.append(pygame.Rect(player_x + PLAYER_WIDTH // 2 - BULLET_WIDTH // 2, player_y, BULLET_WIDTH, BULLET_HEIGHT))

        # Move bullets
        for bullet in bullets[:]:
            bullet.y -= bullet_speed
            if bullet.y < 0:
                bullets.remove(bullet)

        # Spawn aliens
        if alien_timer >= alien_spawn_delay:
            alien_x = random.randint(0, WIDTH - ALIEN_WIDTH)
            aliens.append(pygame.Rect(alien_x, 0, ALIEN_WIDTH, ALIEN_HEIGHT))
            alien_timer = 0

        # Move aliens
        for alien in aliens[:]:
            alien.y += alien_speed
            if alien.y > HEIGHT:
                aliens.remove(alien)

        # Bullet-alien collision
        for bullet in bullets[:]:
            for alien in aliens[:]:
                if bullet.colliderect(alien):
                    bullets.remove(bullet)
                    aliens.remove(alien)
                    score += 1
                    break

        draw_window()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()