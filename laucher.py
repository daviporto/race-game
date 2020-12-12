import pygame, pygame_gui as gui


class Menu:
    def __init__(self, manager):
        self.a = gui.elements.UIButton(relative_rect=pygame.rect(50, 50, 100, 20), text='works?', manager=manager, object_id=1)
