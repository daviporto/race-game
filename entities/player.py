from entities.car import Car


class Player:
    def __init__(self, sprites):
        self.score = 0
        self.lives = 4
        self.sprites = sprites
        self.car = Car(400, 200, sprites[0])
        self.current_sprite = 0
        self.collided = 0

    def crash(self, enemy):
        if self.collided == 0:
            enemy.count = 120
            enemy.car.y += 100
            self.collided = 100
            self.lives -= 1
            self.next_sprite()
            if enemy.foward:
                print(self.car.speed)
                self.car.speed -= enemy.car.speed + self.car.speed
                print(self.car.speed)
            else:
                self.car.speed = int(enemy.car.speed / 1.5)

    def draw(self, screen):
        self.car.draw(screen)

    def update(self):
        self.car.update()
        if self.collided:
            self.collided -= 1

    def next_sprite(self):
        self.current_sprite += 1
        self.car.sprite = self.sprites[self.current_sprite]
