def get_absoluto(value):
    return value if value >= 0 else value * -1


class Car:
    def __init__(self, x, y, sprite, max_speed=250, aceleration=1):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.max_speed = max_speed
        self.aceleration = aceleration
        self.speed = 0
        self.gas = 0
        self.direction = 0

    def draw(self, screen):
        self.sprite.render(screen, self.x, self.y)

    def collided(self, obj):
        offset_x = self.x - obj.x
        offset_y = self.y - obj.y
        return self.sprite.mask.overlap(obj.sprite.mask, (offset_x, offset_y)) != None

    def too_close(self, y, obj):
        offset_x = 100
        offset_y = self.y - y
        return self.sprite.mask.overlap(obj.sprite.mask, (offset_x, offset_y)) != None

    def update(self):
        if self.speed:
            if self.direction:
                if self.direction == 1:
                    self.x += 5
                else:
                    self.x -= 5
            self.direction = 0

    def get_speed(self):
        if not self.gas:
            if self.speed:
                if self.speed > 0:
                    self.speed -= self.aceleration
                elif self.speed < 0:
                    self.speed += self.aceleration
        else:
            if self.gas == -1:
                self.speed += self.aceleration
            else:
                self.speed -= self.aceleration
        self.gas = 0

        if get_absoluto(self.speed) > self.max_speed:
            if self.speed > 0:
                self.speed = self.max_speed
            else:
                self.speed = -self.max_speed

        return self.speed // 10
