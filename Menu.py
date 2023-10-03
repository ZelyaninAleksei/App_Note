class Menu:
    '''
    Метод print_menu отвечает за вывод главного меню
    '''
    def print_menu(self):
        print("Menu:")
        print("1. Создать новую заметку")
        print("2. Просмотр всех заметок")
        print("3. Удаление заметок")
        print("4. Сохранение заметок в файл")
        print("5. Выход")

    '''    
    Функция selecting_an_item отвечает за вывод приглашения ввода пользователем пункта меню,
    а также за проверку корректности введённых данных
    @ return - возвращает int, обозначающий необходимый пункт меню 
    '''
    def selecting_an_item(self):
        self.print_menu()
        check = False
        while not check:
            try:
                choice = int(input("Введите номер пункта меню: "))
                check = True
            except ValueError:
                print("\033[91mОшибка ввода. Повторите выбор пункта меню\033[0m")
        return choice
