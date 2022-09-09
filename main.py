import pygame
import os
pygame.init()

pygame.display.set_caption("PONG GAME")
FPS = 60

WIDTH, HEIGHT = (700,400)
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
VEL = 8

# LEFT_PL = pygame.Rect(10,290,10,75)
# RIGHT_PL = pygame.Rect(980,290,10,75)

BORDER = pygame.Rect(WIDTH/2 - 10, 0, 10, HEIGHT)

BALL = pygame.Rect(WIDTH/2 - 10, HEIGHT/2,10,10 )

class Ball:
    MAX_VEL = 8;

    def __init__(self):
        self.x_vel = self.MAX_VEL
        self.y_vel = 0
    
    def draw(self,WINDOW):
        pygame.draw.rect(WINDOW, (137,192,111), BALL,10,10)



def moveLeftPL(keysPressed, obj):
    if keysPressed[pygame.K_a] and obj.x - VEL > 0: # left
        obj.x -= VEL
            
    if keysPressed[pygame.K_w] and obj.y - VEL > 0: # up
        obj.y -= VEL

    if keysPressed[pygame.K_d] and obj.x + VEL + obj.width < BORDER.x : # right
        obj.x += VEL
        
    if keysPressed[pygame.K_s] and obj.y + VEL + obj.height < HEIGHT: # down
        obj.y += VEL

def moveRightPL(keysPressed, obj):
    if keysPressed[pygame.K_LEFT] and obj.x - VEL > BORDER.x  : # left
        obj.x -= VEL
            
    if keysPressed[pygame.K_UP] and obj.y - VEL > 0: # up
        obj.y -= VEL

    if keysPressed[pygame.K_RIGHT] and obj.x + VEL < WIDTH - obj.width : # right
        obj.x += VEL
        
    if keysPressed[pygame.K_DOWN] and obj.y + VEL + obj.height < HEIGHT: # down
        obj.y += VEL
    
def draw_window(left,right):
    WINDOW.fill((223,248,208))
    pygame.draw.rect(WINDOW, (51,104,86), left)
    pygame.draw.rect(WINDOW, (51,104,86), right)
    pygame.draw.rect(WINDOW, (137,192,111), BORDER)
    pygame.display.update()

def main():
    
    left = pygame.Rect(10,HEIGHT/2 - 40 ,10,75)
    right = pygame.Rect(WIDTH - 20,HEIGHT/2 - 40,10,75)
    
    
    run = True
    clock = pygame.time.Clock()
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                run = False
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                pass
            
        keysPressed = pygame.key.get_pressed()
        # print(keysPressed)
        moveRightPL(keysPressed,right)
        moveLeftPL(keysPressed, left)    
        draw_window(left,right)
    
    main()

if __name__ == "__main__":
    main()