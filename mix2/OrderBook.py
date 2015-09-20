# -*- coding: utf-8 -*-

# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados

# Codeforces
# Problem: 572B - A. Order Book
# Time limit per test: 2 second
# Memory limit per test: 256 megabytes
# Input: standard input
# Output: standard output

# the number of orders and the book depth
orders, depth = map(int, raw_input().split())

buy = {}
sell = {}
for order in xrange(orders):
    book = None
    # the direction (buy or sell), price and volume to the order
    direction, price, volume = raw_input().split()
    price, volume = int(price), int(volume)

    if direction == 'S':
        book = buy
    else:
        book = sell

    book[price] = book.get(price, 0) + volume

if buy:
    book = sorted(buy.keys())
    for i in xrange(min(depth, len(buy)) - 1, -1, -1):
        print 'S %d %d' % (book[i], buy[book[i]])

if sell:
    book = sorted(sell.keys(), reverse=True)
    for i in xrange(min(depth, len(sell))):
        print 'B %d %d' % (book[i], sell[book[i]])
