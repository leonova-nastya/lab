import xml.etree.ElementTree as ET

def read_books(file_name):
    tree = ET.parse(file_name)
    root = tree.getroot()
    
    books = []
    total_price = 0.0
    
    for book in root.findall('book'):
        title = book.find('title').text
        author = book.find('author').text
        year = int(book.find('year').text)
        genre = book.find('genre').text
        price = float(book.find('price').text)
        
        books.append({
            'title': title,
            'author': author,
            'year': year,
            'genre': genre,
            'price': price
        })
        
        total_price += price
    
    average_price = total_price / len(books) if books else 0
    return books, average_price

def filter_books(books, genre=None, year=None):
    filtered_books = []
    for book in books:
        if (genre is None or book['genre'] == genre) and (year is None or book['year'] == year):
            filtered_books.append(book)
    return filtered_books

# Чтение и обработка книги
books, average_price = read_books('library.xml')
print("Список книг:")
for book in books:
    print(f"{book['title']} by {book['author']}, {book['year']}, {book['genre']}, ${book['price']:.2f}")

print(f"Средняя цена книг: ${average_price:.2f}")

# Фильтрация книг по жанру
filtered_books = filter_books(books, genre='Fiction')
print("\nФильтрованные книги (жанр 'Fiction'):")
for book in filtered_books:
    print(f"{book['title']} by {book['author']}, {book['year']}, {book['genre']}, ${book['price']:.2f}")
