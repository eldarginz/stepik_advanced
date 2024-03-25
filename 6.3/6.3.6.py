poet_data = ('Пушкин', 1799, 'Санкт-Петербург')

buffer = list(poet_data)
buffer[2] = 'Москва'

poet_data = tuple(buffer)

print(poet_data)
