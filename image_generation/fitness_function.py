import cv2
import numpy as np

fitness = 0

image1 = cv2.imread('F:\LetsCode\HillClimbAlgo\image_generation\dnld.jpg')


image2 = cv2.imread('F:\LetsCode\HillClimbAlgo\image_generation\dnld.1.jpg')
# length,breadth,depth = image1.shape
# image2 = np.zeros((length, breadth,3), dtype = "uint8")

delta_red = image1[:,:,2] - image2[:,:,2]
delta_blue = image1[:,:,0] - image2[:,:,0]
delta_green = image1[:,:,1] - image2[:,:,1]

fitness = np.sum(delta_red*delta_red+delta_blue*delta_blue+delta_green*delta_green)


# height = image1.shape[0]
# width = image1.shape[1]
# for x in range(height):
#     for y in range(width):
#         color1 = image1[x][y]
#         color2 = image2[x][y]

#         delta_blue = color1[1] - color2[1]
#         delta_green = color1[2] - color2[2]
#         delta_red = color1[0] - color2[0]

#         pixel_fitness = delta_red*delta_red + delta_green*delta_green + delta_blue*delta_blue

#         fitness+=pixel_fitness

print(fitness)



