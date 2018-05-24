def is_true(side1, side2):
    for i in range(len(side1)-1):
        if side1[i] >= side1[i+1]:
            continue
        else:
            return 'No'
    for i in range(len(side2)-1):
        if side2[i] <= side2[i+1]:
            continue
        else:
            return 'No'
    return 'Yes'

n = int(input())
for i in range(n):
    count= 0
    a = int(input()) 
    #print(a)
    b = list(map(int, input().split()))
    #print(b)
    smallest_id = b.index(min(b))
    #print(smallest_id)
    side1 = b[:smallest_id]
    side2 = b[smallest_id+1:]
    
    print(is_true(side1, side2))

