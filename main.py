import pygame
import random
import sys


WIDTH, HEIGHT = 500, 700
FPS = 60

BASKET_SPEED = 8
MAX_LIVES = 3

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SKY = (135, 206, 250)
GREEN = (34, 139, 34)
RED = (220, 20, 60)
YELLOW = (255, 215, 0)
BROWN = (139, 69, 19)
DARK_RED = (180, 0, 0)


pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Apples!")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)
big_font = pygame.font.SysFont(None, 70)
medium_font = pygame.font.SysFont(None, 50)


try:
    pygame.mixer.music.load("tatamusic-game-gaming-video-game-music-482380.mp3")
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)
except:
    print("Background music not found. Game will run without music.")


class Basket:
    def __init__(self):
        self.width = 100
        self.height = 40
        self.x = WIDTH // 2 - self.width // 2
        self.y = HEIGHT - 80
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= BASKET_SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += BASKET_SPEED

        self.x = max(0, min(self.x, WIDTH - self.width))
        self.rect.x = self.x

    def draw(self, surface):
        pygame.draw.rect(surface, BROWN, self.rect)
        pygame.draw.rect(surface, (100, 50, 20), (self.x, self.y, self.width, 10))
        pygame.draw.line(surface, BROWN, (self.x + 10, self.y), (self.x + 25, self.y - 15), 4)
        pygame.draw.line(surface, BROWN, (self.x + self.width - 10, self.y),
                         (self.x + self.width - 25, self.y - 15), 4)

class FallingObject:
    def __init__(self, obj_type, speed):
        self.type = obj_type
        self.radius = 22
        self.x = random.randint(30, WIDTH - 30)
        self.y = -40
        self.speed = speed
        self.rect = pygame.Rect(self.x - self.radius, self.y - self.radius,
                                self.radius * 2, self.radius * 2)

    def update(self):
        self.y += self.speed
        self.rect.y = self.y - self.radius
        self.rect.x = self.x - self.radius

    def draw(self, surface):
        if self.type == "apple":
            pygame.draw.circle(surface, RED, (self.x, self.y), self.radius)
            pygame.draw.circle(surface, (180, 0, 0), (self.x - 6, self.y - 6), 6)
            pygame.draw.ellipse(surface, GREEN, (self.x + 5, self.y - 28, 14, 10))
        else:
            pygame.draw.circle(surface, BLACK, (self.x, self.y), self.radius)
            pygame.draw.circle(surface, (60, 60, 60), (self.x - 5, self.y - 5), 5)
            pygame.draw.line(surface, (80, 80, 80), (self.x, self.y - self.radius),
                             (self.x + 8, self.y - self.radius - 12), 3)
            pygame.draw.circle(surface, YELLOW, (self.x + 8, self.y - self.radius - 12), 4)

    def is_off_screen(self):
        return self.y > HEIGHT + 50


def reset_game():
    basket = Basket()
    objects = []
    score = 0
    lives = MAX_LIVES
    level = 1
    spawn_timer = 0
    game_over = False
    won = False
    return basket, objects, score, lives, level, spawn_timer, game_over, won

basket, objects, score, lives, level, spawn_timer, game_over, won = reset_game()

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if (game_over or won) and event.key == pygame.K_r:
                basket, objects, score, lives, level, spawn_timer, game_over, won = reset_game()
                # Restart music when restarting the game
                try:
                    pygame.mixer.music.play(-1)
                except:
                    pass

    keys = pygame.key.get_pressed()

    if not game_over and not won:
        basket.move(keys)

        spawn_timer += 1
        spawn_interval = max(14, 40 - level * 5)
        fall_speed = 3.5 + level

        if spawn_timer >= spawn_interval:
            obj_type = "apple" if random.random() < 0.70 else "bomb"
            objects.append(FallingObject(obj_type, fall_speed + random.uniform(-0.5, 1.0)))
            spawn_timer = 0

        for obj in objects[:]:
            obj.update()

            if obj.rect.colliderect(basket.rect):
                if obj.type == "apple":
                    score += 10
                else:
                    lives -= 1
                    if lives <= 0:
                        game_over = True
                        pygame.mixer.music.stop()  # stop music on game over
                objects.remove(obj)
                continue

            if obj.is_off_screen():
                objects.remove(obj)

        new_level = min(5, score // 80 + 1)
        if new_level > level:
            level = new_level

        if level >= 5 and score >= 400:
            won = True
            pygame.mixer.music.stop()  # stop music on win

    screen.fill(SKY)
    pygame.draw.rect(screen, GREEN, (0, HEIGHT - 40, WIDTH, 40))

    basket.draw(screen)
    for obj in objects:
        obj.draw(screen)

    screen.blit(font.render(f"Score: {score}", True, BLACK), (15, 15))
    screen.blit(font.render(f"Level: {level}/5", True, BLACK), (15, 55))
    screen.blit(font.render(f"Lives: {lives}", True, DARK_RED), (15, 95))

    if game_over:
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 160))
        screen.blit(overlay, (0, 0))

        text = big_font.render("GAME OVER", True, RED)
        score_text = medium_font.render(f"Score: {score}", True, WHITE)
        sub = medium_font.render("Press R to Restart", True, WHITE)
        screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - 50))
        screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, HEIGHT//2))
        screen.blit(sub, (WIDTH//2 - sub.get_width()//2, HEIGHT//2 + 40))



    if won:
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 160))
        screen.blit(overlay, (0, 0))

        text = big_font.render("YOU WIN!", True, YELLOW)
        sub = medium_font.render(f"Final Score: {score}", True, WHITE)
        restart = font.render("Press R to Play Again", True, WHITE)
        screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - 80))
        screen.blit(sub, (WIDTH//2 - sub.get_width()//2, HEIGHT//2 - 10))
        screen.blit(restart, (WIDTH//2 - restart.get_width()//2, HEIGHT//2 + 50))

    pygame.display.flip()

pygame.quit()
sys.exit()



