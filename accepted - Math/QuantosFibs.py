# -*- coding: utf-8 -*-
 
# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados
  
# Problema: Quantos Fibs
# Nivel: 3

def fibonacci():
    a, b = 1, 2
    
    while 1:
        yield a
        a, b = b, a+b
    
while 1:
    a, b = map(long, raw_input().split())
    if a == 0 and b == 0: break
    
    n = 0
    fib = fibonacci()
    while 1:
        x = fib.next()
        if x > b: break
        
        if x >= a and x <= b:
            n += 1
            
    print n