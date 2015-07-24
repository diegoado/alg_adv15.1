# -*- coding: utf-8 -*-
 
# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados

# Codeforces 
# Problem: 520B - B. Two Buttons
# Time limit per test: 2 second
# Memory limit per test: 256 megabytes
# Input: standard input
# Output: standard output

queue = []
n, m = map(int, raw_input().split())

queue.append([n, 0])
memory = [False] * 100005

while queue:
    vertex = queue.pop(0)
    if memory[vertex[0]] or vertex[0] > 10000 or vertex[0] < 1:
        continue
    else:
        memory[vertex[0]] = True
            
    if vertex[0] - 1 == m:
        print vertex[1] + 1
        break
    else:
        queue.append([vertex[0] - 1, vertex[1] + 1])
        
    if vertex[0] * 2 == m:
        print vertex[1] + 1
        break
    else:
        queue.append([vertex[0] * 2, vertex[1] + 1])