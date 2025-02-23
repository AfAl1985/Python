monsters = int(input("Enter a number of monsters: "))
mage_index = int(input("Enter a Mage's number: "))
monsters_damage = []

for monster in range(monsters):
    print(monster + 1, end= ' ')
    damage = int(input())
    monsters_damage.append(damage)

for i_monsters in range(monsters):
    if monsters_damage[i_monsters] < 100 and i_monsters != mage_index - 1:
        monsters_damage[i_monsters] += monsters_damage[mage_index - 1]

print(monsters_damage)