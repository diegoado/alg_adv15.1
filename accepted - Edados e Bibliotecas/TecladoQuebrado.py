# -*- coding: utf-8 -*-
    
# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados
     
# Problema: Teclado Quebrado
# Nivel: 3
 
def answer(s):
    l = ''
    r = ''
    posToInsert = 1
        
    for i in s:
        if i == '[':
            posToInsert = 0
            r = l + r
            l = ''
        elif i == ']':
            posToInsert = 1
            r = l + r
            l = ''
        elif posToInsert == 0:
            l += i
        else:
            r += i
         
    return l + r
 
 
while 1:
    try:
        l = raw_input()
        print answer(l)
    except:
        break