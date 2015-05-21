# -*- coding: utf-8 -*-
    
# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados
     
# Problema: Parafusos e Porcas?
# Nivel: 2

def answer(n):
    l = []
    for i in xrange(n):
        x, y = map(int, raw_input().split())
        while x <= y:
            l.append(x)
            x += 1
        
    l.sort()
    num = int(raw_input())
    l = filter(lambda x: l[x] == num, xrange(len(l)))
        
    if len(l) == 0:
        print '%d not found' % num
    else:
        print '%d found from %d to %d' % (num, l[0], l[-1])
            
while 1:
    try:
        n = raw_input()
        if n.strip() != '': answer(int(n))
    except EOFError:
        break