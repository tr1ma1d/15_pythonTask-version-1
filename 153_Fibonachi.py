
old_count = 1
current_count = 1

count = '''
10
'''[1:-1].split('\n')

for val in count:
    limit = int(val)
    while old_count <= limit:
        print(old_count)
        new_count = old_count + current_count
        old_count = current_count
        current_count = new_count
        

