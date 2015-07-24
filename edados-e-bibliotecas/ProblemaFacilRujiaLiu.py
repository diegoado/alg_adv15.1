# -*- coding: utf-8 -*-
     
# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados
      
# Problema: Problema Fácil de Rujia Liu?
# Nivel: 4
  
def getDict(n, l):
    d = {}
    for i in range(n):
        if d.has_key(l[i]):
            d[l[i]].append(i+1)
        else:
            d[l[i]] = [i+1]
     
    return d
 
def answer(d, k, v):
    if not d.has_key(v):
        return 0;
     
    l = d.get(v)
    if k > len(l):
        return 0;
    else:
        return l[k-1];
  
while 1:
    try:
        n, m = map(int, raw_input().split())
        l = map(int, raw_input().split())
         
        d = getDict(n, l)
        for i in range(m):
            k, v = map(int, raw_input().split())
            print answer(d, k, v)
    except EOFError:
        break