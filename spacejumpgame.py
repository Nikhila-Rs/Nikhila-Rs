import pygame
import random

# Initialize Pygame
pygame.init()

# Game Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SIZE = 40
GRAVITY = 0.8
JUMP_POWER = -18
WORD_SPEED = 3
WORDS = ["python", "jump", "keyboard", "coding", "challenge", "speed", "perplexity"]

# Setup Display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Keyboard Jump Game")
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT-50))
        self.velocity = 0
        self.on_ground = True

    def jump(self):
        if self.on_ground:
            self.velocity = JUMP_POWER
            self.on_ground = False

    def update(self):
        self.velocity += GRAVITY
        self.rect.y += self.velocity
        if self.rect.bottom >= SCREEN_HEIGHT-50:
            self.rect.bottom = SCREEN_HEIGHT-50
            self.on_ground = True

class FallingWord(pygame.sprite.Sprite):
    def __init__(self, word, speed):
        super().__init__()
        self.word = word
        self.speed = speed
        self.image = font.render(word, True, (0, 0, 0))
        self.rect = self.image.get_rect(center=(random.randint(100, SCREEN_WIDTH-100), 30))

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

def game_loop():
    player = Player()
    all_sprites = pygame.sprite.Group(player)
    words = pygame.sprite.Group()
    
    current_word = random.choice(WORDS)
    words.add(FallingWord(current_word, WORD_SPEED))
    input_text = ""
    score = 0
    game_active = True

    while True:
        screen.fill((255, 255, 255))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if game_active and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.unicode.isalpha():
                    input_text += event.unicode.lower()

        if game_active:
            # Word typing logic
            if input_text == current_word:
                player.jump()
                score += len(current_word)
                current_word = random.choice(WORDS)
                words.add(FallingWord(current_word, WORD_SPEED + score//10))
                input_text = ""
            
            # Collision check
            if pygame.sprite.spritecollide(player, words, False):
                game_active = False

            # Update sprites
            all_sprites.update()
            words.update()

            # Spawn new word if needed
            if not words:
                words.add(FallingWord(random.choice(WORDS), WORD_SPEED + score//10))

            # Drawing
            all_sprites.draw(screen)
            words.draw(screen)
            screen.blit(font.render(f"Score: {score}", True, (0, 0, 0)), (10, 10))
            screen.blit(font.render(input_text, True, (0, 0, 0)), (50, SCREEN_HEIGHT-80))
        else:
            screen.blit(font.render("Game Over! Press SPACE to restart", True, (255, 0, 0)), 
                       (SCREEN_WIDTH//4, SCREEN_HEIGHT//2))
            screen.blit(font.render(f"Final Score: {score}", True, (0, 0, 0)), 
                       (SCREEN_WIDTH//3, SCREEN_HEIGHT//2 + 50))
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                game_loop()
                return

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    game_loop()
    pygame.quit()
