import pygame, sys

#--Initialize Pygame--#
pygame.init()


#--Setting--#
window_width = 900
window_height = 600
fps = 120
clock = pygame.time.Clock()

color_white = (255,255,255)


#--Game Window--#
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Pong")



#--Sprites--#
class Player1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,80))
        self.image.fill(color_white)
        self.rect = self.image.get_rect()
        self.rect.left = 25
        self.rect.centery = window_height / 2

class Player2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,80))
        self.image.fill(color_white)
        self.rect = self.image.get_rect()
        self.rect.right = window_width - 25
        self.rect.centery = window_height / 2


#--Sprite Groups--#
all_sprites = pygame.sprite.Group()

player1 = Player1()
all_sprites.add(player1)
player2 = Player2()
all_sprites.add(player2)



#--Game Loop--#
while True:
    #--Set Framerate--#
    clock.tick(fps)

    #--Process Events--#
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #-Update-#

    #-Draw-#
    all_sprites.draw(game_window)

    #-Flip-#
    pygame.display.flip()

pygame.quit()
