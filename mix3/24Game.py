# -*- coding: utf-8 -*-

# University Federal of Campina Grande
# Student: Diego Adolfo Silva de Araújo
# Registry: 113210090
# Discipline: Algoritmos Avançados

# Code forces
# Problem: 568A - A. 24 Game
# Time limit per test: 1 second
# Memory limit per test: 256 megabytes
# Input: standard input
# Output: standard output

# Range of Numbers in stack of the game
stack = int(raw_input())
# Output of Game
message = ''

if stack < 4:
    message += 'NO'
elif stack % 2 == 0:
    message += 'YES\n'
    while stack != 4:
        message += '%d - %d = 1\n' % (stack, stack-1)
        message += '4 * 1 = 4\n'
        stack -= 2

    message += '1 * 2 = 2\n'
    message += '3 * 4 = 12\n'
    message += '12 * 2 = 24'
else:
    message += 'YES\n'
    while stack != 5:
        message += '%d - %d = 1\n' % (stack, stack-1)
        message += '5 * 1 = 5\n'
        stack -= 2

    message += '5 - 1 = 4\n'
    message += '4 - 2 = 2\n'
    message += '2 * 3 = 6\n'
    message += '6 * 4 = 24'

print message
