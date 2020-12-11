from entities.car import Car


class Player:
    def __init__(self, sprites):
        self.score = 0
        self.lives = 4
        self.sprites = sprites
        self.car = Car(400, 200, sprites[0])
        self.current_sprite = 0

    def crash(self, enemy):
        if not enemy.collided:
            enemy.collided = True
            enemy.count = 60
            self.lives -= 1
            if enemy.foward:
                self.car.speed -= enemy.car.speed // 2
            else:
                self.car.speed = 0

    def draw(self, screen):
        self.car.draw(screen)

    def update(self):
        self.car.update()

    def next_sprite(self):
        self.current_sprite += 1
        self.car.sprite = self.sprites[self.current_sprite]
