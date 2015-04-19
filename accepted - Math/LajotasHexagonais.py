# -*- coding: utf-8 -*-
 
# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados
  
# Problema: Lajotas Hexagonais
# Nivel: 2

def fibonacci():
    a, b = 1, 2
    
    while 1:
        yield a
        a, b = b, a+b
        
while 1:
    n = int(raw_input())
    if n == 0: break
    
    x = 0
    fib = fibonacci()
    for i in range(n):
        x = fib.next()
        
    print x
        