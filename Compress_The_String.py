# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby
s = str(input())
groups = []
for k, d in groupby(s):
    groups.append('({}, {})'.format(len(list(d)), k))
print(' '.join(groups))
