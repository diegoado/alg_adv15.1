# -*- coding: utf-8 -*-

# University Federal of Campina Grande
# Student: Diego Adolfo Silva de Araújo
# Registry: 113210090
# Discipline: Algoritmos Avançados

# Code forces
# Problem: 569A - B. Chat Online
# Time limit per test: 1 second
# Memory limit per test: 256 megabytes
# Input: standard input
# Output: standard output

fixed = []
floating = []
p, q, l, r = map(int, raw_input().split())

for i in xrange(p):
    a, b = map(int, raw_input().split())
    fixed.append((a, b))

for i in xrange(q):
    c, d = map(int, raw_input().split())
    floating.append((c, d))

segment = 0
for i in xrange(l, r + 1):
    judge = False
    for j in xrange(len(fixed)):
        if judge:
            continue

        for k in xrange(len(floating)):
            if fixed[j][1] < i + floating[k][0] or i + floating[k][1] < fixed[j][0]:
                continue
            else:
                judge = True
                segment += 1
                break
print segment
