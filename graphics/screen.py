import pygame

#
pygame.font.init()
defaultFont = font = pygame.font.SysFont("comicsansms", 35)


class ProgressBar():
    def __init__(self, x, y, width, height, percent, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.percent = percent
        self.color = color

    def update(self, percent):
        self.percent = percent

    def draw(self, canvas):
        current_width = self.width * self.percent // 100
        pygame.draw.rect(canvas, self.color, pygame.Rect(self.x, self.y, current_width, self.height))


class Canvas:
    def __init__(self, width, height, title, background=None):
        self.canvas = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        if background:
            self.background = pygame.image.load(background)
            self.background = pygame.transform.smoothscale(
                self.background, (width, height))

    def redraw(self, color=0x0000000):
        self.canvas.fill(color)

    def draw_mob(self, mob):
        mob.draw(self.canvas)

    def draw_image(self, image, x=100, y=100):
        self.canvas.blit(image, (x, y))

    def draw_sprite(self, sprite):
        self.canvas.blit(sprite.get_image(), (0, 0))

    def draw_text(self, text, x, y, color=0x999999, font=defaultFont, anchor='TL'):
        '''TL = top-left || TR = topRight || BL = bottomLeft || BR = bottnRight || C = center'''
        label = font.render(text, 1, color)

        if anchor == 'TL':
            pass
        elif anchor == 'C':
            x += (self.canvas.get_width() >> 1) - (label.get_width() >> 1)
            y += (self.canvas.get_height() >> 1) - (label.get_height() >> 1)
        elif anchor == 'TR':
            x += self.canvas.get_width() - label.get_width()
        elif anchor == 'BL':
            y += self.canvas.get_height() - label.get_height()
        else:
            x += self.canvas.get_width() - label.get_width()
            y += self.canvas.get_height() - label.get_height()

        self.canvas.blit(label, (x, y))

    @staticmethod
    def update():
        pygame.display.update()
