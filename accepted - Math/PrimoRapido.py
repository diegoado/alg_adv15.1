# -*- coding: utf-8 -*-
  
# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados
   
# Problema: Primo Rápido
# Nivel: 2
 
def isPrime(x):
    if x == 2:
        return True
     
    for i in range(3, int(x**0.5)+1, 2):
        if x % i == 0:
            return False
    return True
 
     
n = int(raw_input())
for i in range(n):
    x = int(raw_input())
    if isPrime(x):
        print'Prime'
    else:
        print'Not Prime'