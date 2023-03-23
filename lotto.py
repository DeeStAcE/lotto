from random import shuffle, randint


def get_the_number():
    while True:
        try:
            user_num = int(input('Enter the number:'))
            break
        except ValueError:
            print("It's not a number")
    return user_num


def get_the_numbers():
    user_num_list = []
    while len(user_num_list) < 6:
        user_num = get_the_number()
        if user_num in user_num_list or user_num not in range(1, 49):
            print('Number has to be between 1 - 49 and it can not repeat')
        else:
            user_num_list.append(user_num)
    user_num_list.sort()
    print(f'Your numbers: {user_num_list}')
    return user_num_list


def random_numbers():
    rand_num_list_ = [_ for _ in range(1, 50)]
    shuffle(rand_num_list_)
    rand_num_list_ = rand_num_list_[:6]
    print(f'Drawn numbers: {rand_num_list_}')
    return rand_num_list_


def game():
    user_list = get_the_numbers()
    rand_list = random_numbers()
    correct_count = 0
    for user_el in user_list:
        if user_el in rand_list:
            correct_count += 1
    if correct_count >= 3:
        print(f'Congratulations, you won! You guessed {correct_count} numbers')
    else:
        print(f'You guessed only {correct_count} numbers')


if __name__ == '__main__':
    game()
