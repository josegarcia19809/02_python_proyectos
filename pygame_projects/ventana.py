import pygame

pygame.init()

screen_width = 1000
screen_height = 720

screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
pygame.display.set_caption("Hello Pygame")

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

pygame.quit()
