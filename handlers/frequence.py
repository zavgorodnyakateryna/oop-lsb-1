import re

from handlers.strategy import CalculateStrategy


class Frequency(CalculateStrategy):
    def run(self, text: str):
        stat = self.__calculate_relative_frequency(text)

        result: str = ""
        for word, frequency in stat.items():
            result += f"Відносна частота вживання '{word}' в тексті: {frequency:.2f}% \n\r"

        return result

    def __relative_frequency(self, word_count, total_word_count):
        relative_frequency = (word_count / total_word_count) * 100
        return relative_frequency


    def __calculate_relative_frequency(self, text):
        words = re.findall(r'\b\w+\b', text.lower()) # Convert text to lowercase
        word_count_dict = {}
        for word in words:
            word_count_dict[word] = word_count_dict.get(word, 0) + 1


        total_word_count = len(words)
        relative_frequencies = {}
        for word, count in word_count_dict.items():
            relative_frequencies[word] = self.__relative_frequency(count, total_word_count)


        return relative_frequencies