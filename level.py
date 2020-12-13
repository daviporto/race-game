import pygame
import pygame_gui
import math
from graphics.screen import Canvas
from graphics.spriteSheet import SptriteSheet
from graphics.track import Track
from entities.player import Player
from entities.enemy import Enemy, audi_sprite
from graphics.menu import Menu

red_car_sheet = SptriteSheet('res/cars/red_car.png')
red_car_sprites = red_car_sheet.getSprites(5, 1, invisibleColor=0xff00ff)
track_image = pygame.image.load("res/track/lineTrack.jpeg")


class Level:
    def __init__(self, width, height):
        self.track = Track(track_image, width, height)
        self.player = Player(red_car_sprites)
        self.enemies = [Enemy(audi_sprite, False),
                        Enemy(audi_sprite, True, 1000),
                        Enemy(audi_sprite, True, 3000),
                        Enemy(audi_sprite, True, 5000),
                        Enemy(audi_sprite, True, 7000),
                        Enemy(audi_sprite, True, 9000)]

    def control_ai(self):
        for i in range(1, len(self.enemies)):
            if i == len(self.enemies) - 1:
                next_car, previous_car = self.enemies[1].car, self.enemies[i - 1].car
            elif i == 1:
                next_car, previous_car = self.enemies[i + 1].car, self.enemies[len(self.enemies) - 1].car
            else:
                next_car, previous_car = self.enemies[i + 1].car, self.enemies[i - 1].car

            current = self.enemies[i].car

            if current.too_close(current.y + 100, next_car):
                current.speed = next_car.speed + 5
            elif current.too_close(current.y - 150, previous_car):
                current.speed = next_car.speed - 5
            elif current.collided(next_car):
                current.y + 100
                next_car.y - 100
            elif current.collided(previous_car):
                current.y - 100
                previous_car.y + 100

    def update(self):
        self.player.key_board(pygame.key.get_pressed())
        self.player.update()
        if self.player.collided == 0:
            speed = self.player.car.get_speed()
        else:
            speed = self.player.car.speed
        self.track.update_offset(speed)
        self.player.score += math.fabs(speed)
        for enemy in self.enemies:
            enemy.update(speed, self.player.car.y, self.track.track_extension)
            if self.player.car.collided(enemy.car):
                self.player.crash(enemy)
        self.control_ai()

    def render(self, screen):
        self.track.render(screen.canvas)
        screen.draw_text(f"speed {math.fabs(self.player.car.speed * 10)}", 20, -20, color=0x0, anchor='BL')
        screen.draw_text(f"score {self.player.score}", -120, -20, color=0x0, anchor='BR')
        screen.draw_text(f"lives {self.player.lives}", 20, 20, color=0x0)
        self.player.draw(screen.canvas)
        for enemy in self.enemies:
            enemy.draw(screen.canvas)

        screen.update()
        if self.player.lives == 0:
            running = False
