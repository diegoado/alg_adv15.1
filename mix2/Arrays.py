# -*- coding: utf-8 -*-

# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados

# Codeforces
# Problem: 572A - A. Arrays
# Time limit per test: 2 second
# Memory limit per test: 256 megabytes
# Input: standard input
# Output: standard output

# sizes of arrays A and B
len_of_a, len_of_b = map(int, raw_input().split())
# numbers to choose in array A and B
chooses_in_a, chooses_in_b = map(int, raw_input().split())

# The array A
array_a = map(int, raw_input().split())
# The array B
array_b = map(int, raw_input().split())

if array_a[chooses_in_a-1] < array_b[-chooses_in_b]:
    print 'YES'
else:
    print 'NO'
