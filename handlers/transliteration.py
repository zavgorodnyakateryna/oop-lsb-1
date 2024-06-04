import re

from handlers.strategy import CalculateStrategy


class Transliteration(CalculateStrategy):
    def run(self, text: str) -> str:
        return self.__transliterate(text)

    def __transliterate(self, name: str) -> str:
        letters = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'h', 'ґ': 'g', 'д': 'd', 'е': 'e', 'є': 'ie',
                   'ж': 'zh', 'з': 'z', 'и': 'y', 'і': 'і', 'ї': 'і', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
                   'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'kh': 'h',
                   'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ю': 'іu', 'я': 'ia', 'ь': '', 'А': 'A', 'Б': 'B', 'В': 'V',
                   'Г': 'H', 'Ґ': 'G', 'Д': 'D', 'Е': 'E', 'Є': 'YE', 'Ж': 'ZH', 'З': 'Z', 'И': 'Y',
                   'І': 'І', 'Ї': 'YI', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N',
                   'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'KH',
                   'Ц': 'TS', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH', 'Ю': 'YU', 'Я': 'YA', 'Ь': ''}


        for key in letters:
            name = name.replace(key, letters[key])
        return name