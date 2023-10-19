import pygame
import math


pygame.init()  
pygame.display.set_caption("planet orbit sim")  
screen = pygame.display.set_mode((800, 800))  
clock = pygame.time.Clock() 
gameover = False 



t=0



while not gameover:
    clock.tick(60) 
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            gameover = True
    t+=.1
    
    MercX = 100*.3870*math.sin(t*4.1+.0796)+400
    MercY = 100*.3788*math.cos(t*4.1)+400
    
    VenX = 100*.7219*math.sin(t*1.62+.0049)+400
    VenY = 100*.7219*math.cos(t*1.62)+400
    



    # RENDER--------------------------------------------------------------------------------
            
    screen.fill((0,0,0))
    
    pygame.draw.circle(screen, (200, 200, 0), (400,400),10) #sun

    pygame.draw.circle(screen, (200, 100, 100), (MercX, MercY),3) #mercury
    
    pygame.draw.circle(screen, (150, 150, 100), (VenX, VenY),5) #mercury

    
    pygame.display.flip()
    
