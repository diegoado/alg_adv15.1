# coding: utf-8

# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados

# Problema: Divisão da Nlogônia
# Nivel: 2

while 1:
    k = int(raw_input())
    if(k==0): break
    
    m, n = map(int, raw_input().split())
    for i in range(k):
        x, y = map(int, raw_input().split())
        if x > m and y > n:
            print'NE'
        elif x < m and y > n:
            print'NO'
        elif x < m and y < n:
            print'SO'
        elif x > m and y < n:
            print'SE'
        else:
            print'divisa'
    
