import re

def relative_frequency(word_count, total_word_count):
   relative_frequency = (word_count / total_word_count) * 100
   return relative_frequency


def calculate_relative_frequency(text):
   words = re.findall(r'\b\w+\b', text.lower()) # Convert text to lowercase
   word_count_dict = {}
   for word in words:
       word_count_dict[word] = word_count_dict.get(word, 0) + 1


   total_word_count = len(words)
   relative_frequencies = {}
   for word, count in word_count_dict.items():
       relative_frequencies[word] = relative_frequency(count, total_word_count)


   return relative_frequencies

def transliterate(name):
   letters = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo',
             'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
             'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h',
             'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e',
             'ю': 'u', 'я': 'ya', 'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'YO',
             'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N',
             'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H',
             'Ц': 'C', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SCH', 'Ъ': '', 'Ы': 'y', 'Ь': '', 'Э': 'E',
             'Ю': 'U', 'Я': 'YA', 'ґ': 'g', 'ї': 'i', 'є': 'ie', 'Ґ': 'g', 'Ї': 'i',
             'Є': 'Ie'}


   for key in letters:
       name = name.replace(key, letters[key])
   return name

def count_sentences(text):
   sentence_endings = re.compile(r'[.!?]')
   sentences = sentence_endings.findall(text)
   return len(sentences)