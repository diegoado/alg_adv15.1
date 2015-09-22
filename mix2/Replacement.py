# -*- coding: utf-8 -*-

# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados

# Codeforces
# Problem: 570C - C. Replacement
# Time limit per test: 2 second
# Memory limit per test: 256 megabytes
# Input: standard input
# Output: standard output

def replacement(words):
    value, number = 0, 0
    for character in words:
        if character == '.':
           number += 1
        elif number > 0:
           value += number - 1
           number = 0
    
    if number > 0:
        value += number - 1
    return value

empty_str = [' ']
# the lenght of the string and number of queries
n, m = map(int, raw_input().split())
# the string s, consisting of n lowercase English letters and period signs (characters '.')
string = empty_str + map(None, raw_input()) + empty_str
value = replacement(string[1:n+1])
for query in xrange(m):
    # a position and a lowercase English letter or period sing, describing the query
    position, symbol = raw_input().split()
    position = int(position)

    if symbol != '.' and string[position] == '.':
        if string[position - 1] == '.' and string[position + 1] == '.':
            value -= 2
        elif string[position - 1] == '.' or string[position + 1] == '.':
            value -= 1
    elif symbol == '.' and string[position] != '.':
        if string[position - 1] == '.' and string[position + 1] == '.':
            value += 2
        elif string[position - 1] == '.' or string[position + 1] == '.':
            value += 1

    string[position] = symbol 
    # print numbers to the value of replacement(string) after performing the i-th assignment
    print value