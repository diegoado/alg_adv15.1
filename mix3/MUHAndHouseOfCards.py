# -*- coding: utf-8 -*-

# University Federal of Campina Grande
# Student: Diego Adolfo Silva de Araújo
# Registry: 113210090
# Discipline: Algoritmos Avançados

# Code forces
# Problem: 571C - C. MUH and House of Cards
# Time limit per test: 1 second
# Memory limit per test: 256 megabytes
# Input: standard input
# Output: standard output

# Number of cards
n = int(raw_input())
# Number of floors for each house
F = 3 - (n % 3) + 1

houses = 0
while F * (F - 1) / 2 * 3 <= n + F:
    F += 3
    houses += 1

print houses
