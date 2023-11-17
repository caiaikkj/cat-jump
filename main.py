# Libraries
import pygame

# Init Pygame
pygame.init()

# Window Dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Create Game Window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Untitled Cat Game')

#  FPS
clock = pygame.time.Clock()
FPS = 60

# Load Images
bg_image = pygame.image.load('assets/background.png').convert_alpha()
cat_sprite = pygame.image.load('assets/cat_sprite.png').convert_alpha()

# Player Class
class Player () :
    def __init__(self, x, y):
        self.image = pygame.transform.scale(cat_sprite, (35, 35))
        self.width = 35
        self.height = 20
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)

    def move(self):

        dx = 0
        dy = 0
        
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            dx = -8
        if key[pygame.K_d]:
            dx = 8

        if self.rect.left + dx < 0:
            dx = 0 - self.rect.left
        if self.rect.right + dx > SCREEN_WIDTH:
            dx = SCREEN_WIDTH - self.rect.right

        self.rect.x += dx
        self.rect.y += dy

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y - 15))
        pygame.draw.rect(screen, 'red', self.rect, 2)

cat = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT -150)

# Game Loop
running = True
while running:

    # Clock
    clock.tick(FPS)

    # Call Move
    cat.move()

    # Draw Background
    screen.blit(bg_image, (0, 0))

    # Draw Sprites
    cat.draw()

    # Event Handler
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            running = False


    # Update display window
    pygame.display.update()

pygame.quit()