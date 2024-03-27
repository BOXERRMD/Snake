import pygame
import sys

# Définir les constantes
GRID_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 20
SCREEN_WIDTH = GRID_SIZE * GRID_WIDTH
SCREEN_HEIGHT = GRID_SIZE * GRID_HEIGHT
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Snake:
    def __init__(self):
        self.positions = [(5, 5)]
        self.direction = (1, 0)  # Initial direction vers la droite

    def move(self):
        cur = self.positions[0]
        x, y = self.direction
        new = ((cur[0] + x) % GRID_WIDTH, (cur[1] + y) % GRID_HEIGHT)
        if new in self.positions[1:]:
            return False  # Le serpent a heurté son propre corps
        self.positions.insert(0, new)
        return True

    def turn(self, point):
        if (point[0] * -1, point[1] * -1) == self.direction:
            return  # Ne pas permettre de faire demi-tour
        self.direction = point

class Game:
    def __init__(self):
        self.snake = Snake()
        self.apple = (10, 10)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.turn((0, -1))
                elif event.key == pygame.K_DOWN:
                    self.snake.turn((0, 1))
                elif event.key == pygame.K_LEFT:
                    self.snake.turn((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    self.snake.turn((1, 0))

    def draw(self, screen):
        screen.fill(BLACK)
        self.draw_grid(screen)
        self.draw_snake(screen)
        self.draw_apple(screen)

    def draw_grid(self, screen):
        for x in range(0, SCREEN_WIDTH, GRID_SIZE):
            pygame.draw.line(screen, WHITE, (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
            pygame.draw.line(screen, WHITE, (0, y), (SCREEN_WIDTH, y))

    def draw_snake(self, screen):
        for pos in self.snake.positions:
            pygame.draw.rect(screen, GREEN, (pos[0]*GRID_SIZE, pos[1]*GRID_SIZE, GRID_SIZE, GRID_SIZE))

    def draw_apple(self, screen):
        pygame.draw.rect(screen, RED, (self.apple[0]*GRID_SIZE, self.apple[1]*GRID_SIZE, GRID_SIZE, GRID_SIZE))

    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake")

        while True:
            clock.tick(6)  # Vitesse du jeu (10 fps)

            self.handle_keys()
            if not self.snake.move():
                print("Game Over!")
                pygame.quit()
                sys.exit()

            self.draw(screen)
            pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()