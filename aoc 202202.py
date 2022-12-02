# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 09:22:07 2022

@author: damjan.jurkovic
"""

import pandas as pd

input = pd.read_csv(r'input202202.txt', sep=' ', header=None)

input.columns = ['Elf', 'Me']

#Prvi dio

input.loc[input['Me'] == 'X', 'shape'] = 1
input.loc[input['Me'] == 'Y', 'shape'] = 2     
input.loc[input['Me'] == 'Z', 'shape'] = 3

input.loc[(input['Elf'] == 'A') & (input['Me'] == 'X'), 'outcome'] = 3
input.loc[(input['Elf'] == 'A') & (input['Me'] == 'Y'), 'outcome'] = 6
input.loc[(input['Elf'] == 'A') & (input['Me'] == 'Z'), 'outcome'] = 0
input.loc[(input['Elf'] == 'B') & (input['Me'] == 'X'), 'outcome'] = 0
input.loc[(input['Elf'] == 'B') & (input['Me'] == 'Y'), 'outcome'] = 3
input.loc[(input['Elf'] == 'B') & (input['Me'] == 'Z'), 'outcome'] = 6
input.loc[(input['Elf'] == 'C') & (input['Me'] == 'X'), 'outcome'] = 6
input.loc[(input['Elf'] == 'C') & (input['Me'] == 'Y'), 'outcome'] = 0
input.loc[(input['Elf'] == 'C') & (input['Me'] == 'Z'), 'outcome'] = 3


input['sum'] = input['shape'] + input['outcome']


list1 = list(input['sum'])
total = sum(list1)
print(total)

#Drugi dio

input.loc[input['Me'] == 'X', 'outcome2'] = 0
input.loc[input['Me'] == 'Y', 'outcome2'] = 3    
input.loc[input['Me'] == 'Z', 'outcome2'] = 6

input.loc[(input['Elf'] == 'A') & (input['Me'] == 'X'), 'me2'] = 'Z'
input.loc[(input['Elf'] == 'A') & (input['Me'] == 'Y'), 'me2'] = 'X'
input.loc[(input['Elf'] == 'A') & (input['Me'] == 'Z'), 'me2'] = 'Y'
input.loc[(input['Elf'] == 'B') & (input['Me'] == 'X'), 'me2'] = 'X'
input.loc[(input['Elf'] == 'B') & (input['Me'] == 'Y'), 'me2'] = 'Y'
input.loc[(input['Elf'] == 'B') & (input['Me'] == 'Z'), 'me2'] = 'Z'
input.loc[(input['Elf'] == 'C') & (input['Me'] == 'X'), 'me2'] = 'Y'
input.loc[(input['Elf'] == 'C') & (input['Me'] == 'Y'), 'me2'] = 'Z'
input.loc[(input['Elf'] == 'C') & (input['Me'] == 'Z'), 'me2'] = 'X'

input.loc[input['me2'] == 'X', 'shape2'] = 1
input.loc[input['me2'] == 'Y', 'shape2'] = 2    
input.loc[input['me2'] == 'Z', 'shape2'] = 3

input['sum2'] = input['shape2'] + input['outcome2']

print(input)
list2 = list(input['sum2'])
total2 = sum(list2)
print(total2)
