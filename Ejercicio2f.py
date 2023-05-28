from interpreter import draw
from chessPictures import *

base = square.join(square.negative())
negativeBase = base.negative()

row = base.horizontalRepeat(4)
negativeRow = negativeBase.horizontalRepeat(4)

rowPair = row.up(negativeRow)

figure = rowPair.verticalRepeat(2)

draw(figure)