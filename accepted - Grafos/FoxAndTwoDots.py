# -*- coding: utf-8 -*-
 
# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados

# Codeforces 
# Problem: 510B - B. Fox And Two Dots
# Time limit per test: 2 second
# Memory limit per test: 256 megabytes
# Input: standard input
# Output: standard output

import sys
sys.setrecursionlimit(10000)

def dfs_path(x, y, startX, startY, color):
    global n, m
    global find_cycle
    global graph, visited
    
    if x < 0 or x >= n or y < 0 or y >= m:
        return
    if graph[x][y] != color:
        return
    if find_cycle == 'Yes':
        return
    if visited[x][y]:
        find_cycle = 'Yes'
        return 
    
    paths = [1, -1, 0, 0]
    visited[x][y] = True
    
    for i in range(4):
        nextX = x + paths[i]
        nextY = y + paths[-i-1]
        if nextX == startX and nextY == startY:
            continue
        dfs_path(nextX, nextY, x, y, color)

graph = []
visited = []
find_cycle = 'No'
n, m = map(int, raw_input().split())

for i in xrange(n):
    graph.append(map(list, raw_input()))
    visited.append([False] * m)
    
for i in xrange(n):
    for j in xrange(m):
        if not visited[i][j]:
            dfs_path(i, j, -1, -1, graph[i][j])
            
print find_cycle