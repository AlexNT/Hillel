import codecs
def delete_html_tags(html_file, result_file='cleaned.txt'):
    # Відкриваємо HTML-файл для читання
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    сln_text = ""
    fl_intag = False
    for char in html:
        if char == '<':             # Початок тегу
            fl_intag = True
        elif char == '>':           # Кінець тегу
            fl_intag = False
        elif not fl_intag:          # Якщо не всередині тегу, додаємо символ до результату
            сln_text += char
    # Записуємо очищений текст у новий файл
    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(сln_text)

delete_html_tags('draft.html', 'cleaned.txt')