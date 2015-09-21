# -*- coding: utf-8 -*-

# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados

# Codeforces
# Problem: 570B - B. Simple Game
# Time limit per test: 1 second
# Memory limit per test: 256 megabytes
# Input: standard input
# Output: standard output

# the range of numbers in the game and the number selected by Misha
n, m = map(int, raw_input().split())

# check the border between n and m to find the highest probability
left, right = m-1, n-m

if left >= right:
    print max(1, m-1)
else:
    print min(n, m+1)