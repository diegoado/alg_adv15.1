# -*- coding: utf-8 -*-
   
# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados
    
# Problema: Eu Posso Adivinhar a Estrutura de Dados!
# Nivel: 4

from heapq import _heapify_max, heappush, heappop
    
def answer(n):
    stk = []
    que = []
    heap = []
    is_stk = is_que = is_heap = True
    for i in xrange(n):
        c, e = map(int, raw_input().split())
        if c == 1:
            stk.append(e)
            que.append(e)
            heappush(heap, e)
        else:
            if is_stk and len(stk) > 0 and e != stk.pop():
                is_stk = False
            if is_que and len(que) > 0 and e != que.pop(0):
                is_que = False
            if is_heap and len(heap) > 0:
                _heapify_max(heap)
                if e != heappop(heap):
                    is_heap = False
    
            
    if not is_stk and not is_que and not is_heap:
        return 'impossible'
    if (is_stk and is_que) or (is_stk and is_heap) or (is_que and is_heap):
        return 'not sure'
    if is_stk:
        return 'stack'
    if is_que:
        return 'queue'
    if is_heap:
        return 'priority queue'
            
        
while 1:
    try:
        n = int(raw_input())
        print answer(n)
    except EOFError:
        break