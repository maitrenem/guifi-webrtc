#!/usr/bin/env python

lines = open('thesis.tex').readlines()

i=0
for line in lines:
    if line.startswith('%%%%%'):
        break
    i+=1

open('thesis.tex', 'w').writelines(lines[i:-1])