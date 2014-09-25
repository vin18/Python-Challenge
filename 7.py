from PIL import Image
import os.path


img = Image.open("oxygen.png")
width, height = img.size
#print ("Dimensions:", img.size, "Total pixels:", width * height)
img = img.crop((0,45,610,50))
pic = img.convert('RGB')
for i in range(0,608,7):
    R,G,B  = pic.getpixel((i, 0))
    L = 0.2125 * R + 0.7154 * G + 0.0721 * B
    print(chr(int(L)),end="")
#img.show()
nextL = [105, 110, 116, 101, 103, 114, 105, 116, 121]
for L in nextL:
    print(chr(int(L)),end="")
