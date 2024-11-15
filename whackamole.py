import pygame
import random
#defined all the nums i need so i dont need to keep remembering them
sw,sh,gs,gw,gh,gc=640,512,32,20,16, (0,0,0)

def draw(screen):
    for x in range(0, sw,gs):
        for y in range(0, sh, gs):
            pygame.draw.rect(screen, gc, (x, y, gs, gs), 1)

def random_move():
    x=random.randrange(0,gw)
    y=random.randrange(0,gh)
    return x,y

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        mole_image=pygame.transform.scale(mole_image, (gs, gs))
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        pos=(0,0)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type==pygame.MOUSEBUTTONDOWN:
                    mx, my=event.pos
                    mole_location=mole_image.get_rect(topleft=(pos[0]*gs,pos[1]*gs))
                    if mole_location.collidepoint(mx, my):
                        pos=random_move()
            screen.fill("light green")
            draw(screen)
            mole_location=mole_image.get_rect(topleft=(pos[0]*gs,pos[1]*gs))
            screen.blit(mole_image,mole_location)
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
