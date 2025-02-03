def reverse_words(sentence):
    lst = []
    for s in sentence.split(' '):
        lst.append(s[::-1])
    return ' '.join(lst)

print(reverse_words('Hello world'))