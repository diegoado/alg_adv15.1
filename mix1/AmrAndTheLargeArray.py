# -*- coding: utf-8 -*-

# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados

# Codeforces
# Problem: 558B - B. Amr and The Large Array
# Time limit per test: 1 second
# Memory limit per test: 256 megabytes
# Input: standard input
# Output: standard output

MAX_N = 10**6

n = int(raw_input())
a = map(int, raw_input().split())

dis = [0] * MAX_N
count = [0] * MAX_N

l = r = 0
max_count = min_dis = 0
for i in xrange(n):
    if not count[a[i] - 1]:
        dis[a[i] - 1] = i

    count[a[i] - 1] += 1
    if max_count < count[a[i] - 1]:
        max_count = count[a[i] - 1]
        l = dis[a[i] - 1]
        r = i
        min_dis = i - dis[a[i] - 1]

    if max_count == count[a[i] - 1] and i - dis[a[i] - 1] < min_dis:
        min_dis = i - dis[a[i] - 1]
        l = dis[a[i] - 1]
        r = i

print l + 1, r + 1
