# from PIL import Image
# from colorit import init_colorit, background

# init_colorit()
# image = Image.open("unamed.jpg")

# depth = int(input("Write the depth: "))
# image = image.resize((depth, depth))

# for y in range(image.size[1]) :
#     for x in range(image.size[0]) :
#         print(background(" ", image.getpixel((x,y))), end="")
#     print()


    
# importing Image class from PIL package 
from PIL import Image 
 
# creating a object 
im = Image.open(r"../image/try1.jpg") 
 
im.show()