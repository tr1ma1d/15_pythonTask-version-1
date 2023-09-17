import math

dataInput = '''
1 9 2000
12 9 2012
'''[1:-1].split('\n')

result = 0

def calculation_formula(_day,_month,_year):
    c = (_year - 1) // 100 + 1
    y = (_year - 1) % c * 100
    w = day + ((13 * _month - 1) // 5) + y + (y // 4 + c // 4 - 2 * c + 777)
    r = w % 7
    return r

for val in dataInput:
    val = val.split()
    day, month, year = map(int, val)
    result = calculation_formula(day,month,year)
    print(result)

    