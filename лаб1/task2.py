n = 1,44
pages = 100
lines = 50
chars = 25
chars_on_pages= lines * chars
byt_on_page=chars_on_pages * 1
pages_on_diskette = ( n * 1024 * 1024 ) // byt_on_page
book_on_diskette = pages_on_diskette // 100
itog = book_on_diskette
print("Количество книг, помещающихся на дискету:" , itog)
