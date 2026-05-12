

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
    if title in library:
        answer = get_update_answer()

        if answer == "нет":
            print(f"Информация о книге '{title}' не была изменена.")
            return

        is_available = library[title]["is_available"]
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


def get_book_title():
    return input("Введите название книги: ").strip()


def remove_book(library, title):
    if title in library:
        del library[title]
        print(f"Книга {title} была успешно удалена.")
    else:
        print(f"Книга {title} не найдена.")


def main():
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

    title, author, year = get_book_info()
    add_book(library, title, author, year)

    title_to_remove = get_book_title()
    remove_book(library, title_to_remove)

    print("\nСписок книг в библиотеке:")
    book_list_view(library)


main()