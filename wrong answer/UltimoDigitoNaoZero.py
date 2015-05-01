# -*- coding: utf-8 -*-
 
# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados
  
# Problema: O Último Dígito Não-Zero 
# Nivel: 5

from math import factorial

def permutation(n, r):
    return str(factorial(n)/factorial(n-r))

while 1:
    try:
        m, n = map(long, raw_input().split())
    except EOFError:
        break
        
    i = -1
    b = True
    x = permutation(m, n)
    
    for i in range(1, len(x)+1):
        if x[-i] != '0':
            print x[-i]
            break