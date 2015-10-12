# -*- coding: utf-8 -*-

# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados

# Codeforces
# Problem: 571A - A. MUH and Sticks
# Time limit per test: 1 second
# Memory limit per test: 256 megabytes
# Input: standard input
# Output: standard output

sticks = map(int, raw_input().split())
sticks = dict((l, sticks.count(l)) for l in set(sticks))

leg = sticks.values()
if len(sticks) > 3 or (4 not in leg and 5 not in leg and 6 not in leg):
    print 'Alien'
elif len(sticks) == 3 or 1 in leg:
    print 'Bear'
else:
    print 'Elephant'
