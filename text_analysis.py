from collections import Counter

class TextStats:
    # Конструктор приймає текст
    def __init__(self, text):
        self.text = text

    # Метод рахує кількість слів
    def count_words(self):
        return len(self.text.split())

    # Метод визначає найпоширенішу літеру
    def most_common_letter(self):
        letters = [c.lower() for c in self.text if c.isalpha()]
        if not letters:
            return None
        return Counter(letters).most_common(1)[0][0]
