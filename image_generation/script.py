import cv2
import numpy as np
from generations import Generations
import sys
import os

image1 = cv2.imread('F:\LetsCode\HillClimbAlgo\image_generation\Mona.jpg')
length,breadth,colours = image1.shape

generation_instance = Generations(length,breadth)

generation_instance.fitness_function(image1)

max_score = generation_instance.score
best_untill_now = generation_instance.generation
c = 1

while(generation_instance.score< 0.95):

    if(generation_instance.score > max_score):
        max_score = generation_instance.score
        best_uptil_now = generation_instance.generation
        cv2.imwrite("Image"+str(c)+".jpg",generation_instance.generation)
        print(generation_instance.score)
        c+=1

    if(generation_instance.score==max_score):
        generation_instance.mutate_gen(image1)
        
    elif(generation_instance.score>0 and generation_instance.score<max_score):
        generation_instance.generation = best_uptil_now
        generation_instance.mutate_gen(image1)
        
    else:
        generation_instance.create_next_gen(image1)
        
cv2.imwrite("Final_Image.jpg",generation_instance.generation)
