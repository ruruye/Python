from random import random
def getRandomHoll():
    
    rnd = random()    
    if rnd > 0.5:
        return "홀"
    else:
        return "짝"



com = getRandomHoll()
print("com", com)