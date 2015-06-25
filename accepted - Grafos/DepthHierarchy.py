# -*- coding: utf-8 -*-
 
# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados

# URI Online Judge 
# Problem: 1081 - DFSr - Depth Hierarchy
# Time limit per test: 1 second

def solve(vertex):
    index = 0
    global visited
    while index + 1:
        if dfs_pathR(index, vertex, 2):
            print
        
        index = -1
        for i in xrange(vertex):
            if not visited[i]:
                index = i
                break
            
def dfs_pathR(index, vertex, spaces):
    global graph
    global visited
    has_path = False
    
    visited[index] = True
    for i in xrange(vertex):
        if graph[index][i] == 1:
            has_path = True
            if not visited[i]:
                print'%s%d-%d pathR(G,%d)' % (' ' * spaces, index, i, i)
                dfs_pathR(i, vertex, spaces + 2)
            else:
                print'%s%d-%d' % (' ' * spaces, index, i)
    
    return has_path

graph = []
cases = int(raw_input())

for case in xrange(cases):
    vertex, edge = map(int, raw_input().split())
    visited = [False] * vertex
    
    for i in xrange(vertex):
        graph.append([0] * vertex)
    
    for i in xrange(edge):
        start, end = map(int, raw_input().split())
        
        graph[start][end] = 1
        
    print'Caso %d:' % (case + 1)
    solve(vertex)
    
    graph = []
    