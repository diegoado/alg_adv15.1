# -*- coding: utf-8 -*-
    
# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados
     
# Problema: Lucro
# Nivel: 3

global memory
global recipe

def solve(i):
    if memory[i] != -1:
        return memory[i]
    
    if i == 0:
        memory[0] = recipe[0]
        return memory[0]
    
    memory[i] = max(solve(i-1) + recipe[i], recipe[i])
    return memory[i]

recipe_max = 0
recipe = []

while 1:
    try:
        n = int(raw_input())
        cost = int(raw_input())
        
        for i in xrange(n):
            x = int(raw_input())
            recipe.append(x - cost)
        
        memory = [-1] * len(recipe)
        
        for i in range(len(recipe)):
            result = solve(i)
            
            if result > recipe_max:
                recipe_max = result
        
        print recipe_max
        recipe_max = 0
        recipe = []
    except EOFError:
        break

    
