import math

AB = int(input())
BC = int(input())
num = round(math.degrees(math.atan2(AB, BC)))
print('{}°'.format(num))
