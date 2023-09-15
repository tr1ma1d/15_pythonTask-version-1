import math

steps = '''
1
1
5
3
2
4
4
3
'''[1:-1].split('\n')

stones = int(input())

for val in steps:
    val = val.split()
    stone_value = [int(x) for x in val]
    if sum(stone_value) <= 3:
        stones = stones - sum(stone_value)
    
    

    print(stones)