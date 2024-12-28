import pygame
import random

pygame.init()
screen=pygame.display.set_mode((600,600))

x=10
y=10
score=0

alien=pygame.image.load('C:/Users/ffion/Desktop/Python Game Development/alien game in pygame/alien.png')
rectangle=pygame.Rect(x,y,20,20)

font=pygame.font.SysFont('Times New Roman',50)
playing=True
message=''

while playing:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            playing=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
            if (rectangle.x-10,rectangle.y-10)<=pygame.mouse.get_pos()<=(rectangle.x+50,rectangle.y+50):
                rectangle.x=random.randint(10,550)
                rectangle.y=random.randint(10,550)
                score=score+1
                message='You win!'
                print('New coordinates',rectangle.x,rectangle.y)
                screen.blit(alien,(rectangle.x,rectangle.y))
                pygame.display.update()

    screen.fill('purple')
    screen.blit(alien,(rectangle.x,rectangle.y))
    text=font.render('Score: '+str(score),True,'white')
    screen.blit(text,(400,10))
    win=font.render(message,True,'white')
    screen.blit(win,(100,10))
    pygame.display.update()