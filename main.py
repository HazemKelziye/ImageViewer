import cv2
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os

# this is the way to open an image using Opencv Lib
# cv2.IMREAD_UNCHANGED to open the image as it is
# include the image file in the project folder

img1 = cv2.imread("images/Rubik1.jpeg", cv2.IMREAD_UNCHANGED)
img2 = cv2.imread("images/Rubik2.jpeg", cv2.IMREAD_UNCHANGED)
img3 = cv2.imread("images/Rubik3.jpeg", cv2.IMREAD_UNCHANGED)
img4 = cv2.imread("images/Rubik4.jpeg", cv2.IMREAD_UNCHANGED)
img5 = cv2.imread("images/FamousIm.png", cv2.IMREAD_UNCHANGED)

resized_img1 = cv2.resize(img1, (750,750), interpolation= cv2.INTER_LINEAR)
resized_img2 = cv2.resize(img2, (750,750), interpolation= cv2.INTER_LINEAR)
resized_img3 = cv2.resize(img3, (750,750), interpolation= cv2.INTER_LINEAR)
resized_img4 = cv2.resize(img4, (750,750), interpolation= cv2.INTER_LINEAR)
resized_img5 = cv2.resize(img5, (750,750), interpolation= cv2.INTER_LINEAR)
#

# Note!
# OpenCV uses BGR image format. So, when we read an image using cv2.
# imread() it interprets in BGR format by default.
# We can use cvtColor() method to convert a BGR image to RGB and vice-versa
# But since we can convert direcrtly from BGR to HSV so...

# Converting from BGR/RGB to HSV/HSI
hsv_img1 = cv2.cvtColor(resized_img1, cv2.COLOR_BGR2HSV)
rgb_img1 = cv2.cvtColor(resized_img1, cv2.COLOR_BGR2RGB)

hsv_img2 = cv2.cvtColor(resized_img2, cv2.COLOR_BGR2HSV)
rgb_img2 = cv2.cvtColor(resized_img2, cv2.COLOR_BGR2RGB)

hsv_img3 = cv2.cvtColor(resized_img3, cv2.COLOR_BGR2HSV)
rgb_img3 = cv2.cvtColor(resized_img3, cv2.COLOR_BGR2RGB)

hsv_img4 = cv2.cvtColor(resized_img4, cv2.COLOR_BGR2HSV)
rgb_img4 = cv2.cvtColor(resized_img4, cv2.COLOR_BGR2RGB)

hsv_img5 = cv2.cvtColor(resized_img5, cv2.COLOR_BGR2HSV)
rgb_img5 = cv2.cvtColor(resized_img5, cv2.COLOR_BGR2RGB)
# This creates a GUI window with a title name of your choice

LastListRGB = [rgb_img1, rgb_img2, rgb_img3, rgb_img4, rgb_img5]
LastListHSV = [hsv_img1, hsv_img2, hsv_img3, hsv_img4, hsv_img5]
# cv2.imshow("HSV Mecca",hsv_img)
# cv2.imshow("RGB Mecca", img)

# specified number is the time in milliseconds
# if you pass 0 as an argument it will not close unless you do so

# cv2.waitKey(0)

# cv2.destroyAllWindows()

# Accessing a single pixel value in OpenCV
# In our case we are going to access the Voxel since it has 3-channels
print(f"This is the value of voxel at (0,0): {img1[250, 250]} for the BGR Image")
#print(f"This is the value of voxel at (0,0): {resized_img1[250, 250]} for the RGB Image")
print(f"This is the value of voxel at (0,0): {hsv_img1[0, 0]} for the HSV Converted Image")

#Getting my hands dirty with Tkinter


root = Tk()
# root.geometry("800x600+300+150")
root.resizable(width=True, height=True)

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
TkImageRGB1 = Image.fromarray(rgb_img1)
TkinterRGB1 = ImageTk.PhotoImage(image=TkImageRGB1)
TkImageHSV1 = Image.fromarray(hsv_img1)  # Converting the image from Opencv format to Pillow format
TkinterHSV1 = ImageTk.PhotoImage(image=TkImageHSV1)

TkImageRGB2 = Image.fromarray(rgb_img2)
TkinterRGB2 = ImageTk.PhotoImage(image=TkImageRGB2)
TkImageHSV2 = Image.fromarray(hsv_img2)  # Converting the image from Opencv format to Pillow format
TkinterHSV2 = ImageTk.PhotoImage(image=TkImageHSV2)

TkImageRGB3 = Image.fromarray(rgb_img3)
TkinterRGB3 = ImageTk.PhotoImage(image=TkImageRGB3)
TkImageHSV3 = Image.fromarray(hsv_img3)  # Converting the image from Opencv format to Pillow format
TkinterHSV3 = ImageTk.PhotoImage(image=TkImageHSV3)

TkImageRGB4 = Image.fromarray(rgb_img4)
TkinterRGB4 = ImageTk.PhotoImage(image=TkImageRGB4)
TkImageHSV4 = Image.fromarray(hsv_img4)  # Converting the image from Opencv format to Pillow format
TkinterHSV4 = ImageTk.PhotoImage(image=TkImageHSV4)

TkImageRGB5 = Image.fromarray(rgb_img5)
TkinterRGB5 = ImageTk.PhotoImage(image=TkImageRGB5)
TkImageHSV5 = Image.fromarray(hsv_img5)  # Converting the image from Opencv format to Pillow format
TkinterHSV5 = ImageTk.PhotoImage(image=TkImageHSV5)

image_list_rgb = [TkinterRGB1, TkinterRGB2, TkinterRGB3, TkinterRGB4, TkinterRGB5]
image_list_hsv = [TkinterHSV1, TkinterHSV2, TkinterHSV3, TkinterHSV4, TkinterHSV5]

current = 0

status = IntVar()
status.set(0)

print("value of status",status.get())

temp = 0

coorLabel = Label(root, text="Pixel value")
coorLabel2 = Label(root, text="Pixel value2")

#Only the Size/shape is left to be adjusted

def displayCoordinates(event):
    global temp
    temp +=1

    if status.get() == 0:
        if temp%2 == 1:
            coorLabel['text'] = "The pixel ("+str(event.x)+","+str(event.y)+") "+"and the value is:"+str(LastListRGB[current][event.x,event.y])
        else:
            coorLabel2['text'] = "The pixel ("+str(event.x)+","+str(event.y)+") "+"and the value is:"+str(LastListRGB[current][event.x,event.y])
    else:
        if temp%2 == 1:
            coorLabel['text'] = "The pixel ("+str(event.x)+","+str(event.y)+") "+"and the value is:"+str(LastListHSV[current][event.x,event.y])
        else:
            coorLabel2['text'] = "The pixel ("+str(event.x)+","+str(event.y)+") "+"and the value is:"+str(LastListHSV[current][event.x,event.y])


def clicked():
    global current
    global my_label

    my_label.grid_forget()

    if status.get()==0:
        my_label = Label(image=image_list_rgb[current])
    else:
        my_label = Label(image=image_list_hsv[current])

    my_label.bind('<Button-1>', displayCoordinates)
    my_label.grid(row=0, column=1)
    coorLabel.grid(row=7, column=1)
    coorLabel2.grid(row=8, column=1)


Radiobutton(root, text="Convert to HSV domain", variable=status, value=1, command=clicked).grid(row=2, column=1)
Radiobutton(root, text="Convert to RGB domain", variable=status, value=0, command=clicked).grid(row=3, column=1)

if status.get() == 0:
    my_label = Label(image=TkinterRGB1)
else:
    my_label = Label(image=TkinterHSV1)

my_label.grid(row=0, column=1)
my_label.bind('<Button-1>', displayCoordinates)
coorLabel.grid(row=7, column=1)
coorLabel2.grid(row=8, column=1)

#my_label.bind('<Button-1>', displayCoordinates)


def forward(image_number):
    global my_label
    global button_forward
    global button_back
    global current

    current = image_number + 1

    if current == 5:
        current = 0

    my_label.grid_forget()
    if status.get()==0:
        my_label = Label(image=image_list_rgb[current])
    else:
        my_label = Label(image=image_list_hsv[current])

    button_forward = Button(root, text=">>", command=lambda: forward(current))
    button_back = Button(root, text="<<", command=lambda: back(current))

    my_label.bind('<Button-1>', displayCoordinates)
    my_label.grid(row=0, column=1)
    coorLabel.grid(row=7, column=1)
    coorLabel2.grid(row=8, column=1)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)

def back(image_number):
    global my_label
    global button_forward
    global button_back
    global current

    current = image_number -1

    if current == -1:
        current = 4

    my_label.grid_forget()
    if status.get()==0:
        my_label = Label(image=image_list_rgb[current])
    else:
        my_label = Label(image=image_list_hsv[current])

    button_forward = Button(root, text=">>", command=lambda: forward(current))
    button_back = Button(root, text="<<", command=lambda: back(current))

    my_label.bind('<Button-1>', displayCoordinates)
    my_label.grid(row=0, column=1)
    coorLabel.grid(row=7, column=1)
    coorLabel2.grid(row=8, column=1)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)


button_forward = Button(root, text=">>", command=lambda: forward(0))
button_back = Button(root, text="<<", command=back)
exit_button = Button(root, text="Exit program", command=root.quit)

exit_button.grid(row=1, column=1)
button_back.grid(row=1, column=0)
button_forward.grid(row=1, column=2)
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