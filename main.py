from random import randint

from PIL import Image, ImageDraw


class PuzzlePiece(object):

    def __init__(self, number_of_balls, box_dimensions, identifier):
        self.number_of_balls = number_of_balls
        self.box_dimensions = box_dimensions
        self.identifier = identifier

piece_color_map = {
    'A': (255,165,0),
    'B': (255, 0, 0),
    'C': (0, 0, 255),
    'D': (255,204,255),
    'E': (0, 255, 0),
    'F': (255,255,255),
    'G': (155, 255, 255),
    'H': (153, 0, 153),
    'I': (255, 255, 0),
    'J': (102, 0, 0),
    'K': (0, 204, 0),
    'L': (192, 192, 192),
    'X': (0, 0, 0)
}

pieces = {}
p = PuzzlePiece(4, [2, 3], 'A')
pieces[p.identifier] = p

resize_multiplier = 50
game_width = 11
game_height = 5

height = game_height * resize_multiplier
width = game_width * resize_multiplier

lines = []
with open("level6-11.txt") as textFile:
    lines = [line.split() for line in textFile]
    print(lines)

image = Image.new(mode='RGB', size=(width, height), color=255)


def draw_rect(x, y, resize_multiplier, color):
    shape = (x, y, x + resize_multiplier, y + resize_multiplier)
    img1 = ImageDraw.Draw(image)
    img1.rectangle(shape, fill=color)


def render_board():
    x = 0
    y = 0
    for w in range(0, game_width):
        for l in range(0, game_height):

            game_board_row = lines[l]
            piece_code = game_board_row[0][w]

            draw_rect(x, y, resize_multiplier, piece_color_map[piece_code])
            y += resize_multiplier

        x += resize_multiplier
        y = 0

    image.show()




render_board()