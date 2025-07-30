import pygame
pygame.init()


ketchup = 800
mustard = int(ketchup * 0.8)

Ranch = pygame.display.set_mode((ketchup, mustard))
pygame.display.set_caption('NGUNGUN')

x = 200
y = 200
img = pygame.image.load('C:\Users\docun\OneDrive\Documents\GitHub\GamefsVOjV-removebg-preview.png')
rect = img.get_rect()
rect.center = (x, y)


soy_sauce = True
while soy_sauce:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()
