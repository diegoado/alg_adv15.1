# -*- coding: utf-8 -*-
    
# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados
     
# Problema: Comércio de Vinhos na Gergóvia
# Nivel: 2

while 1:
    n = int(raw_input())
    if n == 0: break
    
    l = map(int, raw_input().split())
    
    t = 0
    for i in xrange(1, n):
        t += abs(l[i-1])
        l[i] += l[i-1] 
    
    print t 