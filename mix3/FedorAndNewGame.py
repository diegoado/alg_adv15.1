# -*- coding: utf-8 -*-

# University Federal of Campina Grande
# Student: Diego Adolfo Silva de Araújo
# Registry: 113210090
# Discipline: Algoritmos Avançados

# Code forces
# Problem: 567B - B. Fedor and New Game
# Time limit per test: 1 second
# Memory limit per test: 256 megabytes
# Input: standard input
# Output: standard output

def compare_weapons(weapon):
    equal_bits = 0
    for j in xrange(n):
        if fedor[j] and weapon & 1 << j == 0:
            equal_bits += 1
        elif not fedor[j] and weapon & 1 << j:
            equal_bits += 1

    return equal_bits

# Types of soldier, number of players and a most K types of soldiers respectively
n, m, k = map(int, raw_input().split())

armies = []
for i in xrange(m):
    army = int(raw_input())
    armies.append(army)

fedor = []
army = int(raw_input())
for i in xrange(n):
    if army & 1 << i:
        fedor.append(True)
    else:
        fedor.append(False)

friends = 0
for i in xrange(m):
    if compare_weapons(armies[i]) <= k:
        friends += 1

print friends
