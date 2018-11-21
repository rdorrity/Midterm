#################################################
# Ryan Dorrity, Nathan Warren-Acord
# Midterm Project
# 11/19/2018
#################################################


#################################################
# return picture
#################################################
def getPic():
  return makePicture(pickAFile())
  
#################################################
# Creates a CSUMB color effect to a photo
#################################################
def csumbfy(pic):  
  filename = "csumbfy" + ".jpg" 
  for x in range (0, getWidth(pic)):
    for y in range (0, getHeight(pic)):
      px = getPixel(pic, x, y)
      r = getRed(px)
      g = getGreen(px)
      b = getBlue(px)
      
      if x < (getWidth(pic)/3):
        setColor(px, makeColor(r*.9, g*.6, b*.5))
      elif x >= (getWidth(pic)/3) and x < (getWidth(pic)/3)*2:
        setColor(px, makeColor(r*.5, g, b*.5))
      elif x >= (getWidth(pic)/3)*2:
        setColor(px, makeColor(r*.1, g*.5, b))
      
  show(pic)
  #writePictureTo(pic, "C:\\Users\\rdorr\\OneDrive\\CSUMB\\CST 205\\Pictures\\" + filename)
 
#################################################
# Changes photo to a 64 color effect
################################################# 
def color64(pic):
  pixels = getPixels(pic)
  keys = [0,85,170,255]
  for i in pixels:
    rnew = getRed(i)
    gnew = getGreen(i)
    bnew = getBlue(i)
    rnew = min(keys, key=lambda x:abs(x-rnew))
    gnew = min(keys, key=lambda x:abs(x-gnew))
    bnew = min(keys, key=lambda x:abs(x-bnew))
    setColor(i,makeColor(rnew,gnew,bnew))
  #show (pic)
  #writePic(pic, "\CGA_LastTest3.jpg")
  return pic


#################################################
# Color effect
#################################################
def cmk(pic):
  pixels = getPixels(pic)
  keys = [0,255]
  for i in pixels:
    rnew = getRed(i)
    gnew = getGreen(i)
    bnew = getBlue(i)
    rnew = min(keys, key=lambda x:abs(x-rnew))
    if rnew == 0:
      gnew = min(keys, key=lambda x:abs(x-gnew))
      bnew = gnew
    else:
      gnew = min(keys, key=lambda x:abs(x-gnew))
      bnew = 255
    setColor(i,makeColor(rnew,gnew,bnew))
  #show (pic)
  #writePic(pic, "\CMK_LastLastTest3.png")
  return pic


#################################################
# Creates a box pixel effect
#################################################
def gamefy(pic):
  boxSize = input("Enter the number of pixels to consolidate:")
  boxDivider = boxSize**2
  filename = "gamefy" + str(boxSize) + ".jpg"  
  #filename = "\TestElise-CMK-" + str(boxSize) + ".jpg"
  for x in range (0, getWidth(pic), boxSize):
    for y in range (0, getHeight(pic), boxSize):
      iX = x
      iY = y
      r = 0
      g = 0
      b = 0
      for iX in range(x, x+boxSize):
        for iY in range(y, y+boxSize):
          if iX < getWidth(pic) and iY < getHeight(pic):
            px = getPixel(pic, iX, iY)
            r += getRed(px)
            g += getGreen(px)
            b += getBlue(px)
      
      newR = r/boxDivider
      newG = g/boxDivider
      newB = b/boxDivider
      
      iX = x
      iY = y
      for iX in range(x, x+boxSize):
        for iY in range(y, y+boxSize):
          if iX < getWidth(pic) and iY < getHeight(pic):
            px = getPixel(pic, iX, iY)
            setColor(px, makeColor(newR, newG, newB))
  colorMode = raw_input("Enter 'cmk' for 4 color palette or anything else for 64 color palette:")
  if colorMode.isalpha() and colorMode.lower() == "cmk":
    pic = cmk(pic)
  else:
    pic = color64(pic)
  show(pic)
  #writePictureTo(pic, "C:\\Users\\rdorr\\OneDrive\\CSUMB\\CST 205\\Pictures\\" + filename)
  #writePictureTo(pic, "C:\Users\NAcor\Desktop\CSCI School\CST 205\CST205 - Midterm" + filename)