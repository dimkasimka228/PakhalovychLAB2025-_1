from collections import deque

class Note:
    def __init__(self, text, date):
        self.text = text
        self.date = date

    def __str__(self):
        return f"[{self.date}] {self.text}"

class NotebookQueue:
    def __init__(self):
        self.notes = deque()

    def add_note(self, note):
        self.notes.append(note)

    def get_next_note(self):
        if not self.notes:
            raise IndexError("Черга порожня! Немає нотаток для обробки.")
        return self.notes.popleft()

    def is_empty(self):
        return len(self.notes) == 0

    def size(self):
        return len(self.notes)
