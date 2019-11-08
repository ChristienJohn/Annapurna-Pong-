import pygame, sys, random

#--Initialize Pygame--#
pygame.init()


#--Setting--#
window_width = 900
window_height = 600
fps = 120
clock = pygame.time.Clock()

#-Colors-#
color_white = (255,255,255)
color_black = (0,0,0)


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
        self.dy = 0

    def update(self):
        self.dy = 0

        #-movement-#
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_w]:
            self.dy = -3
        if keystate[pygame.K_s]:
            self.dy = 3
        self.rect.y += self.dy

        #-constraints-#
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > window_height:
            self.rect.bottom = window_height


class Player2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,80))
        self.image.fill(color_white)
        self.rect = self.image.get_rect()
        self.rect.right = window_width - 25
        self.rect.centery = window_height / 2

    def update(self):
        self.dy = 0

        #-movement-#
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.dy = -3
        if keystate[pygame.K_DOWN]:
            self.dy = 3
        self.rect.y += self.dy

        #-constraints-#
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > window_height:
            self.rect.bottom = window_height


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,10))
        self.image.fill(color_white)
        self.rect = self.image.get_rect()
        self.rect.center = (window_width / 2,window_height / 2)
        self.dx = random.choice([-1,1])
        self.dy = random.choice([-2,-1,1,2])

    def update(self):
        self.rect.x += self.dx
        self.rect.y  += self.dy

        #-constraints-#
        if self.rect.top < 0:
            self.dy *= -1
        if self.rect.bottom > window_height:
            self.dy *= -1

        #-collision with paddle-#
        collision = pygame.sprite.spritecollideany(ball, all_sprites)
        if collision:
            if collision == player2: #fix player 2
                self.rect.x -= self.dx
                self.dx *= -1
                self.dx += random.choice([0,1])

            if collision == player1:
                self.rect.x -= self.dx
                self.dx *= -1
                self.dx += random.choice([0,1])

            if self.dy == 0:
                self.dy += random.choice([-1,1])
            if self.dy <= 0:
                self.dy += -random.choice([-1,0,1])
            if self.dy >= 0:
                self.dy += random.choice([-1,0,1])



#--Sprite Groups--#
all_sprites = pygame.sprite.Group()
ball_sprite = pygame.sprite.GroupSingle()

player1 = Player1()
all_sprites.add(player1)
player2 = Player2()
all_sprites.add(player2)
ball = Ball()
ball_sprite.add(ball)



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
    all_sprites.update()
    ball_sprite.update()

    #-Draw-#
        #-Fill-#
    game_window.fill(color_black)
        #-Field-#
    pygame.draw.line(game_window,color_white,(window_width / 2,0), (window_width / 2,window_height))
    pygame.draw.circle(game_window,color_white,(window_width // 2,window_height // 2), 80, 1)

        #-Sprites-#
    all_sprites.draw(game_window)
    ball_sprite.draw(game_window)

    #-Flip-#
    pygame.display.flip()

pygame.quit()
