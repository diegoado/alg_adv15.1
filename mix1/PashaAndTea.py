# -*- coding: utf-8 -*-

# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados

# Codeforces
# Problem: 557B - B. Pasha and Tea
# Time limit per test: 1 second
# Memory limit per test: 256 megabytes
# Input: standard input
# Output: standard output

n, w = map(int, raw_input().split())

a = map(int, raw_input().split())
a.sort()

num = min(a[0], a[n] / 2.) * 3 * n
num = min(num, w)

if int(num) < num:
    print num
else:
    print int(num)