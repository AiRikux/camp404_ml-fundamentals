# Part 2 of Introduction to Python
# https://github.com/AiRikux

print("Hello Camp404")

# list
a = 'Wati'
b = 'Budi'
c = 'Bayu'
group1 = ['Wati', 'Budi', 'Bayu']
group1.remove('Wati')
print(group1)

# tuple
data = (1, 2, 3, 4, 5)
print(data[0])
for d in data:
	print(d)

# dictionary
carDict = {"factory": "toyota",
           'model': 'avanza',
           'year': '2020'}

# set
cartypes = {'avansa', 'xenia', 'nissan'}
cartypes.add("something")
print(cartypes)
cartypes.pop()
print(cartypes)
d = {'avansa'}

print(cartypes.issubset(d))
print(d.issubset(cartypes))

anumb = {1, 2, 3, 4, 5, 6, 7, 1}
anumb.difference_update({1, 2})
print(anumb)

# map


def a_func(li):
	print(li)

map(a_func, anumb)

print(list(map(lambda x: x[0], cartypes)))

# indexing
anumb[0]

# slicing
anumb[0:2]

