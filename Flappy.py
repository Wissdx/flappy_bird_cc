import pygame, random, math, os, time, birdfile 

pygame.font.init()

width = 500
height = 800

background = pygame.transform.scale2x(pygame.image.load(os.path.join("bg.png")))

def draw_window(win,bird,base):
    win.blit(background, (0, 0))
    bird.draw(win)
    base.draw(win)
    pygame.display.update()
    
def main():
    run = True
    window = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    bird = birdfile.Bird(230, 350)
    base = birdfile.Base(730)
    pipes = [Pipe(600)]
    
    while run:
        clock.tick(30)
        bird.move()        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
        pipe_ind = 0
        add_pipe = False
        rem = []
        
        for pipe in pipes:
            if pipe.collide(bird):
                main()
                
        
        draw_window(window, bird,base)
        
if __name__ == "__main__":
    main()