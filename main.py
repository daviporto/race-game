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
enemies.append(Enemy(audi_sprite))


def key_board(keys):
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.car.direction = -1
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.car.direction = 1

    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.car.gas = -1
    elif keys[pygame.K_UP] or keys[pygame.K_w]:
        player.car.gas = 1


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
        enemy.update(speed)
        if player.car.collided(enemy.car):
            player.crash(enemy)

    screen.redraw()
    track.render(screen.canvas)
    screen.draw_text(f"speed {math.fabs(speed * 10)}", 20, -20, color=0x0, anchor='BL')
    screen.draw_text(f"score {player.score}", -120, -20, color=0x0, anchor='BR')
    screen.draw_text(f"lives {player.lives}", 20, 20, color=0x0)
    player.draw(screen.canvas)
    for enemy in enemies:
        enemy.draw(screen.canvas)

    screen.update()
