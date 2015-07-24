# -*- coding: utf-8 -*-
   
# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados
    
# Problema: Pintura Preto e Branco
# Nivel: 2
 
from math import ceil
 
while 1:
    n, m, c = map(int, raw_input().split())
    if n == 0 and m == 0 and c == 0: break
     
    n -= 7
    m -= 7
    if n % 2 != 0 and m % 2 != 0 and c == 0:
        print int(ceil( n * m / 2.0) - 1)
    else:
        print int(ceil( n * m / 2.0))