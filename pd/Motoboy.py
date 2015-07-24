# -*- coding: utf-8 -*-
    
# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados
     
# Problema: Motoboy
# Nivel: 4

def matriz(n, p):
    m = [0] * p
    for i in xrange(n):
        m[i] = [0] * p
    
    return m
    
m = matriz(21, 31)
    
while 1:
    n = int(raw_input())
    if n == 0: break
    
    p = []
    t = []
    num_p = int(raw_input())
    
    for i in xrange(n):
        t_i, p_i = map(int, raw_input().split())
        t.append(t_i)
        p.append(p_i)
    
    for i in xrange(1, num_p + 1):
        for j in xrange(n):
            if j > 0:
                m[j][i] = m[j-1][i]
                if p[j] <= i:
                    m[j][i] = max(m[j][i], m[j-1][i - p[j]] + t[j])
            else:
                m[j][i] = 0
                if p[j] <= i:
                    m[j][i] = max(m[j][i], t[j])
       
    print '%d min.' % m[n-1][num_p]