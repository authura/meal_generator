import random

tuna_casserole = open('./Recipes/tuna_casserole.txt', 'r')
lemon_chicken = open('./Recipes/lemon_chicken.txt', 'r')
spaghetti = open('./Recipes/spaghetti.txt', 'r')
goulash = open('./Recipes/goulash.txt', 'r')
ranch_chicken_parm = open('./Recipes/ranch_chicken_parm.txt', 'r')
chicken_marsala = open('./Recipes/chicken_marsala.txt', 'r')
cheeseburgers = open('./Recipes/cheeseburgers.txt', 'r')
chicken_bacon_ranch = open('./Recipes/chicken_bacon_ranch.txt', 'r')
scooby_doo = open('./Recipes/scooby_doo.txt', 'r')
black_bean_burger = open('./Recipes/black_bean_burger.txt', 'r')
kielbasa = open('./Recipes/kielbasa.txt', 'r')
lentil_soup = open('./Recipes/lentil_soup.txt', 'r')
meatloaf = open('./Recipes/meatloaf.txt', 'r')
asian_meatballs = open('./Recipes/asian_meatballs.txt', 'r')

recipes = [tuna_casserole, lemon_chicken, spaghetti, goulash, 
ranch_chicken_parm, chicken_marsala, cheeseburgers, chicken_bacon_ranch, 
scooby_doo, black_bean_burger, kielbasa, lentil_soup, meatloaf, asian_meatballs]

random.shuffle(recipes)

for i in recipes[:1]:
    with i as f:
        f_contents = f.read()
        print(f_contents)
        f.close()
        pass