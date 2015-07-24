# coding: utf-8

# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados

# Problema: Troca de Cartas
# Nivel: 3

while 1:
    a, b = map(int, raw_input().split())
    if(a==0 and b==0): break
    
    x = set(map(int, raw_input().split()))
    y = set(map(int, raw_input().split()))
    
    xy = x.intersection(y)
    x-= xy
    y-= xy
    print min(len(x), len(y))
    
    