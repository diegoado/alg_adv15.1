# -*- coding: utf-8 -*-
    
# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados
     
# Problema: Fibonacci, Quantas Chamadas?
# Nivel: 2

MAX = 50
global memory

memory = [-1] * MAX

def fib(n):
    if memory[n] != -1:
        return memory[n]
    
    if n == 0:
        memory[n] = 0
        return 0
    
    elif n == 1:
        memory[n] = 1
        return 1
    
    else:
        memory[n] = fib(n - 1) + fib(n - 2)
        return memory[n]

def calls(x):
    if x == 1:
        return 0
    
    return (2*memory[x] - 2 + 2*memory[x-1] - 2) + 2 
    
n = int(raw_input())

for i in xrange(n):
    x = int(raw_input())
    fib(x)

    print 'fib(%d) = %d calls = %d' % (x, calls(x), memory[x])
