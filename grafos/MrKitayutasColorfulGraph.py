# -*- coding: utf-8 -*-
 
# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados

# Codeforces 
# Problem: 505B - B. Mr. Kitayuta's Colorful Graph
# Time limit per test: 1 second
# Memory limit per test: 256 megabytes
# Input: standard input
# Output: standard output

def answer(start, end):
    count = 0
    global graph
    
    for key in graph:
        if start not in graph[key] or end not in graph[key]:
            continue
        
        if list([path for path in dfs_paths(graph[key], start, end, [])]):
            count += 1
    
    return count

def dfs_paths(graph, start, end, path):
    if not path:
        path.append(start)
    
    if start == end:
        yield path
    
    for vertex in graph[start] - set(path):
        for key in dfs_paths(graph, vertex, end, path + [vertex]):
            yield key

        

graph = {}      
n, m = map(int, raw_input().split())

for value in xrange(m):
    vertex, edge, color = map(int, raw_input().split())
    
    if not graph.has_key(color):
        graph[color] = {}
    
    if not graph[color].has_key(edge):
        graph[color][edge] = set()
    
    if not graph[color].has_key(vertex):
        graph[color][vertex] = set()
       
    graph[color][edge].add(vertex) 
    graph[color][vertex].add(edge)

num_queries = int(raw_input())

for line in xrange(num_queries):
    u, v = map(int, raw_input().split())
    print answer(u, v)