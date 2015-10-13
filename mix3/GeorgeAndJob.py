# -*- coding: utf-8 -*-

# University Federal of Campina Grande
# Student: Diego Adolfo Silva de Araújo
# Registry: 113210090
# Discipline: Algoritmos Avançados

# Code forces
# Problem: 567C - C. George and Job
# Time limit per test: 1 second
# Memory limit per test: 256 megabytes
# Input: standard input
# Output: standard output

n, m, k = map(int, raw_input().split())
P = map(int, raw_input().split())

sP = [0] * (n + 1)
menory = [[0] * (k + 1)]

for i in xrange(n):
    sP[i + 1] = P[i] + sP[i]
    menory.append([0] * (k + 1))

for i in xrange(1, k + 1):
    for j in xrange(1, n + 1):
        menory[j][i] = menory[j - 1][i]
        if j >= m:
            menory[j][i] = max(menory[j][i], menory[j - m][i - 1] + sP[j] - sP[j - m])

print menory[n][k]