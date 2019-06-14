import cv2
import random
import matplotlib.pyplot as  plt
import numpy as np
import sys
import os

colors = []

'''for generating shapes'''
def createShapes(img,length,breadth,image1):
    
    # overlay = img.copy()
    # output = img.copy()

    '''storing all the colours of the picture'''
    '''more a colour is present, more will it be present in the array and greater is its probability of getting selected'''
    if len(colors) == 0 :
        for i in range(length):
            for j in range(breadth):
                colors.append(image1[i][j])

    '''generating x and y coordinates of the centre of the circles'''
    centre_x = random.randint(0,length)
    centre_y = random.randint(0,breadth)

    '''ideally for a small image keep the radius of the circles more than 3 pixels'''
    radius = random.randint(length/30,length)

    '''generating RGB values'''
    rgb = list(random.choice(colors))
    
    # '''generating the size of the ellipse'''
    # major_axis = random.randint(length//10,length)
    # minor_axis = random.randint(breadth//10,breadth)

    # angle = random.randint(0,360)

    # '''drawing the ellipse'''
    # cv2.ellipse(overlay,(centre_x,centre_y),(major_axis,minor_axis),angle,0,360,(int(rgb[0]),int(rgb[1]),int(rgb[2])),-1)

    '''generating circle'''
    cv2.circle(img,(centre_x,centre_y),radius,(int(rgb[0]),int(rgb[1]),int(rgb[2])),-1)
    
    # '''applying transaprency to the drawn ellipse'''
    # cv2.addWeighted(overlay,0.5,output,0.5,0,img)

    return img


class Generations:

    def __init__(self,length,breadth,depth,image1):
        self.length = length
        self.breadth = breadth
        self.children = []
        self.children_score = {}
        self.generation_no = 1
        
        '''population represents the best image of a mating pool'''
        self.population = (np.zeros((length, breadth,3), dtype = "uint8"))
        '''best score of the population'''
        self.score = self.fitness_function(image1,self.population)
            
    '''fitness function generates the fitness or how close a generated image looks to the original image'''
    def fitness_function(self,image1,image2):

        fitness = 0

        delta_red = image1[:,:,2] - image2[:,:,2]
        delta_blue = image1[:,:,0] - image2[:,:,0]
        delta_green = image1[:,:,1] - image2[:,:,1]

        fitness = np.sum(delta_red*delta_red+delta_blue*delta_blue+delta_green*delta_green)

        return fitness

    '''function to choose the best image in the children to see if its better than the parent'''
    '''if yes then the parent is replaced, if not then it is discarded'''
    def find_next_offspring(self):
        self.generation_no+=1

        list_of_scores = list(self.children_score.values())
        list_of_children = list(self.children_score.keys())
        minimum_score = min(list_of_scores)
        child_with_best_score  = self.children[list_of_scores.index(min(list_of_scores))]

        if(minimum_score<self.score):
            
            self.population = child_with_best_score
            self.score = minimum_score
            cv2.imwrite("image"+str(self.generation_no)+".jpg",self.population)
            print(self.generation_no)
        
    '''best image among 5 children are choosen, 5 us a random number though'''
    '''yet to test how increasing number of children affects the test'''
    '''50 mutations are done on each child and the best mutation is kept'''
    def mutate_gen(self,image1):

        self.children =[]
        self.children_score = {}
        for i in range(0,5):
            best_so_far = self.population
            score = 99999999999999999
            for j in range(50):
                copy = self.population.copy()
                mutated_child = (createShapes(copy,self.length,self.breadth,image1))
                score_of_mutate = self.fitness_function(mutated_child,image1)
                if score_of_mutate<score:
                    best_so_far = mutated_child
                    score = score_of_mutate
            self.children.append(best_so_far)
            self.children_score[i] = score

image1 = cv2.imread('F:\LetsCode\HillClimbAlgo\image_generation\landscape.jpg')

length,breadth,depth = image1.shape

generation_instance = Generations(length,breadth,depth,image1)

'''the lower the score the better the result'''
while(generation_instance.score>5000):
    generation_instance.mutate_gen(image1)
    generation_instance.find_next_offspring()

