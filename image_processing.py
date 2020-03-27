from PIL import Image
img = Image_open('new.png')
tran_img = img.transpose(Image_FLIP_LEFT_RIGHT)
tran_img.save("corrected.png")
print('dine file')
