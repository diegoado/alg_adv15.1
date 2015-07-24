# -*- coding: utf-8 -*-
    
# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados
     
# Problema: Onde está o Mármore?
# Nivel: 2

case = 1

def search(l, n):
    head = 0
    tail = len(l) -1
    mid = tail / 2
    
    while head < tail:
        if l[mid] < n:
            head = mid + 1
            mid = (head + tail) / 2
        elif l[mid] > n or (mid > 0 and l[mid-1] == n):
            tail = mid - 1
            mid = (head + tail) / 2
        else:
            return mid + 1
    
    if l[mid] == n:
        return mid + 1
    
    return -1

while 1:
    n, q = map(int, raw_input().split())
    if n == 0 and q == 0: break
    
    l = []
    for i in xrange(n):
        m = int(raw_input())
        l.append(m)
    
    l.sort()
    print 'CASE# %d:' % case
    
    for i in xrange(q):
        e = int(raw_input())
        p = search(l, e)
        
        if p == -1:
            print '%d not found' % e
        else:
            print '%d found at %d' % (e, p)
        
    case += 1    