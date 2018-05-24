#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

c = Counter(input()).items()
d = []
for a,b in sorted(c, key=lambda x: (-x[1], x[0])):
    d.append((a, b))
for i in range(3):
    print(d[i][0], d[i][1])

if __name__ == '__main__':
    s = input()
