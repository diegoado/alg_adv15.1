# -*- coding: utf-8 -*-
    
# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados
     
# Problema: Subsequências
# Nivel: 5

def strStr(s1, s2):
    p = 0
    for i in s1:
        if s2[p] == i:
            p += 1
        
        if p == len(s2):
            return True
    
    return False

n = int(raw_input())

for i in xrange(n):
    s1 = raw_input()
    
    q = int(raw_input())
    
    for i in xrange(q):
        s2 = raw_input()
        
        if strStr(s1, s2):
            print 'Yes'
        else:
            print 'No'
        
