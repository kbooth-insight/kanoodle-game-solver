from random import randint
import numpy
import cv2

piece_color_map = {
    'A': (255, 165, 0),
    'B': (255, 0, 0),
    'C': (0, 0, 255),
    'D': (255, 204, 255),
    'E': (0, 255, 0),
    'F': (255, 255, 255),
    'G': (155, 255, 255),
    'H': (153, 0, 153),
    'I': (255, 255, 0),
    'J': (102, 0, 0),
    'K': (0, 204, 0),
    'L': (192, 192, 192),
    'X': (0, 0, 0)
}

resize_multiplier = 50

class PuzzlePiece(object):

    def __init__(self, identifier, piece_dimensions, piece_definition):
        self.piece_dimensions = piece_dimensions
        self.width = piece_dimensions[0]
        self.height = piece_dimensions[1]
        self.piece_definition = piece_definition
        self.identifier = identifier

    def draw(self):
        image = numpy.zeros((self.piece_dimensions[0] * resize_multiplier, self.piece_dimensions[1] * resize_multiplier, 3), numpy.uint8)

        img2 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        cv2.imshow('test', img2)
        cv2.waitKey(250)



pieces = {}
p = PuzzlePiece('A', (2, 3), ((1, 1), (1, 0), (1, 1)))
p.draw()
pieces[p.identifier] = p


game_width = 11
game_height = 5

height = game_height * resize_multiplier
width = game_width * resize_multiplier

lines = []
with open("level6-11.txt") as textFile:
    lines = [line.split() for line in textFile]
    print(lines)

def draw_rect(x, y, resize_multiplier, color, img):
    start_point = (x, y)
    end_point = (x + resize_multiplier, y + resize_multiplier)
    return cv2.rectangle(img, start_point, end_point, color, -1)


def render_board(img):
    x = 0
    y = 0
    for w in range(0, game_width):
        for h in range(0, game_height):
            game_board_row = lines[h][0]
            piece_code = game_board_row[w]

            img = draw_rect(x, y, resize_multiplier, piece_color_map[piece_code], img)
            y += resize_multiplier

            img2 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            cv2.imshow('test', img2)
            cv2.waitKey(10)

        x += resize_multiplier
        y = 0

    return img


image = numpy.zeros((height, width, 3), numpy.uint8)

image = render_board(image)
img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imshow('test', img)
cv2.waitKey(0)
