# -*- coding: utf-8 -*-

# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados

# Codeforces
# Proble m: 555A - A. Case of Matryoshkas
# Time limit per test: 2 second
# Memory limit per test: 256 megabytes
# Input: standard input
# Output: standard output

answer = count = 0
n, k = map(int, raw_input().split())

for i in xrange(k):
    prev = -1

    chains = map(int, raw_input().split())
    for j in xrange(1, len(chains)):
        if chains[j] == 1 or prev + 1 == chains[j]:
            prev = chains[j]

    if prev != -1:
        answer += chains[0] - prev
        count += chains[0] - prev + 1
    else:
        answer += chains[0] - 1
        count += chains[0]

answer += count - 1
print answer