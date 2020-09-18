import time
from random import randint
from micropython import const
import board
import rgbmatrix
import framebufferio
import terminalio
import displayio
import adafruit_imageload
import digitalio
import simpleio
import displayio
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

displayio.release_displays()
matrix = rgbmatrix.RGBMatrix(
    width=32,
    height=32,
    bit_depth=4,
    rgb_pins=[board.D6, board.D5, board.D9, board.D11, board.D10, board.D12],
    addr_pins=[board.A5, board.A4, board.A3, board.A2],
    clock_pin=board.D13,
    latch_pin=board.D0,
    output_enable_pin=board.D1,
)
display = framebufferio.FramebufferDisplay(matrix)
matrix.brightness = 0.05

group = displayio.Group(max_size=20)

parrot, parrot_pal = adafruit_imageload.load("/partyParrotsMatrix.bmp",
                                             bitmap=displayio.Bitmap,
                                             palette=displayio.Palette)

parrot0_grid = displayio.TileGrid(parrot, pixel_shader=parrot_pal,
                                 width=1, height=1,
                                 tile_height=32, tile_width=32,
                                 default_tile=0,
                                 x=0, y=0)

group.append(parrot0_grid)

display.show(group)

party0 = 0
p = 0

while True:
    if (party0 + 0.1) < time.monotonic():

        parrot0_grid[0] = p

        p += 1
        party0 = time.monotonic()
        if p > 9:
            p = 0