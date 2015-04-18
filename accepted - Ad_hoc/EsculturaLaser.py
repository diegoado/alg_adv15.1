# -*- coding: utf-8 -*-
  
# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados
  
# Problema: Escultura à Laser
# Nivel: 3
  
  
while 1:
    a, c = map(int, raw_input().split())
    if a==0 and c==0: break
     
    l = map(int, raw_input().split())
    l.insert(0, a)
     
    s = 0
    for i in range(1, c+1):
        if l[i] < l[i-1]:
            s += l[i-1] - l[i]
             
    print s