#!/usr/bin/python

import math

test_recipe = {'milk': 100, 'butter': 50, 'flour': 5}
test_ingredients = {'milk': 132, 'butter': 48, 'flour': 51}

def recipe_batches(recipe, ingredients):
  recipe_keys = list(recipe.keys())
  ingredients_keys = list(ingredients.keys())
  if len(recipe_keys) != len(ingredients_keys):
    return 0 
  min_batches = []
  for key in recipe_keys: 
    ingredient_min_batch = ingredients[key] // recipe[key]
    if ingredient_min_batch == 0:
      return 0
    else:
      min_batches.append(ingredient_min_batch)
  return(min(min_batches))

print(recipe_batches(test_recipe, test_ingredients))

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))