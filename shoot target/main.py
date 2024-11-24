import pgzrun
import random
import itertools

TITLE = "shoot target"
WIDTH = 800
HEIGHT = 800
BLOCKPOSITION = [(750,50), (750,750), (50, 750), (50, 50)]
BLOCKCYCLE = itertools.cycle(BLOCKPOSITION)

'---------------------'

block = Actor("block")
ship = Actor("player")

ship.pos = (WIDTH//2, HEIGHT//2)
block.pos = (50,50)

'---------------------'

def draw():
    screen.clear()
    block.draw()
    ship.draw()

def move_block():
    animate(block, "bounce_end", duration = 1, pos = next(BLOCKCYCLE))

def move_ship(target_pos):
    animation = animate(ship, tween = "accel_decel", pos = target_pos, duration = ship.distance_to(ship.target)/200, on_finished = rotate_ship)

def rotate_ship():
    global ship
    x = random.randint(70, WIDTH - 70)
    y = random.randint(70, HEIGHT - 70)
    ship.target = (x,y)
    target_angle = ship.angle_to(ship.target)
    target_angle += 360*((ship.angle - target_angle+180)//360)
    animate(ship, angle = target_angle, duration = 0.5, on_finished = move_ship(ship.target))

move_block()
rotate_ship()
clock.schedule_interval(move_block, 2)
pgzrun.go()