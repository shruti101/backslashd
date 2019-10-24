# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 22:09:16 2019

@author: shrut
"""

print('enter your annual slary:')
annual_salary = int(input())
print('enter portion saved')
portion_saved = float(input())
print('enter total cost')
total_cost = int(input())
portion_down_payment = 0.25 * total_cost
monthly_savings = portion_saved * (annual_salary/12)
t=0
current_savings = 0
while current_savings < portion_down_payment:
    current_savings = current_savings + current_savings * (0.04/12) 
    #investment
    current_savings = current_savings + monthly_savings 
    #investment with savings entered 
    t=t+1
print(t)