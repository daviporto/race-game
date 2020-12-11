from entities.car import Car
from graphics.sprite import Sprite
import pygame
import os
import random
import math
import copy

audi_image = pygame.image.load(os.path.join('res', 'enemmy_cars', 'audi.png'))
audi_sprite = Sprite(audi_image)

dodge_image = pygame.image.load(os.path.join('res', 'enemmy_cars', 'dodge.png'))
dodge_sprite = Sprite(dodge_image)

mini_truck_image = pygame.image.load(os.path.join('res', 'enemmy_cars', 'mini_truck.png'))
mini_truck_sprite = Sprite(mini_truck_image)

mini_van_image = pygame.image.load(os.path.join('res', 'enemmy_cars', 'mini_van.png'))
mini_van_sprite = Sprite(mini_van_image)

mustang_image = pygame.image.load(os.path.join('res', 'enemmy_cars', 'mustang.png'))
mustang_sprite = Sprite(mustang_image)

taxi_image = pygame.image.load(os.path.join('res', 'enemmy_cars', 'taxi.png'))
taxi_sprite = Sprite(taxi_image)

truck_image = pygame.image.load(os.path.join('res', 'enemmy_cars', 'truck.png'))
truck_sprite = Sprite(truck_image)

enemies_sprites = [audi_sprite, dodge_sprite, mini_truck_sprite, mini_van_sprite, mustang_sprite, taxi_sprite,
                   truck_sprite]


class Enemy:
    def __init__(self, sprite, foward=True, y=150):
        if not foward:
            sprite = copy.copy(sprite)
            sprite.rotate(180)
            x = random.randint(50, 260)
        else:
            x = random.randint(350, 520)
        self.car = Car(x, y, sprite, max_speed=150)
        self.foward = foward
        self.car.speed = random.randint(9, 12)
        self.collided = False
        self.count = 0

    def update(self, speed, py, track_size):
        if self.collided:
            if self.count == 0:
                self.collided = False
            else:
                self.count-=1
        else:
            if not self.foward:
                self.car.y += self.car.speed - speed
                if math.fabs(math.fabs(self.car.y) - math.fabs(py)) > random.randint(1000, 4000):
                    self.car.y = py - 300
                    self.car.x = random.randint(50, 260)

            else:
                self.car.y -= self.car.speed + speed
                if self.car.y > track_size:
                    self.car.y = self.car.y % track_size

    def draw(self, screen):
        self.car.draw(screen)
