
my_book = (2002, '파이썬', 200)

print(type(my_book))
print(my_book)

year, title, size = my_book
print(year)
print(title)
print(size)

print('-'*30)
print(my_book[0])
print(my_book[1])
print(my_book[2])
# print(my_book[3]) error!!!

print('-'*30)
print(my_book[-1])
print(my_book[-2])
print(my_book[-3])
# print(my_book[-4]) error!!

print(len(my_book))
print(my_book[len(my_book)-1])
