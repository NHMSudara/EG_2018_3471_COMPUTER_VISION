
#Take Home Assignment 1
#Sudara N.H.M -EG/2018/3471



import cv2
import numpy as np 
import matplotlib.pyplot as plt 
import skimage
from skimage import data
from skimage.transform import rotate





image = data.camera() #read the image
print(image.shape)



#----part 01------


def reduce_intensity_levels(image, levels):
    steps = pow(2,levels)
    print(steps)
   
    reduced_image= np.array(np.floor(image/(256/steps))*(256/steps))
    return reduced_image
 
   
    
level=input("Enter level in integer powers of 2:") #get input level in integer powers of 2
if (int(level)>0 and int(level)<9):
    plt.gray()
    f,arr = plt.subplots(1,2)
    reduced = reduce_intensity_levels(image,int(level)) 
    arr[0].imshow(image)
    arr[1].imshow(reduced) #show reduced image
    arr[0].set_title(' Original image')
    arr[1].set_title('{} intensity levels'.format(pow(2,int(level))))
else :
    print("invalid number")




#----part 02------


f,arr=plt.subplots(1,4)
image3k=cv2.blur(image,(3,3))
image10k=cv2.blur(image,(10,10))
image20k=cv2.blur(image,(20,20))

arr[0].imshow(image)
arr[1].imshow(image3k)
arr[2].imshow(image10k)
arr[3].imshow(image20k)

arr[0].set_title(' Original image')
arr[1].set_title(' spatial 3x3')
arr[2].set_title(' spatial 10x10')
arr[3].set_title(' spatial 20x20')


#----part 03------

rotated_image_45 = rotate(image, 45,resize=True)
rotated_image_90 = rotate(image, 90,resize=True)


f,arr=plt.subplots(1,2)
arr[0].imshow(rotated_image_45)
arr[1].imshow(rotated_image_90)
arr[0].set_title('45 degree rotated')
arr[1].set_title('90 degree rotated')


#----part 04------

block = (3,5,7)
rows,cols = image.shape[0],image.shape[1]

f, arr = plt.subplots(1, len(block))
for i,B in enumerate(block):
    image_mod = image.copy()
    for r in range(round(B/2),rows,B):
        for c in range(round(B/2),cols,B):
            image_mod[r-round(B/2):r+round(B/2)+1,c-round(B/2):c+round(B/2)+1] = np.average(image[r-round(B/2):r+round(B/2)+1,c-round(B/2):c+round(B/2)+1])
    arr[i].imshow(image_mod);
    arr[i].set_title('{}x{} average block'.format(B,B))

print(image_mod)
