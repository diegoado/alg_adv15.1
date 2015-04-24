# -*- coding: utf-8 -*-
   
# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados
    
# Problema: Ones
# Nivel: 4
 
def answer(n):
    count = 1
    x = 10 % n
    y = 1
     
    while (x * y)  % n != 0:
        y = (x * y) % n + 1
        count += 1
         
    return count
  
while 1:
    try:
        n = int(raw_input())
        print answer(n)
    except EOFError:
        break