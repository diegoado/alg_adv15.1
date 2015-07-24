# coding: utf-8

# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados

# Problema: A Lenda de Flavious Josephus
# Nivel: 3

def josephus(n, k):
    a=i=1
    while(i<=n):
        a=(a+k-1)%i+1
        i+=1
    return a


nc = int(raw_input())
for i in range(nc):
    n, k = map(int, raw_input().split())
    print'Case %d: %d' % (i+1, josephus(n, k))
