# We are still introduced to Python

# basic python

a = 3 + 3
print(a)

a = int(input("first number: "))
b = int(input("second number: "))
total = a + b
print("Total = ", total)

# branching
kkey = input("Password: ")

if kkey == 'test123':
	print("Login successful")
else:
	print("Login failed")

# repeating
for x in range(5):
	print("number = ", x)

counter = 1
maxy = 3

while counter < maxy:
	print(counter)
	counter = counter + 1

# function


def halo():
	print("this is from a function")

	
halo()
