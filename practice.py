import pygame
import image_processing

pygame.init()
screen = pygame.display.set_mode((600, 500))
done = False
is_blue = True
x, y = 30, 30
clock = pygame.time.Clock()

pygame.mixer.music.load('BOOM BOOM GOBLIN TRACK.wav')
pygame.mixer.music.play(loops=-1)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #Key Presses
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 5
    if pressed[pygame.K_DOWN]: y += 5
    if pressed[pygame.K_LEFT]: x -= 5
    if pressed[pygame.K_RIGHT]: x += 5

    if is_blue:
        color = (0,128,255)
    else:
       color = (255,100,0)
    screen.fill((255, 255, 255))
    screen.blit(image_processing.get_image('ball.png'), (x, y))

    pygame.display.flip()
    clock.tick(60)