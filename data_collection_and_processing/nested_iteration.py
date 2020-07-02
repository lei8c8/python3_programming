nested1 = [['a', 'b', 'c'], ['d', 'e'], ['f', 'g', 'h']]

for x in nested1:
    print('Level 1: ')
    for y in x:
        print('    Level2: ' + y)