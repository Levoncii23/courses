
lst = [1, 2, 3, 4, 5, 6]
book = {
    'title': 'The Langoliers',
    'author': 'Stephen King',
    'year_published': 1990
}
string = "Hello, world"

for i in book:
    print(i)

# iterator = iter(book)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

it = iter(book)
while True:
    try:
        i = next(it)
        print(i)
    except StopIteration:
        break