# -*- coding: utf-8 -*-
     
# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados
      
# Problema: Infixa para Posfixa
# Nivel: 3

def getPriority(operator):
    if operator == '(':
        return 1
    elif operator == '+' or operator == '-':
        return 2
    elif operator == '*' or operator == '/':
        return 3
    elif operator == '^':
        return 4
    else:
        return 0
    
def isOperating(caracter):
    operands = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return caracter.upper() in operands

def isOperator(caracter):
    operators = '+-*/^'
    return caracter in operators

def inFixaToPosFixa(exp):
    stk = []
    result = ''
    priority = 0
    
    for i in exp:
        if isOperating(i):
            result += i
        elif isOperator(i):
            priority = getPriority(i)
            
            while len(stk) > 0 and getPriority(stk[-1]) >= priority:
                result += stk.pop()
            stk.append(i)
            
        elif i == '(':
            stk.append(i)
        elif i == ')':
            char = stk.pop()
            while char != '(':
                result += char
                char = stk.pop()
            
    while len(stk) > 0:
        result += stk.pop()
    
    return result


n = int(raw_input())

for i in xrange(n):
    exp = raw_input()
    print inFixaToPosFixa(exp)