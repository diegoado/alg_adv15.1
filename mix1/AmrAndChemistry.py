# -*- coding: utf-8 -*-

# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados

# Codeforces
# Problem: 558C - C. Amr and Chemistry
# Time limit per test: 1 second
# Memory limit per test: 256 megabytes
# Input: standard input
# Output: standard output

MAX_N = 10**5 + 1
INF = float('inf')

def solve(num):
    global vis, count
    x = num * 2
    step = 1

    while x <= MAX_N:
        vis[x] += 1
        count[x] += step
        step += 1
        x <<= 1

    x = num
    step = 0
    while x > 0:
        vis[x] += 1
        count[x] += step

        if x & 1 and x > 1:
            s_s = step + 2
            xx = x / 2 * 2

            while xx <= MAX_N:
                vis[xx] += 1
                count[xx] += s_s
                xx <<= 1
                s_s += 1

        x >>= 1
        step += 1



n = int(raw_input())
a = map(int, raw_input().split())

vis = [0] * MAX_N
count = [0] * MAX_N

for i in xrange(n):
    solve(a[i])

ans = INF
for i in xrange(MAX_N):
    if vis[i] == n:
        ans = min(ans, count[i])

print ans