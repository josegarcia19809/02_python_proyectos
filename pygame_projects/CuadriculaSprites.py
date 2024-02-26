# Dibujará una ventana con 4 imágenes en mosaico
import pygame

pygame.init()
screen_width = 800
screen_height = 600

screen = pygame.display.set_mode(
    (screen_width, screen_height))
sprite_1 = pygame.image.load("./images/image1.png")
sprite_2 = pygame.image.load("./images/image2.png")
sprite_3 = pygame.image.load("./images/image2.png")
sprite_4 = pygame.image.load("./images/image1.png")
pygame.display.set_caption("Hello Sprite")

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.blit(sprite_1, (0, 0))
    screen.blit(sprite_2, (400, 0))
    screen.blit(sprite_3, (0, 300))
    screen.blit(sprite_4, (400, 300))
    pygame.display.update()

pygame.quit()
