from interpreter import draw
from chessPictures import *

"""Esto es el bloque en negro"""
negativeSquare = square.negative()

"""Primero estamos agregando las fichas negras con su respectivo fondo"""

bTorre = rock.negative().setFondo(square)
bCaballo = knight.negative().setFondo(negativeSquare)
bAlfil = bishop.negative().setFondo(square)
bReyna = queen.negative().setFondo(negativeSquare)
bRey = king.negative().setFondo(square)
bAlfil2 = bishop.negative().setFondo(negativeSquare)
bCaballo2 = knight.negative().setFondo(square)
bTorre2 = rock.negative().setFondo(negativeSquare)