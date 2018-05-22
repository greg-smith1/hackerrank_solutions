def fun(s):
    # return True if s is a valid email, else return False
    try:
        s = s.split('@', 1)
        s[1] = s[1].split('.', 1)
    except:
        return False
    try:
        if len(s[1][1]) > 3:
            return False
    except:
        return False
    if not s[1][0].isalnum():
        return False
    s[0] = s[0].replace('-', '')
    s[0] = s[0].replace('_', '')
    if not s[0].isalnum():
        return False
    return True
