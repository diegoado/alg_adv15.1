# -*- coding: utf-8 -*-

# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados

# Codeforces
# Problem: 569B - B. Inventory
# Time limit per test: 1 second
# Memory limit per test: 256 megabytes
# Input: standard input
# Output: standard output

MAX_N = 100010
# the number of items in initial inventory
n = int(raw_input())
# the items in inventory
items = map(int, raw_input().split())

orderly = [0] * MAX_N
# temp list to storage items without position in orderly list
stack = []

for i in xrange(n):
    orderly[items[i]] += 1

for i in xrange(n, 0, -1):
    if orderly[i] < 1:
        stack.append(i)

for i in xrange(n):
    if items[i] > n or orderly[items[i]] > 1:
        orderly[items[i]] -= 1
        items[i] = stack.pop()
    if not stack:
        break

inventory = ''
for i in xrange(n):
    if i+1 == n:
        inventory += str(items[i])
    else:
        inventory += str(items[i]) + ' '

print inventory
