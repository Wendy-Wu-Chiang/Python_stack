import random
def randInt(min=0 , max=100 ):
    possible_range = max-min
    return round(random.random() * possible_range + min) 
# print(randInt())
# print(randInt(max=50))
# print(randInt(min=50))
# print(randInt(min=50, max=500))