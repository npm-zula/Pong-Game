import pygame
import os
pygame.init()

pygame.display.set_caption("PONG GAME")
FPS = 60

WIDTH, HEIGHT = (1000,700)
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))

LEFT_PL = pygame.Rect(10,290,10,75)
RIGHT_PL = pygame.Rect(980,290,10,75)

BORDER = pygame.Rect(WIDTH/2 - 10, 0, 10, HEIGHT)




def draw_window():
    WINDOW.fill((223,248,208))
    pygame.draw.rect(WINDOW, (51,104,86), LEFT_PL)
    pygame.draw.rect(WINDOW, (51,104,86), RIGHT_PL)
    pygame.draw.rect(WINDOW, (137,192,111), BORDER)
    pygame.display.update()

def main():
    run = True
    clock = pygame.time.Clock()
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                run = False
                break;
                
        draw_window()
    
    pygame.quit()

if __name__ == "__main__":
    main()