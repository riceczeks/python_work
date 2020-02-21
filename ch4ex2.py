my_foods = ['pizza', 'falafel', 'carrot cake','fudge']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print(f"The first three items in the list are {my_foods[:3]}")
print(f"The items from teh middle of the list are {my_foods[1:4]}")
print(f"The last items in the list are {my_foods[-3:]}")


pizzas = ['pepperoni','sausage','cheese']
friend_pizzas = pizzas[:]
pizzas.append('mushroom')
friend_pizzas.append('chicken')
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
    