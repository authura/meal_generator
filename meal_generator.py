tuna_casserole = open('./Recipes/tuna_casserole.txt', 'r')

with tuna_casserole as f:
    f_contents = f.read()
    print(f_contents)
    f.close()
    pass