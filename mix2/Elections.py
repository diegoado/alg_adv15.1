# -*- coding: utf-8 -*-

# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados

# Codeforces
# Problem: 570A - A. Elections
# Time limit per test: 1 second
# Memory limit per test: 256 megabytes
# Input: standard input
# Output: standard output

# number of candidates and cities
candidate, city = map(int, raw_input().split())

candidates = candidate * [0]
for stage in xrange(city):
    votes = map(int, raw_input().split())

    # partial winner in the city i-th
    partial = votes.index(max(votes))
    candidates[partial] += 1

winner = candidates.index(max(candidates))
print winner + 1
