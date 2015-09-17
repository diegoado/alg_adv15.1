# -*- coding: utf-8 -*-

# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados

# Codeforces
# Problem: 557C - C. Arthur and Table
# Time limit per test: 1 second
# Memory limit per test: 256 megabytes
# Input: standard input
# Output: standard output

class Table:
    def __init__(self, lenght, energy):
        self.lenght = lenght
        self.energy = energy

    def __cmp__(self, other):
        if self.energy < other.energy:
            return -1
        elif self.energy > other.energy:
            return 1
        else:
            return 0

table = []
n = int(raw_input())
l = map(int, raw_input().split())
d = map(int, raw_input().split())

w = [0] * max(l)
for i in xrange(n):
    w[l[i] - 1] += 1
    table.append(Table(l[i], d[i]))

table.sort()
asnwer = float('inf')

for i in xrange(n):
    rst = 0
    menory = []
    tmp = n - 2 * w[table[i].lenght - 1] + 1
    for j in xrange(n):
        if table[i].lenght < table[j].lenght:
            rst += table[j].energy
            tmp -= 1
        else:
            menory.append(j)
    for j in menory:
        if table[i].lenght == table[j].lenght:
            continue
        elif table[i].lenght > table[j].lenght and tmp > 0:
            rst += table[j].energy
            tmp -= 1
        elif tmp == 0:
            break

    asnwer = min(asnwer, rst)

print asnwer
