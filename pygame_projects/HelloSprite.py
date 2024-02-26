import pygame

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
sprite_ballon= pygame.image.load("./images/football.png")
pygame.display.set_caption("Hello Sprite")

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.blit(sprite_ballon, (0, 0))
    pygame.display.update()

pygame.quit()