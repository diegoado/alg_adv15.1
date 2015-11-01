# -*- coding: utf-8 -*-

# University Federal of Campina Grande
# Student: Diego Adolfo Silva de Araújo
# Registry: 113210090
# Discipline: Algoritmos Avançados

# Code forces
# Problem: 569B - B. Making Sequences is Fun
# Time limit per test: 2 second
# Memory limit per test: 256 megabytes
# Input: standard input
# Output: standard output

memory = [0, 10, 90, 900, 9000, 90000, 900000, 9000000, 90000000, 900000000,
          9000000000, 90000000000, 900000000000, 9000000000000, 90000000000000, 900000000000000,
          9000000000000000, 90000000000000000, 900000000000000000, 9000000000000000000]

# Function S(n) to return the n's digits in decimal base n
def S(n):
    size = 0
    while n > 0:
        n /= 10
        size += 1

    return size

# Number W is a max cost to spend to add more a number in the sequence
# Number M is the first number of sequence (m, m+1,...)
# Number K is a constant used to generate the price to add one number in the sequence
w, m, k = map(int, raw_input().split())

pos = S(m)
if w < k*pos:
    print 0
else:
    n = 10**pos - m
    if w > n*k*pos:
        w -= n*k*pos
        W = w
        while W > 0:
            w = W
            pos += 1
            if W > k*pos*memory[pos]:
                W -= k*pos*memory[pos]
            else:
                break
    n = w
    low, mid = 10**(pos-1), 0
    if pos == S(m):
        low = m

    mid = low + n/(k*pos) - 1
    print mid - m + 1

