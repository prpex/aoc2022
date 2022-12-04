# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 16:25:45 2022

@author: damjan
"""
import string

file = open('input202203.txt', 'r+')
input = file.read()
file.close()
lista = input.split()

#Part 1

elfs = []
isti =[]

for line in lista:
    comp1_l = []
    comp2_l = []
    rez = int(len(line)/2)
    for i in line[0:rez:1]:
        comp1_l.append(i)
    for i in line[rez::1]:
        comp2_l.append(i)
    comp1 = set(comp1_l)
    comp2 = set(comp2_l)
    bag = comp1.union(comp2)
    elfs.append(bag)
    isti.append((comp1.intersection(comp2)).pop())

numval = dict()
number = 1
for letter in string.ascii_lowercase:
    numval[letter] = number
    number +=1
for letter in string.ascii_uppercase:
    numval[letter] = number
    number +=1

value1 = []
for a in isti:
    value1.append(numval[a])

total1 = sum(value1) 
print(total1)
    

#Part 2

badges =[]

i=0
while i <= len(elfs)-2:
    badge = set.intersection(elfs[i], elfs[i+1], elfs[i+2])
    badges.append(badge.pop())
    i+=3

value2 = []
for a in badges:
    value2.append(numval[a])

total2 = sum(value2) 
print(total2)



