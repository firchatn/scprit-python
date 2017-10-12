from PIL import Image
from PIL import ImageChops

im1 = Image.open("images/img1.png")
im2 = Image.open("images/img2.png")
diff = ImageChops.difference(im1,im2) 
if not diff.getbbox():
    print("equal")
else:
    print("different see the diff")
diff.show()
