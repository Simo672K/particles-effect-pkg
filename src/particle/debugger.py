import pygame
pygame.init()
font= pygame.font.Font(None, 25)

print("Debugger initialization...")

def debugger(info, x= 10, y= 10):
    display= pygame.display.get_surface()
    debug_surf= font.render(str(info), True, 'Black')
    debug_rect= debug_surf.get_rect(topleft= (x, y))
    display.blit(debug_surf, debug_rect)
