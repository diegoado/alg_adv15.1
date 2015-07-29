# -*- coding: utf-8 -*-

# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados

# Codeforces
# Problem: 556A - A. Case of the Zeros and Ones
# Time limit per test: 1 second
# Memory limit per test: 256 megabytes
# Input: standard input
# Output: standard output

ZERO = '0'
n = int(raw_input())

n_z = n_u = 0
for _str in raw_input():
    if _str == ZERO:
        n_z += 1
    else:
        n_u += 1

print abs(n_z - n_u)
