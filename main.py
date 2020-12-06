import pygame

from entities.car import Car
from graphics.screen import Canvas
from graphics.spriteSheet import SptriteSheet
from graphics.track import Track
import  math

pygame.init()
WIDTH, HEIGHT = 800, 700
screen = Canvas(WIDTH, HEIGHT, "racing game")

red_car_sheet = SptriteSheet('res/cars/red_car.png')
red_car_sprites = red_car_sheet.getSprites(5, 1, invisibleColor=0xff00ff)

track_image = pygame.image.load("res/track/lineTrack.jpeg")
track = Track(track_image, WIDTH, HEIGHT)

player_car = Car(200, 200, red_car_sprites)

running = True
time = 0
clock = pygame.time.Clock()
gas = False


def key_board(keys):
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_car.direction = -1
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_car.direction = 1

    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player_car.gas = -1
    elif keys[pygame.K_UP] or keys[pygame.K_w]:
        player_car.gas = 1

score = 0
while running:
    time += 1
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key_board(pygame.key.get_pressed())
    player_car.update()
    speed = player_car.get_speed()
    track.update_offset(speed)
    score += math.fabs(speed)

    screen.redraw()
    track.render(screen.canvas)
    screen.draw_text(f"speed {math.fabs(speed * 10)}", 20, -20, color=0x0, anchor='BL')
    screen.draw_text(f"score {score}", -120, -20, color=0x0, anchor='BR')
    player_car.draw(screen.canvas)
    screen.update()
