print('enter your annual slary:')
annual_salary = int(input())
print('enter portion saved')
portion_saved = float(input())
print('enter total cost')
total_cost = int(input())
print('enter your annual raise')
semi_annual_raise = float(input())

portion_down_payment = 0.25 * total_cost
monthly_savings = portion_saved * (annual_salary/12)
t=1
current_savings = 0
while current_savings < portion_down_payment:
    current_savings = current_savings + current_savings * (0.04/12)
    #investment
    current_savings = current_savings + monthly_savings 
    #investment with monthly savings
    t=t+1
    if t%6==0:
        continue
    current_savings = current_savings + semi_annual_raise * annual_salary
print(t)
