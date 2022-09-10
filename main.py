import pygame
import os
pygame.init()

pygame.display.set_caption("PONG GAME")
FPS = 60

WIDTH, HEIGHT = (700,400)
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
VEL = 5

# LEFT_PL = pygame.Rect(10,290,10,75)
# RIGHT_PL = pygame.Rect(980,290,10,75)

BORDER = pygame.Rect(WIDTH/2 - 10, 0, 10, HEIGHT)

# BALL = pygame.Rect(WIDTH/2 - 10, HEIGHT/2,10,10)

class Ball:
    MAX_VEL = 3
    RADIUS = 5

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.x_vel = self.MAX_VEL
        self.y_vel = 0
    
    def draw(self,WINDOW):
        # pygame.draw.rect(WINDOW, (51,104,86), pygame.Rect(self.x, self.y,10,10),10,10)
        pygame.draw.circle(WINDOW,(51,104,86), (self.x,self.y), self.RADIUS)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

def handleCollision(ball,left,right):
    if ball.y + ball.RADIUS >= HEIGHT:
        ball.y_vel *= -1
    elif ball.y - ball.RADIUS <= 0:
        ball.y_vel *= -1
        
    if ball.x_vel < 0:
        if ball.y >=  left.y and ball.y <= left.y + left.height:
            if ball.x - ball.RADIUS <= left.x + left.width:
                ball.x_vel *= -1
    else:
            if (ball.y >=  right.y and ball.y <= right.y + right.height):
                if(ball.x + ball.RADIUS >= right.x):
                    ball.x_vel *= -1;
    

def moveLeftPL(keysPressed, obj):
    if keysPressed[pygame.K_w] and obj.y - VEL > 0: # up
        obj.y -= VEL

    if keysPressed[pygame.K_s] and obj.y + VEL + obj.height < HEIGHT: # down
        obj.y += VEL

def moveRightPL(keysPressed, obj):
    if keysPressed[pygame.K_UP] and obj.y - VEL > 0: # up
        obj.y -= VEL
        
    if keysPressed[pygame.K_DOWN] and obj.y + VEL + obj.height < HEIGHT: # down
        obj.y += VEL
    
def draw_window(left,right,ball):
    WINDOW.fill((223,248,208))
    pygame.draw.rect(WINDOW, (51,104,86), left)
    pygame.draw.rect(WINDOW, (51,104,86), right)
    pygame.draw.rect(WINDOW, (137,192,111), BORDER)
    ball.draw(WINDOW)
    pygame.display.update()

def main():
    
    left = pygame.Rect(10,HEIGHT/2 - 40 ,10,75)
    right = pygame.Rect(WIDTH - 20,HEIGHT/2 - 40,10,75)
    ball = Ball(WIDTH/2-5,HEIGHT/2)
    
    run = True
    clock = pygame.time.Clock()
    
    while run:
        clock.tick(FPS)
        draw_window(left,right,ball)
        
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                run = False
                break
            
            if event.type == pygame.KEYDOWN:
                pass
        
        keysPressed = pygame.key.get_pressed()
        # print(keysPressed)
        
        moveRightPL(keysPressed,right)
        moveLeftPL(keysPressed, left)    
        ball.move()
        handleCollision(ball, left, right)
        
        
    
    pygame.quit()

if __name__ == "__main__":
    main()