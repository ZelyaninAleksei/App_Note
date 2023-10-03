from  datetime import datetime
class Note:
    def __init__(self):
        self._title = input("Введите название (тему) заметки ")
        self._user_text = input("Введите текст заметки ")
        self._date_create_note = datetime.now()
    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    def get_user_text(self):
        return self._user_text

    def set_user_text(self, user_text):
        self._user_text = user_text

    def get_date_create_note(self):
        return self._date_create_note

    def set_date_create_note(self, date_create_note):
        self._date_create_note = date_create_note