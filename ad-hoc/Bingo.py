# -*- coding: utf-8 -*-
  
# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados
  
# Problema: Bingo!
# Nivel: 3
  
def isPossible(n, b, l):
    x = [0]*(n+1)
    for i in range(b):
        for j in range(i, b):
            x[abs(l[i]-l[j])] = 1
     
    if 0 in x:
        return False
    return True
  
while 1:
    n, b = map(int, raw_input().split())
    if n==0 and b==0: break
      
    l = map(int, raw_input().split())
      
    p = isPossible(n, b, l)
      
    if p:
        print'Y'
    else:
        print'N'