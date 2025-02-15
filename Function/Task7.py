import random

print("Задача 7. Недоделка")
# Что нужно сделать
# Вы пришли на работу в компанию по разработке игр, целевая аудитория — дети и их родители.
# У предыдущего программиста было задание сделать две игры в одном приложении,
# чтобы пользователь мог выбирать одну из них. Однако программист, на место которого вы пришли,
# перед увольнением не успел выполнить эту задачу и оставил только небольшой шаблон проекта.
# Используя этот шаблон, реализуйте игры «Камень, ножницы, бумага» и «Угадай число».
# Правила игры «Камень, ножницы, бумага»: программа запрашивает у пользователя строку и выводит,
# победил он или проиграл. Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.
# Правила игры «Угадай число»: программа запрашивает у пользователя число до тех пор,
# пока он не отгадает загаданное.
def rock_paper_scissors():
  user = int(input("Make your choice: 1 - rock, 2 - scissors, 3 - paper: "))
  bot = random.randint(1, 3)
  print(bot)
  if (user == 1 and bot == 1) or (user == 2 and bot == 2) or (user == 3 and bot == 3):
    print("It's a draw")
  elif (user == 1 and bot == 2) or (user == 2 and bot == 3) or (user == 3 and bot == 1):
    print("You've won")
  else:
    print("You've lost")

def guess_the_number():
  uknown = random.randint(1, 100)
  print("Number you need to guess: ", uknown)
  guess = 0
  while uknown != guess:
    guess = int(input("Enter your number: "))
    if guess < uknown:
      print("Your number is less than guessed one, try again")
    elif guess > uknown:
      print("Your number is more than guessed one, try again")
    elif guess == uknown:
      print("You have guessed")

def mainMenu():
  select = int(input('Select the game: 1 - rock_paper_scissors, 2 - guess the number '))
  if select == 1:
    rock_paper_scissors()
  elif select == 2:
    guess_the_number()
  else:
    print('Error')

mainMenu()
