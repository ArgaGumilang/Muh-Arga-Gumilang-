import pygame
import random

pygame.init()

# Ukuran layar
WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Project Mandiri")

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

clock = pygame.time.Clock()

# Load gambar
gambar_pemain = pygame.image.load('tupai.png').convert_alpha()
gambar_latar  = pygame.image.load('hutan.jpg').convert()
gambar_biji   = pygame.image.load('biji_ek.png').convert_alpha()
gambar_jamur  = pygame.image.load('jamur.png').convert_alpha()

# Resize
gambar_pemain = pygame.transform.scale(gambar_pemain, (60, 90))
gambar_latar  = pygame.transform.scale(gambar_latar, (WIDTH, HEIGHT))

gambar_biji  = pygame.transform.scale(gambar_biji, (50, 50))
gambar_jamur = pygame.transform.scale(gambar_jamur, (50, 50))

# ================= PLAYER =================
class Player:
    def __init__(self):
        self.image = gambar_pemain
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        self.rect.x = WIDTH // 2
        self.rect.y = HEIGHT - 100
        self.speed = 7

    def move(self, keys):
        if keys[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.x < WIDTH - self.rect.width:
            self.rect.x += self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)


# ================= ITEM =================
class GoodFood:
    def __init__(self, speed):
        self.image = gambar_biji
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = -50
        self.speed = speed

    def fall(self):
        self.rect.y += self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class BadFood:
    def __init__(self, speed):
        self.image = gambar_jamur
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = -50
        self.speed = speed

    def fall(self):
        self.rect.y += self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)


# ================= MAIN =================
def main():
    player = Player()
    items = []
    score = 0
    game_over = False
    running = True

    font = pygame.font.SysFont("Arial", 30, bold=True)
    big_font = pygame.font.SysFont("Arial", 70, bold=True)

    # Event spawn item
    SPAWN_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(SPAWN_EVENT, 800)

    while running:
        screen.blit(gambar_latar, (0, 0))
        keys = pygame.key.get_pressed()

        # ===== EVENT =====
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == SPAWN_EVENT and not game_over:
                speed = 4 + score // 5
                if random.random() < 0.7:
                    items.append(GoodFood(speed))
                else:
                    items.append(BadFood(speed))

        # ===== LOGIC =====
        if not game_over:
            player.move(keys)

            for item in items[:]:
                item.fall()

                # Collision
                if player.rect.colliderect(item.rect):
                    if isinstance(item, GoodFood):
                        score += 1
                        items.remove(item)
                    else:
                        game_over = True

                # Hapus jika keluar layar
                elif item.rect.y > HEIGHT:
                    items.remove(item)

        # ===== DRAW =====
        for item in items:
            item.draw(screen)

        player.draw(screen)

        # Score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (20, 20))

        # Game Over
        if game_over:
            over_text = big_font.render("GAME OVER", True, RED)
            retry_text = font.render("Press R to Restart | ESC to Exit", True, BLACK)

            screen.blit(over_text, (WIDTH // 2 - 200, HEIGHT // 2 - 50))
            screen.blit(retry_text, (WIDTH // 2 - 220, HEIGHT // 2 + 20))

            if keys[pygame.K_r]:
                player.reset()
                items = []
                score = 0
                game_over = False

            if keys[pygame.K_ESCAPE]:
                running = False

        pygame.display.update()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()