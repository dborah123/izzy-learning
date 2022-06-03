x = [[i for i in range(5)] for _ in range(5)]


print(x[1][3])

'''
[0, 1, 2, 3, 4],
[0, 1, 2, 3, 4],
[0, 1, 2, 3, 4],
[0, 1, 2, 3, 4],
[0, 1, 2, 3, 4]
'''

array = Array2d(5, 5)
array.get(1, 4) # array[1][4]
array.change(1, 4, 8)
array.print()