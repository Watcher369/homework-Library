

def book_list_view(library):
    if not library:
        print("В библиотеке пока нет книг.")
    else:
        for book_title in library:
            print(book_title)


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

    book_list_view(library)


main()