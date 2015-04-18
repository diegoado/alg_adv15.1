# -*- coding: utf-8 -*-
 
# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados
  
# Problema: Figurinhas
# Nivel: 2
 
def mdc(x, y):
    if x > y:
        ddd = x
        div = y
    else:
        ddd = y
        div = x
     
    while ddd % div != 0:
        rst = ddd % div
        ddd = div
        div = rst
    return div
     
n = int(raw_input())
for i in range(n):
    x, y = map(int, raw_input().split())
    print mdc(x, y)