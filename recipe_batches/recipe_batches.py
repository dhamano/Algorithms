#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    max_batch = 0
    keys = []

    if len(recipe) > len(ingredients):
        return 0

    for key in recipe.keys():
        keys.append(key)

    for i in range(0, len(recipe)):
        cur_key = keys[i]
        count = math.floor(ingredients[cur_key] / recipe[cur_key])
        if count < 1:
            return 0
        
        if i == 0:
            max_batch = count
        elif (count < max_batch):
            max_batch = count

    return max_batch


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))