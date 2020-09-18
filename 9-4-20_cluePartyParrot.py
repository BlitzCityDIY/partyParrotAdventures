import time
from random import randint
from micropython import const
import board
import terminalio
import displayio
import adafruit_imageload
import digitalio
import simpleio
from adafruit_display_text import label

parrot0 = 0
parrot1 = 1
parrot2 = 2
parrot3 = 3
parrot4 = 4
parrot5 = 5
parrot6 = 6
parrot7 = 7
parrot8 = 8
parrot9 = 9

#  creates display
display = board.DISPLAY
#  scale=2 allows the sprites to be bigger
group = displayio.Group(max_size=20)

def_tile = randint(0, 15)

parrot, parrot_pal = adafruit_imageload.load("/partyParrotsClue.bmp",
                                             bitmap=displayio.Bitmap,
                                             palette=displayio.Palette)

parrot0_grid = displayio.TileGrid(parrot, pixel_shader=parrot_pal,
                                 width=4, height=1,
                                 tile_height=60, tile_width=60,
                                 default_tile=def_tile,
                                 x=0, y=0)

parrot1_grid = displayio.TileGrid(parrot, pixel_shader=parrot_pal,
                                 width=4, height=1,
                                 tile_height=60, tile_width=60,
                                 default_tile=parrot0,
                                 x=0, y=60)

parrot2_grid = displayio.TileGrid(parrot, pixel_shader=parrot_pal,
                                 width=4, height=1,
                                 tile_height=60, tile_width=60,
                                 default_tile=parrot0,
                                 x=0, y=120)

parrot3_grid = displayio.TileGrid(parrot, pixel_shader=parrot_pal,
                                 width=4, height=1,
                                 tile_height=60, tile_width=60,
                                 default_tile=parrot0,
                                 x=0, y=180)

group.append(parrot0_grid)
group.append(parrot1_grid)
group.append(parrot2_grid)
group.append(parrot3_grid)

display.show(group)

party0 = 0
party1 = 0
party2 = 0
party3 = 0

p = 0

a = 0
b = 0
c = 0
d = 0
e = 0

while True:

    if (party0 + 0.01) < time.monotonic():

        parrot0_grid[a] = p
        parrot2_grid[c] = p

        p += 1
        party0 = time.monotonic()
        if p > 9:
            p = 0
    if (party1 + 2) < time.monotonic():
        b = randint(0, 3)
        c = randint(0, 3)
        party1 = time.monotonic()

    if (party2 + 0.1) < time.monotonic():
        parrot1_grid[b] = e
        parrot3_grid[d] = e
        e += 1
        party2 = time.monotonic()
        if e > 9:
            e = 0
    if (party3 + 5) < time.monotonic():
        a = randint(0, 3)
        d = randint(0, 3)
        party3 = time.monotonic()
