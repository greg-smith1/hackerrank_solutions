def minion_game(string):
    # your code goes here
    Stuart = 0
    Kevin = 0
    for i in range(len(string)):
        if string[i] in 'AEIOU':
            Kevin += len(string)-i
        else:
            Stuart += len(string)-i
    if Stuart > Kevin:
        print("Stuart", Stuart)
    elif Kevin > Stuart:
        print("Kevin", Kevin)
    else:
        print("Draw")
