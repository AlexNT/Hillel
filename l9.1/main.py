def popular_words (text, words):
    dic = {}
    text = ' ' + text.lower()
    for s in words:
        dic[s] = text.count(' ' + s + ' ')      # у вхідному тексті після кожного слова є пробіл, тому до слова яке шукаю добавляю пробіл щоб слово шукалось цілком
    return dic

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
