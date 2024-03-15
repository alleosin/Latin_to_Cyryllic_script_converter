one_letter = {
    "Q": "Кв",
    "W": "Ў",
    "E": "Э",
    "R": "Р",
    "T": "Т",
    "Y": "Ы",
    "U": "У",
    "I": "І",
    "O": "О",
    "P": "П",
    "A": "А",
    "S": "С",
    "D": "Д",
    "F": "Ф",
    "G": "Ґ",
    "H": "Г",
    "J": "Й",
    "K": "К",
    "L": "Ль",
    "Z": "З",
    "X": "Кс",
    "C": "Ц",
    "V": "В",
    "B": "Б",
    "N": "Н",
    "M": "М",
    "Š": "Ш",
    "Ŭ": "Ў",
    "Ś": "Сь",
    "Ł": "Л",
    "Ĺ": "Ль",
    "Ź": "Зь",
    "Ž": "Ж",
    "Ć": "Ць",
    "Č": "Ч",
    "Ń": "Нь",
    "q": "кв",
    "w": "ў",
    "e": "э",
    "r": "р",
    "t": "т",
    "y": "ы",
    "u": "у",
    "i": "і",
    "o": "о",
    "p": "п",
    "a": "а",
    "s": "с",
    "d": "д",
    "f": "ф",
    "g": "ґ",
    "h": "г",
    "j": "й",
    "k": "к",
    "l": "ль",
    "z": "з",
    "x": "кс",
    "c": "ц",
    "v": "в",
    "b": "б",
    "n": "н",
    "m": "м",
    "š": "ш",
    "ŭ": "ў",
    "ś": "сь",
    "ł": "л",
    "ź": "зь",
    "ž": "ж",
    "ć": "ць",
    "č": "ч",
    "ń": "нь",
}
two_letters = {
    "ch": "х",
    "CH": "Х",
    "Ch": "Х",
    "LA": "Я",
    "La": "я",
    "la": "я",
    "LO": "Ё",
    "Lo": "ё",
    "lo": "ё",
    "LE": "Е",
    "Le": "е",
    "le": "е",
    "LU": "Ю",
    "Lu": "ю",
    "lu": "ю",
    "LI": "I",
    "Li": "i",
    "li": "i",
}
iotated_softing = {
    "ia": "я",
    "IA": "Я",
    "io": "ё",
    "IO": "Ё",
    "iu": "ю",
    "IU": "Ю",
    "ie": "е",
    "IE": "Е",
}
iotated_not_softing = {
    "JA": "Я",
    "Ja": "Я",
    "ja": "я",
    "JO": "Ё",
    "Jo": "Ё",
    "jo": "ё",
    "JU": "Ю",
    "Ju": "Ю",
    "ju": "ю",
    "JE": "Е",
    "Je": "Е",
    "je": "е",
}
softable = {"П", "п", "С", "с", "Ф", "ф", "Ґ", "ґ", "Г", "г", "К", "к", "З", "з", "Ц", "ц", "В", "в", "Б", "б", "Н", "н", "М", "м"}

def convert(text):
    prev = ""
    result = ""
    for letter in text:
        if prev + letter in two_letters.keys():
            result = result[:-1]
            result += two_letters[prev + letter]
        elif prev + letter in iotated_softing.keys():
            if len(result) > 1 and result[-2] in softable:
                result = result[:-1]
                result += iotated_softing[prev + letter]
            else:
                result += one_letter[letter]
        elif prev + letter in iotated_not_softing.keys():
            result = result[:-1]
            if result != "" and result[-1] in softable:
                result += "'"
            result += iotated_not_softing[prev + letter]
        elif letter in one_letter.keys():
            result += one_letter[letter]
        else:
            result += letter
        prev = letter
    return result


message = input(":")
output = convert(message)
print(output)
