class Track:
    def __init__(self, image, screen_width, screen_height):
        self.image = image
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.track_extension = image.get_height() - screen_height - 10
        self.y_offset = 0

    def render(self, screen):
        screen.blit(self.image, (0, -self.track_extension + self.y_offset ))

    def update_offset(self, speed):
        self.y_offset = (self.y_offset - speed ) % self.track_extension
        #4200 e o tamanho da imagem, entao ela se repetira eternamente

