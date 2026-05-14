

def book_list_view(library):
    if not library:
        print("В библиотеке пока нет книг.")
    else:
        for book_title in library:
            print(book_title)


def get_year():
    while True:
        try:
            year = int(input("Введите год издания книги: "))

            if year > 0:
                return year
            else:
                print("Ошибка: год издания должен быть положительным числом.")
        except ValueError:
            print("Ошибка: год издания должен быть числом.")


def get_book_info():
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    year = get_year()

    return title, author, year


def get_update_answer():
    while True:
        answer = input("\nКнига уже есть. Обновить информацию? да/нет: ").strip().lower()

        if answer == "да" or answer == "нет":
            return answer

        print("Ошибка: введите 'да' или 'нет'.")


def add_book(library, title, author, year):
    found_title = find_book_title(library, title)

    if found_title:
        answer = get_update_answer()

        if answer == "нет":
            print(f"Информация о книге '{found_title}' не была изменена.")
            return

        is_available = library[title]["is_available"]
        title = found_title
        message = f"Информация о книге '{title}' успешно обновлена."
    else:
        is_available = None
        message = f"Книга '{title}' успешно добавлена."

    library[title] = {
        "author": author,
        "year": year,
        "is_available": is_available
    }

    print(message)


def get_book_title(text):
    return input(text).strip()


def remove_book(library, title):
    found_title = find_book_title(library, title)

    if found_title:
        del library[found_title]
        print(f"Книга {found_title} была успешно удалена.")
    else:
        print(f"Книга {title} не найдена.")


def issue_book(library, title):
    found_title = find_book_title(library, title)

    if not found_title:
        print(f"Книга '{title}' не найдена.")
        return

    if library[found_title]["is_available"] is False:
        print(f"Книга '{found_title}' уже выдана.")
        return

    library[found_title]["is_available"] = False
    print(f"Книга '{found_title}' выдана.")


def return_book(library, title):
    found_title = find_book_title(library, title)

    if not found_title:
        print(f"Книга '{title}' не найдена.")
        return

    if library[found_title]["is_available"] is True:
        print(f"Книга '{found_title}' уже находится в библиотеке.")
        return

    library[found_title]["is_available"] = True
    print(f"Книга '{found_title}' возвращена в библиотеку.")


def find_book_title(library, user_title):
    user_title = user_title.strip().lower()

    for library_title in library:
        if library_title.lower() == user_title:
            return library_title

    return None


def get_availability_text(is_available):
    if is_available is None:
        return "Книга в библиотеке, но ее статус не определен"
    elif is_available is False:
        return "Книга выдана"
    elif is_available is True:
        return "Книга доступна"
    else:
        return "Некорректный статус книги"


def find_book(library, title):
    found_title = find_book_title(library, title)

    if found_title:
        availability_text = get_availability_text(library[found_title]["is_available"])

        print(
            f"Название: {found_title}\n"
            f"Автор: {library[found_title]['author']}\n"
            f"Год издания: {library[found_title]['year']}\n"
            f"Наличие: {availability_text}"
        )
    else:
        print(f"Книга '{title}' не найдена.")


def add_book_action(library):
    title, author, year = get_book_info()
    add_book(library, title, author, year)


def remove_book_action(library):
    title = get_book_title("Введите название книги для удаления: ")
    remove_book(library, title)


def issue_book_action(library):
    title = get_book_title("Введите название книги для выдачи: ")
    issue_book(library, title)


def return_book_action(library):
    title = get_book_title("Введите название книги для возврата: ")
    return_book(library, title)


def find_book_action(library):
    title = get_book_title("Введите название книги для поиска: ")
    find_book(library, title)


def main(library):
    menu = {
        "1": {"description": "Показать список книг", "action": book_list_view},
        "2": {"description": "Добавить книгу", "action": add_book_action},
        "3": {"description": "Удалить книгу", "action": remove_book_action},
        "4": {"description": "Выдать книгу", "action": issue_book_action},
        "5": {"description": "Вернуть книгу", "action": return_book_action},
        "6": {"description": "Найти книгу", "action": find_book_action},
        "0": {"description": "Завершить программу", "action": None}
    }

    while True:
        print("\nМеню:")

        for key, value in menu.items():
            print(f"{key}. {value['description']}")

        choice = input("\nВыберите действие: ").strip()

        if choice == "0":
            print("Программа завершена.")
            break

        if choice in menu:
            menu[choice]["action"](library)
        else:
            print("Ошибка: выберите пункт из меню.")


if __name__ == "__main__":
    library = {
        "Гарри Поттер и филосовский камень": {
            "author": "Дж. К. Роулинг",
            "year": 1997,
            "is_available": True
        },
        "Властелин колец": {
            "author": "Дж. Р. Р. Толкин",
            "year": 1954,
            "is_available": False
        },
        "Мастер и Маргарита": {
            "author": "Михаил Булгаков",
            "year": 1967,
            "is_available": True
        },
        "Преступление и наказание": {
            "author": "Фёдор Достоевский",
            "year": 1866,
            "is_available": False
        }
    }

    main(library)