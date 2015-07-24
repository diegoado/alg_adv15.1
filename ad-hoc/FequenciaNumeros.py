# coding: utf-8

# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados

# Problema: Frequência de Números
# Nivel: 2

l = []
qtde = int(raw_input())

for i in range(qtde):
    num = int(raw_input())
    l.append(num)

c = list(set(l))
c.sort()
for i in c:
    print'%d aparece %d vez(es)' % (i, l.count(i))
