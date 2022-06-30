tuna_casserole = open('./Recipes/tuna_casserole.txt', 'r')
lemon_chicken = open('./Recipes/lemon_chicken.txt', 'r')
spaghetti = open('./Recipes/spaghetti.txt', 'r')

with spaghetti as f:
    f_contents = f.read()
    print(f_contents)
    f.close()
    pass