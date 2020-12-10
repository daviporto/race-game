from entities.car import Car
from graphics.sprite import Sprite
import pygame
import os

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
    def __init__(self, sprite, foward=True):
        self.car = Car(400, 150, sprite, max_speed=150)
        self.foward = foward
        self.car.speed = 4
        self.collided = False

    def update(self, speed):
        self.car.y -= self.car.speed + speed

    def draw(self, screen):
        self.car.draw(screen)
