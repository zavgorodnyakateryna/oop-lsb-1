import re

from handlers.strategy import CalculateStrategy
from logger.logger import Logger


class CountSentence(CalculateStrategy):
    def run(self, text: str) -> str:
        res = self.__count_sentences(text)

        Logger().log("CountSentence... DONE")
        result = f"Кількість речень в тексті: {res:.2f} \n\r"
        return result


    def __count_sentences(self, text: str):
        sentence_endings = re.compile(r'[.!?]')
        sentences = sentence_endings.findall(text)
        return len(sentences)