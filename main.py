import pygame


class snake():
    def __init__(self):

        self.clock = pygame.time.Clock()
        self.run = True

        screen_info = pygame.display.Info()
        self.screen_width = screen_info.current_w
        self.screen_height = screen_info.current_h
        self.GRID_SIZE = 50

        #pygame.draw.rect(color=(255,255,255), surface=window, rect=pygame.Rect(0, 0, screen_width, screen_height))

        self.snake = [[],[],[]]    #Le corps du serpent sera des cubes ou les listes contiennent leurs positions sur le plateau


        pygame.display.update()
        self.game()

    def loop(self):
        pygame.display.flip()
        self.clock.tick(6)

    def draw(self, screen):
        self.draw_grid(screen)
        self.draw_snake(screen)
        #self.draw_apple(screen)

    def draw_grid(self, screen):
        for x in range(0, self.screen_width, self.GRID_SIZE):
            pygame.draw.line(screen, (255,255,255), (x, 0), (x, self.screen_height))
        for y in range(0, self.screen_height, self.GRID_SIZE):
            pygame.draw.line(screen, (255,255,255), (0, y), (self.screen_width, y))

    def draw_snake(self, screen):
        for pos in self.snake:
            for coordonnees in pos:
                pygame.draw.rect(screen, (0,255,0), (coordonnees[0]*self.GRID_SIZE, coordonnees[1]*self.GRID_SIZE, self.GRID_SIZE, self.GRID_SIZE))

    #def draw_apple(self, screen):
        #pygame.draw.rect(screen, RED, (self.apple[0]*self.GRID_SIZE, self.apple[1]*self.GRID_SIZE, self.GRID_SIZE, self.GRID_SIZE))

    def game(self):

        while self.run:

            self.draw(window)




            self.loop()







pygame.init()
pygame.display.init()
window = pygame.display.set_mode()




def start():
    snake()

start()