from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    vertical = []
    for value in self.img:
    	vertical.append(value[::-1])
    return vertical

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    return Picture(None)

  def negative(self):
    """ Devuelve un negativo de la imagen """
    newimg = []

    for r in self.img:
      x = 0
      row = ""
      while x < len(r):
        row += self._invColor(r[x])
        x +=1
      newimg.append(row)
    
    return Picture(newimg)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    newimg = []
    x = 0
    while x<len(self.img):
      newimg.append(self.img[x] + p.img[x])
      x += 1

    return Picture(newimg)

  def up(self, p):
    newimg = []
    for r in self.img:
      newimg.append(r)

    for r in p.img:
      newimg.append(r)
    return Picture(newimg)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    return Picture(None)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    return Picture(None)

  def verticalRepeat(self, n):
    return Picture(None)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)