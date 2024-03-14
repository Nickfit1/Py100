# TODO Найдите количество книг, которое можно разместить на дискете
volume = 1.44 * 1024 * 1024 # Информационный объем дискеты в байтах
pages_number = 100  # Количество страниц в книге
string_on_page = 50 # Число строк на странице
chars_on_string = 25 # Количество символов в строке
char_size = 4 # Размер одного символа в байтах

number_of_books = float(volume // (pages_number * string_on_page * chars_on_string * char_size))



print("Количество книг, помещающихся на дискету:", number_of_books)
