import string
def is_palindrome(text):
    text = text.lower().replace(' ', '')    # певодимо в нижній регіст у даляємо пробіли
    for ch in string.punctuation:           # удаляємо знаки пунктуації
        text = text.replace(ch, '')
    if text[::-1] == text:                  # зравнюємо з реверсивною строкою
        return True
    return False

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")