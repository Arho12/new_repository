def str_func(word):
    """Функция изменения регистра"""
    result = word.upper()
    return result


def to_title(word):
    """Функция изменения первых букв слова к верхнему регистру"""
    result = word.split(" ")
    result = [i.title() for i in result]
    return " ".join(result)


print(to_title("jon konor"))
