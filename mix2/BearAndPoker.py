# -*- coding: utf-8 -*-

# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados

# Codeforces
# Problem: 573A - A. Bear and Poker
# Time limit per test: 2 second
# Memory limit per test: 256 megabytes
# Input: standard input
# Output: standard output

# function for extract two and three of one number X
def extract(value):
    while value % 2 == 0:
        value /= 2
    while value % 3 == 0:
        value /= 3

    return value

# number of players
n = int(raw_input())

# list of bids on the table poker
quotes = set(map(int, raw_input().split()))

valid = True
default_quote = extract(quotes.pop())
while valid and quotes:
    valid = default_quote == extract(quotes.pop())

if valid:
    print 'Yes'
else:
    print 'No'
