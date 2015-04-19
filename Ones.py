# -*- coding: utf-8 -*-
 
# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados
  
# Problema: Ones
# Nivel: 4

while 1:
    try:
        n = int(raw_input())
    except EOFError:
        break
    
    if n % 2 != 0 and n % 5 != 0:
        
        one = 1
        while one % n != 0:
            one = 10*one + 1
        
        print len(str(one))