from PIL import Image
import os.path


img = Image.open("cave.jpg")
width, height = img.size
print ("Dimensions:", img.size, "Total pixels:", width * height)
pixels = img.load()

pixelsList = list(img.getdata())
listOdd = pixelsList[1::2][::2]
print(str(len(listOdd)))
print(str((int(width/2)*int(height/2))))
print(str(len(pixelsList)))
listEven = pixelsList[::2][1::2]

imOdd = Image.new(img.mode, (int(width/2),int(height/2)))
imOdd.putdata(listOdd)

imEven = Image.new(img.mode, (int(width/2),int(height/2)))
imEven.putdata(listEven)


imEven.show()
imOdd.show()
img.show()

