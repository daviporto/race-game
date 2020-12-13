import pygame, pygame_gui as gui, os
import openal


class Menu:
    def __init__(self, manager, width, height):
        self.manager = manager
        self.hello_button = gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                                  text='Novo jogo',
                                                  manager=manager,
                                                  object_id='0')
        self.background_image = pygame.image.load(os.path.join('res', "imgs", 'back_ground_menu.png'))
        self.background_image = pygame.transform.scale(self.background_image, (width, height))
        self.source = openal.oalOpen(os.path.join('res', 'songs', 'background.ogg'))

    def update(self):
        pass

    def render(self, cavas):
        cavas.blit(self.background_image, (0, 0))

    def volume(self, volume):
        self.source.set_gain(volume)

    def play(self):
        self.source.play()

    def event_handler(self, events):

        return -1
