# coding: utf-8

# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados

# Problema: Loop Musical
# Nivel: 2

NULL = -99999

while 1:
    n = int(raw_input())
    if n==0: break
    
    l = map(int, raw_input().split())
    c=s=0
    pa=sa=si=sf=NULL
    
    for i in range(n):
        if pa != NULL:
            if pa < l[i]:
                s = 1
            elif pa > l[i]:
                s = -1
            if sa != NULL:
                if sa != 0 and s != sa:
                    c += 1
            sa = s
        pa = l[i]
        if si == NULL and s != 0:
            si = s
        if i == len(l) - 1:
            sf = s
    if si != sf:
        c += 1
    elif si == sf and si != 0:
        c += 2
    
    print c