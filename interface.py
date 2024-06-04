import tkinter as tk
from tkinter import filedialog

from handlers.strategy import CalculateStrategy
from logger.logger import Logger
from handlers.frequence import Frequency
from handlers.count_sentence import CountSentence
from handlers.transliteration import Transliteration


class Interface:
    title: str = "Text analysis"
    __app: tk.Tk
    __text_editor: tk.Text
    __output_panel: tk.Text
    __handlers: dict = dict()

    def __init__(self) -> None:
        self.__app = tk.Tk()
        self.__initialize_components()
        self.__logger = Logger()

    def __initialize_components(self):
        self.__text_editor = tk.Text(self.__app, height=10, width=100)
        self.__text_editor.pack(pady=20)

        self.__output_panel = tk.Text(self.__app, height=10, width=100, state=tk.DISABLED)
        self.__output_panel.pack(pady=20)

        menu_bar = tk.Menu(self.__app)
        self.__app.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open", command=self.__open_file)
        file_menu.add_command(label="Save", command=self.__save_file)

        run_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Run", menu=run_menu)

        frequencyStrategy = Frequency()
        countSentenceStrategy = CountSentence()
        transliterationStrategy = Transliteration()

        run_menu.add_command(label="відносна частота вживання", command=lambda: self.__process(frequencyStrategy))
        run_menu.add_command(label="кількість речень", command=lambda: self.__process(countSentenceStrategy))
        run_menu.add_command(label="транслітерація", command=lambda: self.__process(transliterationStrategy))

    def __open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("JSON files", "*.json"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                self.__text_editor.delete(1.0, tk.END)
                self.__text_editor.insert(tk.END, file.read())

    def __save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension="txt",
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.__text_editor.get(1.0, tk.END))

    def __process(self, strategy: CalculateStrategy):
        content = self.__text_editor.get(1.0, tk.END)
        res = strategy.run(content)
        self.__logger.log(f"run strategy: {strategy}")
        self.__print(res)

    def __print(self, content: str):
        self.__output_panel.config(state=tk.NORMAL)
        self.__output_panel.delete(1.0, tk.END)
        self.__output_panel.insert(tk.END, content)
        self.__output_panel.config(state=tk.DISABLED)

    def __run_function(self):
        content = self.__text_editor.get(1.0, tk.END)
        result = content.upper()

        self.__output_panel.config(state=tk.NORMAL)
        self.__output_panel.delete(1.0, tk.END)
        self.__output_panel.insert(tk.END, result)
        self.__output_panel.config(state=tk.DISABLED)

    def run(self):
        self.__app.title(self.title)
        self.__app.mainloop()