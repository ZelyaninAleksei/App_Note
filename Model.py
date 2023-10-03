import json

from Menu import Menu
from Note import Note
from  datetime import datetime


class Model:

    def start_programm(self):
        menu = Menu()
        list_all_notes = dict()
        show_notes = False

        while True:
            choice = menu.selecting_an_item()
            if choice == 1:
                note = Note()
                list_all_notes.update({
                    len(list_all_notes) + 1: {
                        "Заголовок": note.get_title(),
                        "Текст заметки": note.get_user_text(),
                        "Дата создания заметки": note.get_date_create_note().strftime("%d.%m.%Y")
                    }
                })
                print("\033[1;32mЗаметка успешно добавлена\033[0m")
                self.save_notes(list_all_notes)
            elif choice == 2:
                list_all_notes = self.open_notes()
                show_notes = True
                if show_notes:
                    for key, value in list_all_notes.items():
                        print(f"Заметка №{key}:")
                        for field, field_value in value.items():
                            print(f"   {field}: {field_value}")
                    show_notes = False
            elif choice == 3:

                del_choice = str(input("Введите номер заметки для удаления "))
                if del_choice in list_all_notes:
                    del list_all_notes[del_choice]
                else:
                    print(f"\033[91mЗаметки с № {del_choice} не найдено. \n Повторите ввод номера заметки для удаления\033[0m")
                print("\033[1;32mЗаметка успешно удалена\033[0m")
                list_all_notes = update_dict(list_all_notes)
                self.save_notes(list_all_notes)
            elif choice == 4:
                    self.save_notes(list_all_notes)
            elif choice == 5:
                    self.search_for_notes_by_date(list_all_notes)
            elif choice == 6:
                print("Выход из программы")
                break
            else:
                print("\033[91m Ошибка выбора пункта меню. \n Повторите выбор пункта меню\033[0m")

            def update_dict(list_all_notes ):
                new_list_notes = dict()
                for key, value in list_all_notes.items():
                    count = len(new_list_notes) + 1
                    key_new = str(count)
                    new_list_notes[key_new] = value
                return new_list_notes

    def save_notes(self, list_all_notes):
        with open('notes.json', 'w+', encoding='utf-8') as json_file:
            json.dump(list_all_notes, json_file, ensure_ascii=False, indent=4)
        print("\033[1;32mДанные успешно сохранены в файл notes.json\033[0m")

    def open_notes(self):
        with open('notes.json', 'r', encoding='utf-8') as json_file:
            data = json_file.read()
        list_all_notes = json.loads(data)
        return list_all_notes

    def search_for_notes_by_date(self, list_all_notes):
        required_date_str = input("Введите дату для поиска (в формате dd.mm.yyyy): ")

        try:
            required_date = datetime.strptime(required_date_str, "%d.%m.%Y").date()
        except ValueError:
            print("\033[91mОшибка в формате даты. Введите дату в формате dd.mm.yyyy.\033[0m")
            return

        found_notes = []

        for key, value in list_all_notes.items():
            note_date = datetime.strptime(value["Дата создания заметки"], "%d.%m.%Y").date()
            if note_date == required_date:
                found_notes.append((key, value))

        if found_notes:
            print(f"Найдены заметки, созданные {required_date_str}:")
            for key, value in found_notes:
                print(f"Заметка №{key}:")
                for field, field_value in value.items():
                    print(f"   {field}: {field_value}")
        else:
            print(f"\033[91mЗаметки, созданные {required_date_str}, не найдены.\033[0m")