# coding: utf-8

# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados

# Problema: Crise de Energia
# Nivel: 4

def last(n, m):
    i, r = (1, 0)
    while i<n:
        r = (r+m) % i
        i+=1
    return r

while 1:
    n = int(raw_input())
    if(n==0): break
    m = 1
    while 1:
        if(last(n,m)!=11):
            m+=1
        else:
            break
    print m
