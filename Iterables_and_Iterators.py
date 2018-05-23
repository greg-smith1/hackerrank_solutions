from itertools import combinations

N = int(input())
array = input().split()
K = int(input())

c = list(combinations(array, K))
f = filter(lambda x: 'a' in x, c)

print(len(list(f))/len(c))
