# -*- coding: utf-8 -*-

# University Federal of Campina Grande
# Student: Diego Adolfo Silva de Araújo
# Registry: 113210090
# Discipline: Algoritmos Avançados

# Code forces
# Problem: 571B - B. MUH and Import Thing
# Time limit per test: 1 second
# Memory limit per test: 256 megabytes
# Input: standard input
# Output: standard output

def swap(arg1, arg2):
    # MUH are Menshykov, Uslada and Horac
    muh = 0
    # Output is the ask for each of them
    output = ''
    while muh < 3:
        for i in xrange(len(tasks)):
            output += str(tasks[i][1]) + ' '

        if not muh:
            tasks[arg1][1], tasks[arg1 + 1][1] = tasks[arg1 + 1][1], tasks[arg1][1]
        else:
            tasks[arg2][1], tasks[arg2 + 1][1] = tasks[arg2 + 1][1], tasks[arg2][1]

        muh += 1
        output = output[:len(output) - 1] + '|'

    return output

# The number of tasks
number = int(raw_input())
# The difficulty of each task
difficulty = map(int, raw_input().split())
# List containing the level and number of task
tasks = [0] * number

for level in xrange(number):
    tasks[level] = [difficulty[level], level + 1]

tasks.sort()
bottom = top = -1
for task in xrange(len(tasks) - 1):
    if tasks[task][0] == tasks[task + 1][0]:
        if bottom < 0:
            bottom = task
        else:
            top = task
            break

if top < 0:
    print 'NO'
else:
    print 'YES'
    tasks = swap(bottom, top).split('|')
    for task in xrange(3):
        print tasks[task]
