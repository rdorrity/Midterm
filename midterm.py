#################################################
# Ryan Dorrity, Nathan Warren-Acord
# Midterm Project
# 11/19/2018
#################################################



def getPic():
  return makePicture(pickAFile())
  

def csumbfy(pic):  
  for x in range (0, getWidth(pic)):
    for y in range (0, getHeight(pic)):
      px = getPixel(pic, x, y)
      r = getRed(px)
      g = getGreen(px)
      b = getBlue(px)
      if distance(makeColor(28, 129, 64), getColor(px)) < 200:
        setColor(px, makeColor(abs(r+28)/2, abs(g+129)/2, abs(b+64)/2))
      if distance(makeColor(0, 42, 78), getColor(px)) < 200:
        setColor(px, makeColor(abs(r+0)/2, abs(g+42)/2, abs(b+78)/2))
      if distance(makeColor(41, 126, 159), getColor(px)) < 200:
        setColor(px, makeColor(abs(r+41)/2, abs(g+126)/2, abs(b+159)/2))
  show(pic)



def gamefy(pic):
  for x in range (0, getWidth(pic), 4):
    for y in range (0, getHeight(pic), 4):
      px = getPixel(pic, x, y)
      r = getRed(px)
      g = getGreen(px)
      b = getBlue(px)
      
      if x < getWidth(pic):
        px2 = getPixel(pic, x+1, y)
        r2 = getRed(px)
        g2 = getGreen(px)
        b2 = getBlue(px)
        
      if x+2 < getWidth(pic):
        px3 = getPixel(pic, x+2, y)
        r3 = getRed(px)
        g3 = getGreen(px)
        b3 = getBlue(px)
        
      if x+3 < getWidth(pic):
        px4 = getPixel(pic, x+3, y)
        r4 = getRed(px)
        g4 = getGreen(px)
        b4 = getBlue(px)
      
      if x < getWidth(pic) and y+1 < getHeight(pic):
        pxa = getPixel(pic, x+1, y+1)
        ra = getRed(px)
        ga = getGreen(px)
        ba = getBlue(px)
        
      if x+1 < getWidth(pic) and y+1 < getHeight(pic):
        px2a = getPixel(pic, x+1, y+1)
        r2a = getRed(px)
        g2a = getGreen(px)
        b2a = getBlue(px)
        
      if x+2 < getWidth(pic) and y+1 < getHeight(pic):
        px3a = getPixel(pic, x+1, y+1)
        r3a = getRed(px)
        g3a = getGreen(px)
        b3a = getBlue(px)
        
      if x+3 < getWidth(pic) and y+1 < getHeight(pic):
        px4a = getPixel(pic, x+1, y+1)
        r4a = getRed(px)
        g4a = getGreen(px)
        b4a = getBlue(px)
      
      if x < getWidth(pic) and y+2 < getHeight(pic):
        pxb = getPixel(pic, x+1, y+1)
        rb = getRed(px)
        gb = getGreen(px)
        bb = getBlue(px)
        
      if x+1 < getWidth(pic) and y+2 < getHeight(pic):
        px2b = getPixel(pic, x+1, y+1)
        r2b = getRed(px)
        g2b = getGreen(px)
        b2b = getBlue(px)
        
      if x+2 < getWidth(pic) and y+2 < getHeight(pic):
        px3b = getPixel(pic, x+1, y+1)
        r3b = getRed(px)
        g3b = getGreen(px)
        b3b = getBlue(px)
        
      if x+3 < getWidth(pic) and y+2 < getHeight(pic):
        px4b = getPixel(pic, x+1, y+1)
        r4b = getRed(px)
        g4b = getGreen(px)
        b4b = getBlue(px)
        
      if x < getWidth(pic) and y+3 < getHeight(pic):
        pxc = getPixel(pic, x+1, y+1)
        rc = getRed(px)
        gc = getGreen(px)
        bc = getBlue(px)
        
      if x+1 < getWidth(pic) and y+3 < getHeight(pic):
        px2c = getPixel(pic, x+1, y+1)
        r2c = getRed(px)
        g2c = getGreen(px)
        b2c  = getBlue(px)
        
      if x+2 < getWidth(pic) and y+3 < getHeight(pic):
        px3c = getPixel(pic, x+1, y+1)
        r3c = getRed(px)
        g3c = getGreen(px)
        b3c = getBlue(px)
        
      if x+3 < getWidth(pic) and y+3 < getHeight(pic):
        px4c = getPixel(pic, x+1, y+1)
        r4c = getRed(px)
        g4c = getGreen(px)
        b4c = getBlue(px)
      
      
      newR = ((r+r2+r3+r4+ra+r2a+r3a+r4a+rb+r2b+r3b+r4b+rc+r2c+r3c+r4c)/16)
      newG = ((g+g2+g3+g4+ga+g2a+g3a+g4a+gb+g2b+g3b+g4b+gc+g2c+g3c+g4c)/16)
      newB = ((b+b2+b3+b4+ba+b2a+b3a+b4a+bb+b2b+b3b+b4b+bc+b2c+b3c+b4c)/16)
            
      
      iX = x
      iY = y
      for iX in range(x, x+4):
        for iY in range(y, y+4):
          if iX < getWidth(pic) and iY < getHeight(pic):
            px = getPixel(pic, iX, iY)
            setColor(px, makeColor(newR, newG, newB))
            
      """      
      setColor(px, makeColor(newR, newG, newB))
      if x < getWidth(pic):
        setColor(px2, makeColor(newR, newG, newB))
      if x < getWidth(pic) and y < getHeight(pic):
        setColor(px3, makeColor(newR, newG, newB))
      if y < getHeight(pic):
        setColor(px4, makeColor(newR, newG, newB))
      """
      
  show(pic)
  writePictureTo(pic, r"C:\Users\rdorr\OneDrive\CSUMB\CST 205\Pictures\gamefy.jpg")
