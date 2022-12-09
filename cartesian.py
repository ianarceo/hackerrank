from itertools import product

list_A = [int(a) for a in input().split()]
list_B = [int(b) for b in input().split()]
list_A.sort()
list_B.sort()
print(*(product(list_A, list_B)))
