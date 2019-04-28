import generations

Target = "meow"
length = len(Target)

generation_instance  = generations.Generations(length)

generation_instance.fitnessfunction(Target)

max_score = 0
local_peak = ""
best_uptil_now = generation_instance.generation

while(generation_instance.score != length):
    
    if(generation_instance.score > max_score):
        max_score = generation_instance.score
        best_uptil_now = generation_instance.generation
        print("Best uptil now : ",best_uptil_now," Score : ",max_score)

    if(generation_instance.score==max_score):
        generation_instance.mutate_gen()
        generation_instance.fitnessfunction(Target)
    elif(generation_instance.score>0 and generation_instance.score<max_score):
        generation_instance.generation = best_uptil_now
        generation_instance.mutate_gen()
        generation_instance.fitnessfunction(Target)
    else:
        generation_instance.create_next_gen()
        generation_instance.fitnessfunction(Target)

print(generation_instance.generation)