import unittest
import xmlrunner
from app import Note, NotebookQueue   # імпортуємо код із app.py

class TestNotebookQueue(unittest.TestCase):
    def setUp(self):
        # створюємо чергу з двома нотатками
        self.notebook = NotebookQueue()
        self.notebook.add_note(Note("Test note 1", "2025-11-23"))
        self.notebook.add_note(Note("Test note 2", "2025-11-24"))

    def test_add_note(self):
        # перевірка додавання нотатки
        self.assertEqual(self.notebook.size(), 2)

    def test_get_next_note(self):
        # перевірка отримання першої нотатки
        note = self.notebook.get_next_note()
        self.assertEqual(note.text, "Test note 1")
        self.assertEqual(self.notebook.size(), 1)

    def test_is_empty(self):
        # перевірка порожньої черги
        self.notebook.get_next_note()
        self.notebook.get_next_note()
        self.assertTrue(self.notebook.is_empty())

    def test_get_next_note_empty_queue(self):
        # перевірка виключення при порожній черзі
        self.notebook.get_next_note()
        self.notebook.get_next_note()
        with self.assertRaises(IndexError):
            self.notebook.get_next_note()

if __name__ == "__main__":
    # запускаємо тести з генерацією XML‑репортів у папку test-reports/
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
