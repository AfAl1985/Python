def is_movie_exist(movie, movies_list):
    for i_movie in movies_list:
        if i_movie == movie:
            return  True
    return  False

movies = ['Tough nut', 'Back to the future', 'Taxi driver',
          'Leon', 'Bogemian rapsody', 'Sins city', 'Memento',
          'Harry Potter', 'Village', 'Cursed island', 'Beginning', 'Matrix']

my_list = []

while True:
    print('\nYour top list: ', my_list)
    new_movie = input('Enter a movie: ')
    if is_movie_exist(new_movie, movies):
        print('Commands: add, delete, insert')
        command = input('Choose a command: ')
        if command == 'add':
            my_list.append(new_movie)
        if command == 'delete':
            if is_movie_exist(new_movie, my_list):
                my_list.remove(new_movie)
            else:
                print('This movie is out of our ranq')
        if command == 'insert':
            index = int(input('What index to: '))
            my_list.index(index - 1, new_movie)
    else:
        print("This movie doesn't exist")
