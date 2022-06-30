import random

tuna_casserole = open('./Recipes/tuna_casserole.txt', 'r')
lemon_chicken = open('./Recipes/lemon_chicken.txt', 'r')
spaghetti = open('./Recipes/spaghetti.txt', 'r')
goulash = open('./Recipes/goulash.txt', 'r')
ranch_chicken_parm = open('./Recipes/ranch_chicken_parm.txt', 'r')
chicken_marsala = open('./Recipes/chicken_marsala.txt', 'r')

recipes = [tuna_casserole, lemon_chicken, spaghetti, goulash, 
ranch_chicken_parm, chicken_marsala]

random.shuffle(recipes)

for i in recipes[:1]:
    with i as f:
        f_contents = f.read()
        print(f_contents)
        f.close()
        pass