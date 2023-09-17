stones = '''
3
'''[1:-1].split('\n')
steps = 0



def stones_step(stone):
    if stone - 2 >= 0:
        stone -= 2
    elif stone - 1 >= 0:
        stone -= 1
    return stone


for val in stones:
    stone = int(val)
    while stone > 0:
        stone = stones_step(stone)
        steps += 1
    
    print(steps)
    count_step = 0
