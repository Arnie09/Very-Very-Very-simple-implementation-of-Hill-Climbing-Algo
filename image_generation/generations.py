import cv2
from skimage import measure
import numpy as np
import random

def createEllipses(img,length,breadth):
    '''for generating semi-transaparent rectangles'''
    overlay = img.copy()
    output = img.copy()

    '''generating x and y coordinates of the centre of the ellipse'''
    centre_x = random.randint(0,length)
    centre_y = random.randint(0,breadth)

    '''generating RGB values'''
    red_ = random.randint(0,255)
    green_ = random.randint(0,255)
    blue_ = random.randint(0,255)

    '''generating the size of the ellipse'''
    major_axis = random.randint(0,length//3)
    minor_axis = random.randint(0,breadth//3)

    '''drawing the ellipse'''
    cv2.ellipse(overlay,(centre_x,centre_y),(major_axis,minor_axis),0,0,360,(red_,green_,blue_),-1)
    
    '''applying transaprency to the drawn ellipse'''
    cv2.addWeighted(overlay,0.5,output,0.5,0,img)

class Generations:

    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
        self.score = 0
        self.generation = np.zeros((length, breadth, 3), dtype = "uint8")
        
        '''creating the first generation'''
        createEllipses(self.generation,self.length,self.breadth)

    def fitness_function(self,image1):

        image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
        image2 = cv2.cvtColor(self.generation, cv2.COLOR_BGR2GRAY)

        self.score = measure.compare_ssim(image1,image2)

    def create_next_gen(self,image1):

        self.generation = np.zeros((length, breadth, 3), dtype = "uint8")
        createEllipses(self.generation,self.length,self.breadth)
        self.fitness_function(image1)

    def mutate_gen(self,image1):

        createEllipses(self.generation,self.length,self.breadth)
        self.fitness_function(image1)
        