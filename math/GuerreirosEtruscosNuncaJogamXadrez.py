# -*- coding: utf-8 -*-
 
# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados
  
# Problema: Guerreiros Etruscos Nunca Jogam Xadrez
# Nivel: 3

n = raw_input()
for i in range(int(n)):
    
    x = 1 + int(raw_input())*8
    count = (int(x**0.5) - 1)/2
    print count
