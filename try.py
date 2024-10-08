recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
def cakes(recipe, available):
    possible_cakes_list = []
    
    for ingredient, amount_needed in recipe.items():
        if ingredient in available:
            possible_cakes = available[ingredient] // amount_needed
            possible_cakes_list.append(possible_cakes)
        else:
            return 0
    
    return min(possible_cakes_list)

print(cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}))



    
    
def cakes(recipe, available):
    
    for i,k in recipe.items():
        for m,n in available:
            result = 

cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
