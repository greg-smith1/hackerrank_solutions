#!/bin/python3


n, m = input().split()
data = []
sort_col = []
for i in range(0, int(n)):
    data.append(input().split())
#print(data)
k = int(input())
for l in range(len(data)):
    sort_col.append(int(data[l][k]))
for k in sorted(enumerate(sort_col), key=lambda x:x[1]):
    print(' '.join(data[k[0]]))
