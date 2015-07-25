# -*- coding: utf-8 -*-

# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados

# Codeforces
# Problem: 558A - A. Lala Land and Apple Trees
# Time limit per test: 1 second
# Memory limit per test: 256 megabytes
# Input: standard input
# Output: standard output

def solve(l, r, s):
    l.sort()
    r.sort()
    ll = len(l)
    lr = len(r)
    total = abs(ll - lr) - 1

    if ll > lr:
        for i in xrange(total):
            s -= l[i].apples
    else:
        for i in xrange(total):
            s -= r[lr - i - 1].apples

    return s


class AppleTree:
    def __init__(self, pos, apples):
        self.pos = pos
        self.apples = apples
    def __cmp__(self, other):
        if self.pos < other.pos:
            return -1
        elif self.pos > other.pos:
            return 1
        else:
            return 0
    def __str__(self):
        return 'Position %d, Number of Apples %d' % (self.pos, self.apples)

left = []
right = []
sum_apples = 0

# Number of apple trees in Lala Land
n = int(raw_input())

for i in xrange(n):
    # Representing the position of the i-th tree and number of apples on it
    x, a = map(int, raw_input().split())
    if x < 0:
        left.append(AppleTree(x, a))
    else:
        right.append(AppleTree(x, a))
    sum_apples += a

print solve(left, right, sum_apples)
