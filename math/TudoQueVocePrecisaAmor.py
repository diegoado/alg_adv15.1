# -*- coding: utf-8 -*-
 
# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados
  
# Problema: Tudo o que Você Precisa é Amor
# Nivel: 3
 
def factors(x) :
    f = []
    for i in range(2, int(x**0.5) + 1):
        while x % i == 0:
            x = x / i
            f.append(i) 
     
    return set(f)
 
n = int(raw_input())
for i in range(n):
    s1 = int(raw_input(), 2)
    s2 = int(raw_input(), 2)
     
    f1 = factors(s1)
    f2 = factors(s2)
     
    if len(f1.intersection(f2)) != 0:
        print'Pair #%d: All you need is love!' % (i+1)
    else:
        print'Pair #%d: Love is not all you need!' % (i+1)