# -*- coding: utf-8 -*-

# University Federal of Campina Grande
# Student: Diego Adolfo Silva de Araújo
# Registry: 113210090
# Discipline: Algoritmos Avançados

# Code forces
# Problem: 569A - A. I Wanna Be the Guy
# Time limit per test: 1 second
# Memory limit per test: 256 megabytes
# Input: standard input
# Output: standard output

# Number of levels to the game called "I Wanna Be the Guy"
n = int(raw_input())
# Indices of levels that Little X can pass
player1 = map(int, raw_input().split())
# Indices of levels that Little Y can pass
player2 = map(int, raw_input().split())

message = 'I become the guy.'
if set(player1[1:] + player2[1:]) != set(range(1, n + 1)):
    message = 'Oh, my keyboard!'

print message
