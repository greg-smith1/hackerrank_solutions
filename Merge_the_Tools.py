def merge_the_tools(string, k):
    # your code goes here
    substring = []
    final_strings = []
    is_k = 0
    for i in string:
        #print(i)
        is_k += 1
        if i not in substring:
            substring.append(i)
        if is_k == k:
            final_strings.append(''.join(substring))
            #print(substring)
            substring = []
            is_k = 0
    for item in final_strings:
        print(item)
