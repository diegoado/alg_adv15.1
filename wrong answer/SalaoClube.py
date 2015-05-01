# coding: utf-8

# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados

# Problema: O Salão do Clube
# Nivel: 4

def find(l, k, r):
    c,n = (0, 0)
    y=-1
    i=0
    while len(l)-(i)>abs(y):
        if l[i]==k:
            n+=1
            c+=l[i]
        elif l[i]<k:
            j=1
            s=l[i]
            while i+1<len(l) and l[i+1]+s<k:
                s+=l[i+1]
                j+=1
                i+=1
            if i+1<len(l) and l[i+1]+s==k:
                c+=l[i+1]+s
                n+=j+1
                i+=1
            else:
                while l[y]+s<k:
                    s+=l[y]
                    j+=1
                    y-=1
                if s==k:
                    c+=s
                    n+=j 
                elif l[y]+s==k:
                    c+=l[y]+s
                    n+=j+1
                    y-=1
        i+=1
        if c==r:
            return n
    return -1
 
while 1:
    m, n = map(int, raw_input().split())
    if(m==0 and n==0): break
      
    l = float(raw_input())*10**-2
    k = int(raw_input())
    c = map(int, raw_input().split())
     
    c.sort(reverse = True)
    if m!=n and m!=1 and n!=1:
        h,v = find(c, int(m/l), int(m*n/l)), find(c, int(n/l), int(m*n/l))
    elif n==1:
        h,v = find(c, int(m/l), int(m*n/l)), -1
    else:
        h,v = -1, find(c, int(n/l), int(m*n/l))
    if h==-1 and v==-1:
        print"impossivel"
    elif h==-1:
        print v
    elif v==-1:
        print h
    else:
        print min(h,v)