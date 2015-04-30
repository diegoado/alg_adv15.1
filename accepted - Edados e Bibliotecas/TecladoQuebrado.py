# -*- coding: utf-8 -*-
   
# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados
    
# Problema: Organizador de Vagões
# Nivel: 3

def sort(v):
    count = 0
    if len(v) > 1:
        i = 1
        while i < len(v):
            k = v[i]
            j = i - 1
            while j >= 0 and v[j] > k:
                v[j+1], v[j] = v[j], k
                count += 1
                j -= 1
            
            i += 1    
    return count 
   
n = int(raw_input())
for i in range(n):
    
    l = int(raw_input())
    v = map(int, raw_input().split())
    print 'Optimal train swapping takes %d swaps.' % sort(v)