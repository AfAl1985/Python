import random

squad_1 = [random.randint(40, 80) for  _ in range(10)]
squad_2 = [random.randint(30, 60) for  _ in range(10)]
squad_3 = ['Died' if squad_1[i_damage] + squad_2[i_damage] > 100 else 'Alive' for i_damage in range(10)]

print(squad_1)
print(squad_2)
print(squad_3)

