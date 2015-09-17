# -*- coding: utf-8 -*-

# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados

# Codeforces
# Problem: 574A - A. Bear and Elections
# Time limit per test: 1 second
# Memory limit per test: 256 megabytes
# Input: standard input
# Output: standard output

# number of candidates
n = int(raw_input())

# number of votes for each candidates
votes = map(int, raw_input().split())
votes[1:] = sorted(votes[1:], reverse=True)

index = 1
candies = 0
while votes[0] <= votes[index]:
    candies += 1
    votes[0] += 1
    votes[index] -= 1

    if index + 1 == n:
        index = 1
    elif votes[1] > votes[index]:
        index = 1
        votes[1:] = sorted(votes[1:], reverse=True)
    elif votes[index] < votes[index + 1]:
        index += 1

print candies
