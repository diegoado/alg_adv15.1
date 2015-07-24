# -*- coding: utf-8 -*-
 
# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados
  
# Problema: Fatorial de Novo!
# Nivel: 4

def fatorial(n):
    if n < 1:
        return 1
    
    return n * fatorial(n - 1)

while 1:
    n = raw_input()
    if n == '0': break
    
    dec = 0
    x = len(n)
    for i in range(x):
        dec += int(n[i]) * fatorial(x)
        x -= 1
    
    print dec