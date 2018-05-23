from collections import OrderedDict

num_words = int(input())
word_dict = OrderedDict([])
counts = []
for i in range(num_words):
    word = input()
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1
print(len(word_dict))
for word in word_dict:
    counts.append(str(word_dict[word]))
print(' '.join(counts))
