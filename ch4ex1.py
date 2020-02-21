magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
for magician in magicians:
    print(f"{magician.title()}, that was great work!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print(f"Thank you everyone, that was a great show.")

pizzas = ['pepperoni','sausage','cheese']
for pizza in pizzas:
    print(f"I like {pizza} pizza.")
print(f"I really love pizza!\n")

animals = ['cats','dogs','pandas']
for animal in animals:
    print(f"{animal.title()} are squishy!")
print(f"All of these animals are squishy!")

for value in range(1,6):
    print(value)
for value in range(8):
    print(value)

squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

for value in range (1, 21):
    print(value)

for number in range(1, 10):
    print(number)

numbers = list(range(1,1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

odds = list(range(1, 21, 2))
for value in odds:
    print(value)

threes = list(range(3, 31, 3))
for value in threes:
    print(value)

cubes = [value**3 for value in range(1, 11)]
for cube in cubes:
    print(cube)
