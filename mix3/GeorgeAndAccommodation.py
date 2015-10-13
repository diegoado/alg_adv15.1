# -*- coding: utf-8 -*-

# University Federal of Campina Grande
# Student: Diego Adolfo Silva de Araújo
# Registry: 113210090
# Discipline: Algoritmos Avançados

# Code forces
# Problem: 567A - A. George and Accommodation
# Time limit per test: 1 second
# Memory limit per test: 256 megabytes
# Input: standard input
# Output: standard output

# Total of rooms in dormitory
rooms = int(raw_input())
# Total of rooms where George and Alex can move in
fit = 0
for i in xrange(rooms):
    # The number of people who already live in i-th room
    # and the room's capacity
    people, capacity = map(int, raw_input().split())
    if capacity - people >= 2:
        fit += 1

print fit
