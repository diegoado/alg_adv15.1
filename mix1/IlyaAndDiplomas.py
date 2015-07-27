# -*- coding: utf-8 -*-

# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados

# Codeforces
# Problem: 557A - A. Ilya and Diplomas
# Time limit per test: 1 second
# Memory limit per test: 256 megabytes
# Input: standard input
# Output: standard output

rst = [0] * 3
a = [[0,0] for i in range(3)]

n = int(raw_input())

for i in range(3):
    a[i][0], a[i][1] = map(int, raw_input().split())
    rst[i] = a[i][0]
    a[i][1] -= a[i][0]
    n -= a[i][0]

i = 0
while i < 3 and n > 0:
    rst[i] += min(n, a[i][1])
    n -= a[i][1]
    i += 1

print rst[0], rst[1], rst[2]


