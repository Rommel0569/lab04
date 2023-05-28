from interpreter import draw
from chessPictures import *

base = square.join(square.negative())
baseInv = base.negative()

figure = baseInv.horizontalRepeat(4)

draw(figure)
