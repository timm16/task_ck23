# TODO Найдите количество книг, которое можно разместить на дискете

volume = 1.44
BYTES_ONE_CHAR = 4
pages = 100
lines = 50
chars = 25
#Найдем, какой объем занимает одна книга в байтах
one_book_bt = BYTES_ONE_CHAR * pages * lines * chars
#Переведем в Мб
one_book_Mb = one_book_bt / 1024 / 1024

total_book = volume // one_book_Mb

print(f"Количество книг, помещающихся на дискету:{total_book: .0f}")


