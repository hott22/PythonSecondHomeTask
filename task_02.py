# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"
import random
import time


limit_candies = 5  # лимит конфет
number_of_candies = 25  # количество конфет
number_moves = 0  # количество ходов

appeals_user = ['Твой ход: ', "Сколько конфет возьмешь?: ", "Бери конфеты: ", 'Подумай сколько взять: ',
                'Твой черед: ', 'Твоя очередь: ', 'Ты возьмешь: ']
appeals_bot = ['Я бот и я взял: ', 'Забрал: ',
               'Бот решил взять: ', 'Я подумал и взял: ']
appeals_end_lose = ['Увы :-(', 'Не огорчайся! Но ты проиграл','В следующий раз получится!','Ты проиграл!',
                    'Проигрыш, попробуй еще','На этот раз бот оказался сильнее']
appeals_end_won = ['Ура, ты победил :-)','Сегодня твой день, поздравляю!','Ты выиграл!','Победа!!!',
                    'Удача на твоец стороне!','Хорошо умеешь считать!','Забирай все конфеты!']
appeals_not_correctnumber = [f'Давай все таки число не больше {limit_candies}: ', 'Эй, хочешь поломать программу? Давай число: ',
                    'Жду правильное число: ']
def user_move(count, limit_candies, user):
    if user == 1:
        a = input(f'{appeals_user[random.randint(0, len(appeals_user) - 1)]}')
        while a.isdigit() == False or int(a) > limit_candies or int(a) < 1:
            a = input(f'{appeals_not_correctnumber[random.randint(0, len(appeals_not_correctnumber) - 1)]}')
    elif user == 2:
        a = input(f'{appeals_user[random.randint(0, len(appeals_user) - 1)]}')
        while a.isdigit() == False or int(a) > limit_candies or int(a) < 1:
            a = input(f'{first_user} {appeals_not_correctnumber[random.randint(0, len(appeals_not_correctnumber) - 1)]}')
    elif user == 3:
        a = input(f'{appeals_user[random.randint(0, len(appeals_user) - 1)]}')
        while a.isdigit() == False or int(a) > limit_candies or int(a) < 1:
            a = input(f'{second_user} {first_user} {appeals_not_correctnumber[random.randint(0, len(appeals_not_correctnumber) - 1)]}')
    count -= int(a)
    return count


def bot_move(count, limit, choice):
    correct_count = count % (limit + 1)
 
    if choice == 2:
        if correct_count == 0:
            bot_list = []
            for i in range(3):
                bot_list.append(random.randint(1, (limit)))
        else:
            bot_list = [correct_count]
            for i in range(2):
                bot_list.append(random.randint(1, (limit)))
    if choice == 1:
        if correct_count == 0:
            bot_list = []
            for i in range(5):
                bot_list.append(random.randint(1, (limit)))
        else:
            bot_list = [correct_count]
            for i in range(4):
                bot_list.append(random.randint(1, (limit)))
    if choice == 3:
        if correct_count == 0:
            bot_list = []
            for i in range(2):
                bot_list.append(random.randint(1, (limit)))
        else:
            bot_list = [correct_count]
            for i in range(1):
                bot_list.append(random.randint(1, (limit)))
                    
    bot_choice = bot_list[random.randint(0, len(bot_list) - 1)]
    count -= bot_choice
    print(f'{appeals_bot[random.randint(0, len(appeals_bot) - 1)]}'
        f'{bot_choice}')

    return count


def slow_printing():
    txt = 'Жеребьевка...  '
    for i in txt:
        time.sleep(0.3)
        print(i, end='', flush=True)


print("Поиграем в игру?")
print()
while True:
    print('1 - Правила игры'
          '\n2 - Играть'
          '\n3 - Выйти из игры'
          '\n')

    my_choice = input('Введи номер операции: ')
    while my_choice.isdigit() == False or int(my_choice) > 3 or int(my_choice) < 1:
        my_choice = input('Нужно ввести только число от 1 до 3: ')
    if int(my_choice) == 3:
        break
    elif int(my_choice) == 1:
        print(f'На столе лежит {number_of_candies} конфет(а). Играют два игрока делая ход друг после друга.'
              '\nПервый ход определяется жеребьёвкой.'
              f'За один ход можно забрать не более чем {limit_candies} конфет.'
              '\nВсе конфеты оппонента достаются сделавшему последний ход.'
              '\n')
    elif int(my_choice) == 2:
        print('1 - Играть с ботом'
            "\n2 - Играть с оппонентом"
            '\n')
        
        my_choice2 = input('С кем хочешь играть? ')
        while my_choice2.isdigit() == False or int(my_choice2) > 2 or int(my_choice2) < 1:
            my_choice2 = input('Нужно ввести число от 1 до 2: ')
        if int(my_choice2) == 2:
            first_user = input('Введи имя первого игрока: ')
            second_user = input('Введи имя второго игрока: ')
            draw = random.randint(0, 1)
            slow_printing()
            print()
            if draw == 0:
                print(f'{first_user} ты ходишь первым!')
            else:
                print(f'{second_user} ты ходишь первый!')
            print(f'Изначально {number_of_candies} конфет, можно брать не более {limit_candies}')
            print()
            while number_of_candies > limit_candies:       
                if draw == 0: 
                    number_of_candies = user_move(number_of_candies, limit_candies, 2)
                else:
                    number_of_candies = user_move(number_of_candies, limit_candies, 3)

                if number_of_candies <= limit_candies:
                    break
                number_moves += 1
                print(f'Осталось конфет: {number_of_candies}')
                print()
                if draw == 0: 
                    number_of_candies = user_move(number_of_candies, limit_candies, 3)
                else:
                    number_of_candies = user_move(number_of_candies, limit_candies, 2)

                if number_of_candies <= limit_candies:
                    break
                number_moves += 1
                print(f'Осталось конфет: {number_of_candies}')
                print()
            if number_of_candies <= limit_candies:
                if number_moves % 2 == 0:
                    if draw == 0:
                        print(f'{first_user} проиграл!')
                    else:
                        print(f'{second_user} выиграл!')   
                else:
                    if draw == 0:
                        print(f'{second_user} выиграл!')
                    else:
                        print(f'{first_user} проиграл!')
                break 
        else:
            print('1 - легкий'
                '\n2 - средний'
                '\n3 - тяжелый')
            my_choice3 = input('Какой уровень сложности выбираешь? ')
            while my_choice3.isdigit() == False or int(my_choice3) > 3 or int(my_choice3) < 1:
                my_choice3 = input('Нужно ввести число от 1 до 3: ')
            draw = random.randint(0, 1)
            slow_printing()
            print()
            if draw == 0:
                print("Ты ходишь первым!")
            else: 
                print("Бот ходит первым!")
            print(f'Изначально {number_of_candies} конфет, можно брать не более {limit_candies}')
            while number_of_candies > limit_candies:
                if draw == 0:
                    number_of_candies = user_move(number_of_candies, limit_candies, 1)
                else:
                    number_of_candies = bot_move(number_of_candies, limit_candies, int(my_choice3))
                if number_of_candies <= limit_candies:
                    break
                number_moves += 1
                print(f'Осталось конфет: {number_of_candies}')
                print()
                if draw == 0:
                    number_of_candies = bot_move(number_of_candies, limit_candies, int(my_choice3))
                else:
                    number_of_candies = user_move(number_of_candies, limit_candies, 1)
                if number_of_candies <= limit_candies:
                    break
                number_moves += 1
                print(f'Осталось {number_of_candies} конфет')
                print()

            if number_of_candies <= limit_candies:
                    if number_moves % 2 == 0:
                        if draw == 0:
                            print(f'{appeals_end_lose[random.randint(0, len(appeals_end_lose) - 1)]}')
                        else:
                            print(f'{appeals_end_won[random.randint(0, len(appeals_end_lose) - 1)]}')   
                    else:
                        if draw == 0:
                            print(f'{appeals_end_won[random.randint(0, len(appeals_end_lose) - 1)]}')
                        else:
                            print(f'{appeals_end_lose[random.randint(0, len(appeals_end_lose) - 1)]}')

                    break
                
            
