# coding: utf-8

# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados

# Problema: Sub-Prime
# Nivel: 2

class Bank:
    def __init__(self, r):
        self.reserva = r

while 1:
    b, n = map(int, raw_input().split())
    if(b==0 and n==0): break
    
    l = []
    r = map(int, raw_input().split())
    for i in range(b):
        bank = Bank(r[i])
        l.append(bank)
   
    for i in range(n):
        d, c, v = map(int, raw_input().split())
        l[c-1].reserva += v
        l[d-1].reserva -= v
    
    liquidated = True
    for i in l:
        if i.reserva<0:
            liquidated = False
            break
    if liquidated:
        print'S'
    else:
        print'N'
        
        
        