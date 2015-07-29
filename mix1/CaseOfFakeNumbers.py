# -*- coding: utf-8 -*-

# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados

# Codeforces
# Problem: 556B - B. Case of Fake Numbers
# Time limit per test: 2 second
# Memory limit per test: 256 megabytes
# Input: standard input
# Output: standard output

gears = int(raw_input())
teeth = map(int, raw_input().split())

tooth = teeth[0]
for index, value in enumerate(teeth):
    value += tooth if index % 2 else -tooth

    if value < 0:
        value += gears
    elif value >= gears:
        value -= gears

    teeth[index] = value

answer = 'No'
if teeth == range(gears):
    answer = 'Yes'

print answer