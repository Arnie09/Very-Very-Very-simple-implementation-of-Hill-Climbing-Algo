import random

def getChar():
    c=random.randint(63,122)
    if c == 63 :
        c=32
    if c == 64:
	    c=46	
    return chr(c)

class Generations:
    
    '''constructor'''
    def __init__(self,length):
        self.length = length
        self.score = 0
        self.generation = ""

        '''to fill frst generation'''
        for i in range(self.length):
            self.generation+=getChar()

    def fitnessfunction(self,target):
        for i in range(self.length):
            if(self.generation[i] == target[i]):
                self.score+=1
    
    def create_next_gen(self):
        self.generation = ""
        for i in range(self.length):
            self.generation+=getChar()
        self.score = 0
    
    def mutate_gen(self):
        random_position = random.randint(0,self.length-1)
        self.generation = self.generation.replace(self.generation[random_position], getChar())
        self.score = 0
    
    