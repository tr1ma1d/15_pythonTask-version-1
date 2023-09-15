import math

steps = '''
1
1
5
3
2
4
4
'''[1:-1].split('\n')

stones = int(input())
for val in steps:

    val = val.split()
    substract_caves = map(int, val)
    stones = stones - sum(substract_caves)
    print(stones)