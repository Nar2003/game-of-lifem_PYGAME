import pygame
import numpy as np
from scipy.signal import convolve2d
import time
pygame.init()

PLAYGROUND_SIZE = (80,45)
SCREEN_SIZE = (1600,900)
DOT_SIZE = (
    SCREEN_SIZE[0] / PLAYGROUND_SIZE[0],
    SCREEN_SIZE[1] / PLAYGROUND_SIZE[1],

    )
PLAYGROUND = np.random.randint(0,2, size = PLAYGROUND_SIZE)
screen = pygame.display.set_mode(SCREEN_SIZE)

print(PLAYGROUND)

pygame.display.set_caption("GAME OF LIFE")

live = pygame.Surface(DOT_SIZE)
live.fill('White')

dead = pygame.Surface(DOT_SIZE)
dead.fill('Black')
def metric_transform(x,y,coef = DOT_SIZE):
    return x * coef[0], y*coef[1]

def die_or_alive_codex(playground = PLAYGROUND):
    # print(convolve2d(playground,np.ones((3,3),dtype=int),'same') - playground) #test
    # print(playground) #test
    sum_matrix = convolve2d(playground,np.ones((3,3),dtype=int),'same') - playground
    for x in range(PLAYGROUND_SIZE[0]):
        for y in range(PLAYGROUND_SIZE[1]):
            # print(playground[x,y]) #test
            if playground[x,y] == 1: # bit is live
                if sum_matrix[x,y] >= 2 and sum_matrix[x,y] <= 3: #classic rules of game (can be modificate)
                    playground[x,y] = 1 # bit is most be live
                    screen.blit(live,metric_transform(x,y))
                else:
                    playground[x,y] = 0 #bit is dead
                    screen.blit(dead,metric_transform(x,y))
            else: # bit is dead
                if sum_matrix[x,y] == 3 :
                    playground[x,y] = 1
                    screen.blit(live,metric_transform(x,y))
                else:
                    playground[x,y] = 0
                    screen.blit(dead,metric_transform(x,y))
        # pygame.display.update() # IF YOUR PC SLOW UNCOMMENT THIS!
    print('\n\n\n\n\n\n\n\n' + str(playground)\
        .replace('[','')\
            .replace(' ','')\
                .replace(']','')\
                    .replace('1','O')\
                        .replace('0',' '))



running = 1
while running:
    die_or_alive_codex()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = 0
