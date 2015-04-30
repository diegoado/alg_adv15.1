# -*- coding: utf-8 -*-
   
# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados
    
# Problema: Camisetas
# Nivel: 3

cases = int(raw_input())
empty = raw_input()
trees = []

for i in range(cases):   
    d = {}
    while 1:
        try:
            tree = raw_input()
        except EOFError:
            break
        
        if tree == empty: break
        else: 
            if d.has_key(tree):
                d[tree] += 1
            else:
                d[tree] = 1
    
    if len(d) != 0:
        trees.append(d)

for i in range(len(trees)):
    
    soma = sum(trees[i].values())
    lista = trees[i].keys()
    lista.sort()
    
    for j in range(len(lista)):
        print '%s %.4f' % (lista[j], trees[i].get(lista[j])*100.0/soma)
    
    if i + 1 != len(trees):
        print ''