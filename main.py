import pygame
import math
from entities.car import Car
from graphics.screen import Canvas
from graphics.spriteSheet import SptriteSheet
from graphics.track import Track
from entities.player import Player

pygame.init()
WIDTH, HEIGHT = 800, 700
screen = Canvas(WIDTH, HEIGHT, "racing game")
from entities.enemy import Enemy, audi_sprite

red_car_sheet = SptriteSheet('res/cars/red_car.png')
red_car_sprites = red_car_sheet.getSprites(5, 1, invisibleColor=0xff00ff)

track_image = pygame.image.load("res/track/lineTrack.jpeg")
track = Track(track_image, WIDTH, HEIGHT)

player = Player(red_car_sprites)

running = True
time = 0
clock = pygame.time.Clock()
gas = False

enemies = []
enemies.append(Enemy(audi_sprite, False))
enemies.append(Enemy(audi_sprite, True, 1000))
enemies.append(Enemy(audi_sprite, True, 3000))
enemies.append(Enemy(audi_sprite, True, 5000))
enemies.append(Enemy(audi_sprite, True, 7000))
enemies.append(Enemy(audi_sprite, True, 9000))


def key_board(keys):
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.car.direction = -1
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.car.direction = 1

    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.car.gas = -1
    elif keys[pygame.K_UP] or keys[pygame.K_w]:
        player.car.gas = 1


def control_ai():
    for i in range(1, len(enemies)):
        if i == len(enemies) - 1:
            next_car, previous_car = enemies[1].car, enemies[i - 1].car
        elif i == 1:
            next_car, previous_car = enemies[i + 1].car, enemies[len(enemies) - 1].car
        else:
            next_car, previous_car = enemies[i + 1].car, enemies[i - 1].car

        current = enemies[i].car

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




while running:
    time += 1
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key_board(pygame.key.get_pressed())
    player.update()
    speed = player.car.get_speed()
    track.update_offset(speed)
    player.score += math.fabs(speed)
    for enemy in enemies:
        enemy.update(speed, player.car.y, track.track_extension)
        if player.car.collided(enemy.car):
            player.crash(enemy)
    control_ai()

    screen.redraw()
    track.render(screen.canvas)
    screen.draw_text(f"speed {math.fabs(speed * 10)}", 20, -20, color=0x0, anchor='BL')
    screen.draw_text(f"x= {player.car.x}", -150, 10, color=0x0, anchor='TR')
    screen.draw_text(f"score {player.score}", -120, -20, color=0x0, anchor='BR')
    screen.draw_text(f"lives {player.lives}", 20, 20, color=0x0)
    player.draw(screen.canvas)
    for enemy in enemies:
        enemy.draw(screen.canvas)

    screen.update()
