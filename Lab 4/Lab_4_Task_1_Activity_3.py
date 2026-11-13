def search_by_author(books, author):
    result = []

    for book in books:
        title, book_author = book

        if book_author == author:
            result.append(book)

    return result


books = [
    ("Python Basics", "Salman"),
    ("Data Structures", "Ali"),
    ("Python Advanced", "Salman"),
    ("Programming", "Sherry")
]

result = search_by_author(books, "Salman")

print("Books by Salman:")
for book in result:
    print(book)