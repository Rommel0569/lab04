from interpreter import draw
from chessPictures import *

line1 = knight.join(knight.negative())
line2 = line1.horizontalMirror()
figure = line1.up(line2)

draw(figure)