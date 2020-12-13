import pygame, pygame_gui as gui
from graphics.screen import Canvas
from graphics.menu import Menu
from level import Level

pygame.init()
WIDTH, HEIGHT = 800, 700
screen = Canvas(WIDTH, HEIGHT, "racing game")
manager = gui.UIManager((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

menu = Menu(manager, WIDTH, HEIGHT)
menu.play()
menu.volume(0.1)
level = Level(WIDTH, HEIGHT)

pause = True
while running:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.USEREVENT:
            if event.user_type == gui.UI_BUTTON_PRESSED:
                if event.ui_object_id == '0':
                    pause = False
        manager.process_events(event)

    if pause:
        menu.render(screen.canvas)
        manager.update(time_delta)
        manager.draw_ui(screen.canvas)
    else:
        level.update()
        level.render(screen)
    pygame.display.update()