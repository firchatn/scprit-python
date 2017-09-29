from PIL import Image
from PIL import ImageChops

im1 = Image.open("img1.png")
im2 = Image.open("img2.png")
diff = ImageChops.difference(im1,im1) 
print(type(diff))
if not diff.getbbox():
    print("equal")
diff.show()
print(diff)
