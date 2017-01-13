name = raw_input('What is your name: ')

sales = float(input('How much sales did you make? '))
if sales < 10000:
    commission = 0
    bonus = 0
elif 10000 <= sales < 100000:
    commission = sales * 0.02
    bonus = 0
elif 100001 <= sales < 500000:
    commission = sales * 0.15
    bonus = 1000
elif 500001 <= sales < 1000000:
    commission = sales * 0.28
    bonus = 5000
else:
    commission = sales * 0.35
    bonus = 100000

longevity = int(input('How long have you been with the company?(in month): '))
if longevity >60 and sales > 100000:
    newbonus = bonus + 1000
else:
    newbonus = bonus

vacation = int(input('How many vacation day did you take: '))
base_salary = 2000
if vacation >3:
    base_salary = base_salary -200

paycheck = base_salary + commission + newbonus

print 'Name: ',name
print 'commission: $', commission
print 'bonus: $', newbonus
print 'The employee took', vacation, 'days vacation'
print 'total gross paycheck: $', paycheck
