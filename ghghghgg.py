from pygame import *
init() # this is pygame.init()
running = True
while running:
    display.set_mode((800,600))
    visible = True
    textFont = font.Font(None, 70)
    while visible:
        for evt in event.get():
            if evt.type == QUIT:
                visible = False
            if evt.type == KEYDOWN:
                if evt.key == K_ESCAPE:
                    visible = running = False
        textPic = textFont.render("Hello world!", True, (255,255,255))
        display.get_surface().blit(textPic, (0,0))
        display.flip()
    quit()