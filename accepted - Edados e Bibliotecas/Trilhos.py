# -*- coding: utf-8 -*-
   
# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Ara�jo
# Matricula: 113210090
# Disciplina: Algoritmos Avan�ados
    
# Problema: Trilhos
# Nivel: 3

while 1:
    n = int(raw_input())
    if n == 0: break
    
    while 1:
        a = range(1, n+1)
        b = map(int, raw_input().split())
        if b == [0]: break
        
        stk = []
        while len(a) > 0:
            flag = True
            if a[0] == b[0]:
                flag = False
                a.pop(0)
                b.pop(0)
            
            while len(stk) > 0 and stk[-1] == b[0]:
                    flag = False
                    stk.pop()
                    b.pop(0)
            
            if flag:
                stk.append(a.pop(0))
        
        if len(a) == len(b) == len(stk) == 0:
            print'Yes'
        else:
            print'No'        
    print