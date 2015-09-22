# -*- coding: utf-8 -*-

# Universidade Federal de Campina Grande
# Aluno: Diego Adolfo Silva de Araújo
# Matricula: 113210090
# Disciplina: Algoritmos Avançados

# Codeforces
# Problem: 569A - A. Music
# Time limit per test: 2 second
# Memory limit per test: 256 megabytes
# Input: standard input
# Output: standard output

restarted = 0
# The song's duration is T in seconds.
# The Lesha downloads the first S seconds of the song and plays it.
# Q seconds is the real time the Internet allows you to download q - 1 seconds of the track.
T, S, q = map(int, raw_input().split())

while S < T:
   S *= q
   restarted += 1

print restarted
