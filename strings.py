strings = ['This', 'list', 'is', 'now', 'all', 'together']

sentence = ''
sentence = strings[0]
for x in strings[1:]:
    sentence+=' '
    sentence+=x
print(sentence)
print(' '.join(strings))
