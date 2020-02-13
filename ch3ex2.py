motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('honda')
print(motorcycles)

cycles=[]
cycles.append('honda')
cycles.append('sukuki')
cycles.append('yamaha')
print(cycles)

cycles.insert(0, 'dukati')
print(cycles)

cycles.insert(2, 'newitem')
print(cycles)

del cycles[2]
print(cycles)

mine = cycles.pop(1)
print(f"I own a {mine} motorcycle")
print(cycles)

too_expensive = 'dukati'
cycles.remove(too_expensive)
print(cycles)
print(f"\nA {too_expensive} is too expensive for me")


dinner_invites = ['Marie Curie', 'Rosalind Franklin', 'Sappho']
print(f"\n\n{dinner_invites[0]}, please come to dinner.")
print(f"{dinner_invites[1]}, please come to dinner.")
print(f"{dinner_invites[2]}, please come to dinner.")

print(f"\n{dinner_invites[2]} can't make it.")

dinner_invites[2] = 'Ada Lovelace'

print(f"{dinner_invites[0]}, please come to dinner.")
print(f"{dinner_invites[1]}, please come to dinner.")
print(f"{dinner_invites[2]}, please come to dinner.")

print('\nI found a bigger table!')

dinner_invites.insert(0, "Lise Meitner")
dinner_invites.insert(2, "Jocelyn Bell")
dinner_invites.append("Dorothy Hodgkin")

print(f"{dinner_invites[0]}, please come to dinner.")
print(f"{dinner_invites[1]}, please come to dinner.")
print(f"{dinner_invites[2]}, please come to dinner.")
print(f"{dinner_invites[3]}, please come to dinner.")
print(f"{dinner_invites[4]}, please come to dinner.")
print(f"{dinner_invites[5]}, please come to dinner.")

print(f"\nOh no, my table shrank!  I can only invite 2!")

Lise = dinner_invites.pop(0)
Jocelyn = dinner_invites.pop(1)
Rosalind = dinner_invites.pop(1)
Dorothy = dinner_invites.pop(2)

print(f"\nSorry {Lise}, you're uninvited.")
print(f"Sorry {Jocelyn}, you're uninvited.")
print(f"Sorry {Rosalind}, you're uninvited.")
print(f"Sorry {Dorothy}, you're uninvited.")

print(f"\n{dinner_invites[0]}, you're still invited.")
print(f"{dinner_invites[1]}, you're also still invited")

del dinner_invites[0]
del dinner_invites[0]

print(dinner_invites)

