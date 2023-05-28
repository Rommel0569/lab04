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


"""Ordenando las fichas, cada uno a la derecha"""
row1 = bTorre.join(bCaballo).join(bAlfil).join(bReyna).join(bRey).join(bAlfil2).join(bCaballo2).join(bTorre2)

"""Agregando los peones negros, con el fondo respectivo y utilizando horizontalRepeat para completar los 8 peones"""
coupleBlackPawn = pawn.negative().setFondo(negativeSquare).join(pawn.negative().setFondo(square))

row2 = coupleBlackPawn.horizontalRepeat(4)
"""Tiene que ver con las siguientes 32 casillas vacias"""
base = square.join(square.negative())
baseInv = base.negative()

row = base.horizontalRepeat(4)
negativeRow = baseInv.horizontalRepeat(4)

rowPair = row.up(negativeRow)

fila3__6 = rowPair.verticalRepeat(2)

"""Aca solo se saca el opuesto de las primeras dos filas, para tener las fichas y los bloques opuestos"""
row7 = row2.negative()

row8 = row1.negative()
"""Por ultimo se dibuja en orden utilizando la funcion up para que uno este por encima del otro y asi sucesivamente"""
draw(row1.up(row2).up(row3__6).up(row7).up(row8))