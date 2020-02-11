bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

print(bicycles[0])
print(bicycles[0].title())

print(bicycles[1])
print(bicycles[3])
print(bicycles[-2])

message = f"My first bicycle was a {bicycles[0].title()}"
print(message)

friends = ['Jenn', 'Carissa','Lydia']
print(friends[0])
print(friends[1].lower())
print(friends[-1].upper())

first = "Hello, "
last = ", nice to see you!"

print(f"{first} {friends[0]} {last}")
print(f"{first} {friends[1]} {last}")
print(f"{first} {friends[2]} {last}")

cars = ['pontiac','toyota','audi']
message1 = "I would like to own a"
print(f"{message1} {cars[2].title()}")