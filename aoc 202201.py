# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 09:34:34 2022

@author: damjan.jurkovic
"""

file = open(r'C:\Users\damjan.jurkovic\Desktop\input.txt', 'r+')
input = file.read()
i_str = input.replace('\n',' ').replace('  ', ' 0 ').split(' ')
i_int = [int(i) for i in i_str]
file.close()

#Part 1

elf = []
cal= []
for num in i_int:
    if num != 0:
        cal.append(int(num))
    else:
        sum_cal = sum(cal)
        elf.append(sum_cal)
        cal = []

elf_max_cal = max(elf)

print('elf koji ima najviše kalorija ima:')
print(elf_max_cal)

#-------------------


#Part 2

elf.sort(reverse=True)
n = 0
sum_tri_max = 0
while n < 3:
    sum_tri_max += elf[n]
    n += 1
    
print(elf)
print(sum_tri_max)

