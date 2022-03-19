import cv2
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os

# this is the way to open an image using Opencv Lib
# cv2.IMREAD_UNCHANGED to open the image as it is
# include the image file in the project folder

img = cv2.imread("Mecca.jpeg", cv2.IMREAD_UNCHANGED)
img2 = cv2.imread("MePlusMyHand.jpeg", cv2.IMREAD_UNCHANGED)
# Note!
# OpenCV uses BGR image format. So, when we read an image using cv2.
# imread() it interprets in BGR format by default.
# We can use cvtColor() method to convert a BGR image to RGB and vice-versa
# But since we can convert direcrtly from BGR to HSV so...

# Converting from BGR/RGB to HSV/HSI
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

hsv_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
# This creates a GUI window with a title name of your choice

# cv2.imshow("HSV Mecca",hsv_img)
# cv2.imshow("RGB Mecca", img)

# specified number is the time in milliseconds
# if you pass 0 as an argument it will not close unless you do so

# cv2.waitKey(0)

# cv2.destroyAllWindows()

# Accessing a single pixel value in OpenCV
# In our case we are going to access the Voxel since it has 3-channels
print(f"This is the value of voxel at (0,0): {img[0, 0]} for the BGR Image")
print(f"This is the value of voxel at (0,0): {rgb_img[0, 0]} for the RGB Image")
print(f"This is the value of voxel at (0,0): {hsv_img[0, 0]} for the HSV Converted Image")

#Getting my hands dirty with Tkinter


root = Tk()
# root.geometry("800x600+300+150")
root.resizable(width=True, height=True)
root.geometry("500x500")

# def openfn():
#     '''Accessing the file name extension'''
#     filename = filedialog.askopenfilename(title="open")
#     return filename

#
# def open_image():
#     '''Opening an Image'''
#     x = openfn()
#     TkImage = Image.open(x)
#     # TkImage = TkImage.resize((1200, 1200), Image.ANTIALIAS)
#     TkImage = ImageTk.PhotoImage(TkImage)
#     panel = Label(root, image=TkImage)
#     panel.image = TkImage
#     panel.grid(root, row=0, column=0)


# To convert images from Opencv dataType to Pillow dataType use Image.fromarray()
# Since PIL reads the image as RGB we cant call the img instance
# We will call the rgb_img
TkImageRGB = Image.fromarray(rgb_img)
TkinterRGB = ImageTk.PhotoImage(image=TkImageRGB)
Label(root, image= TkinterRGB).grid(row=0, column=0)

TkImageHSV = Image.fromarray(hsv_img)  # Converting the image from Opencv format to Pillow format
TkinterHSV = ImageTk.PhotoImage(image=TkImageHSV)
Label(root, image= TkinterHSV).grid(row=0, column=1)

TkImageRGB2 = Image.fromarray(rgb_img2).resize((380,500))
TkinterRGB2 = ImageTk.PhotoImage(image=TkImageRGB2)
Label(root, image= TkinterRGB2).grid(row=1, column=0)

TkImageHSV2 = Image.fromarray(hsv_img2).resize((380,500))
TkinterHSV2 = ImageTk.PhotoImage(image=TkImageHSV2)
Label(root, image= TkinterHSV2).grid(row=1, column=1)

# Label(root, image=TkinterHSV).pack()
# def print_location(event):
#     # print(f' location of x={event.x}, location of y ={event.y}')
#     a = event.x
#     b = event.y
#     # Label(root, text=f"The voxel value at{a},{b} is = {img[a, b]}").pack()
#     Label(root, text=f"The voxel value at{a},{b} is = {img[a, b]}").pack()
#
#
# btn = Button(root, text="open image", padx=50, command=open_image).pack()
# root.bind("<Button-1>", print_location)

root.mainloop()