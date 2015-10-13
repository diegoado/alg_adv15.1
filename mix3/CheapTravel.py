# -*- coding: utf-8 -*-

# University Federal of Campina Grande
# Student: Diego Adolfo Silva de Araújo
# Registry: 113210090
# Discipline: Algoritmos Avançados

# Code forces
# Problem: 566A - A. Cheap Travel
# Time limit per test: 1 second
# Memory limit per test: 256 megabytes
# Input: standard input
# Output: standard output

# N is the number of rides Ann has planned
# M is the number of rides covered by the special ticket
# A is the price of a ride ticket
# B is the price of special ticket
n, m, a, b = map(int, raw_input().split())
if a * m < b:
    rules = n * a
else:
    rules = min(n / m * b + n % m * a, n / m * b + b)
    
print rules



