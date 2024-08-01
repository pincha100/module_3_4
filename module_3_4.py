def single_root_words(root_word, *other_words):
    same_words = []
    # Приводим корневое слово к нижнему регистру
    root_word_lower = root_word.lower()
    # Перебираем все слова в other_words
    for i in other_words:
        # Приводим текущее слово к нижнему регистру
        word_lower = i.lower()
        # Проверяем условие: если root_word содержится в word или наоборот
        if root_word_lower in word_lower or word_lower in root_word_lower:
            # Добавляем оригинальное слово в список same_words
            same_words.append(i)

    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)


