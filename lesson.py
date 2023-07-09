# name = str(input('Enter your name...'))
# vowels = 'aeoiu'

# for i in name:
#     if i in vowels:
#         print(f"{i} is a vowel")
#     else:
#         print(f"{i} is a consonant")


# std_numb = int(input('How many students are in your class?'))
# total_scores = 0
# number_of_iteration = 0
# while number_of_iteration < std_numb:
#     score = int(input('What is the score of student?'))
#     total_scores += score
#     number_of_iteration += 1
# print(total_scores / number_of_iteration)


# numb_of_driver = int(input('How many drivers?'))
#
# total_distance = 0
# total_fuel_used = 0
# numb_of_iteration = 0
#
# while numb_of_iteration < numb_of_driver:
#     distance = int(input('How many kilometres traveled?'))
#     fuel_used = int(input('How many litres of fuel used?'))
#
#     total_distance += distance
#     total_fuel_used += fuel_used
#
#     numb_of_iteration += 1
#
#
# average_fuel_used = total_fuel_used / numb_of_iteration
# average_distance_travelled = total_distance / numb_of_iteration
#
# print(round(average_distance_travelled/average_fuel_used, 2))

# numb1 = int(input('What is your first number?'))
# numb2 = int(input('What is your second number?'))
# numb3 = int(input('What is your third number?'))
#
# smallestNumb = numb1
#
# if numb2 <= smallestNumb:
#     smallestNumb = numb2
# if numb3 <= smallestNumb:
#     smallestNumb = numb3
# print('The smallest number is', smallestNumb)


# userName = str(input('Input your username\n')).lower()
# userPwd = str(input('Enter your password\n')).lower()
#
# if userName == "house" and userPwd == "user":
#     print('True')
#     print('Login in successful')
# else:
#     print('false')
#     print('invalid login credentials')


# numb1 = int(input('Enter a number\n'))
#
# numb2 = int(input('Enter another number\n'))
#
# if numb1 >= 20 and numb2 < 80:
#     print('You have a colour red')
# else:
#     print('You have not chose a colour')


# for i in range(1, 101):
#     if i % 5 == 0 and i % 3 == 0:
#         print(i, 'fuzzbuzz')
#     elif i % 3 == 0:
#         print(i, 'buzz')
#     elif i % 5 == 0:
#         print(i, 'fuzz')

# for points_reader in range(1, 100):
#     if points_reader == 10:
#         print('first bonus')
#         continue
#     elif points_reader == 20:
#         print('second bonus')
#         continue
#     elif points_reader == 40:
#         print('third bonus')
#         continue
#     elif points_reader == 60:
#         print('fourth bonus')
#         continue
#     elif points_reader == 80:
#         print('fifth bonus')
#         continue
#     elif points_reader == 90:
#         print('congrats! All bonuses won!!')
#         break
#     print(points_reader, end = ' ')

# user_input = int(input('Type your number\n'))
#
# def square(user_input):
#     return user_input ** 2
#
# print("The square of your input is\n", square(user_input))


# numb1 = int(input('Enter your first lucky number\n'))
# numb2 = int(input('Enter your second lucky number\n'))
# numb3 = int(input('Enter your last lucky number\n'))
#
# def maximum(numb1, numb2, numb3):
#     lucky_number = numb1
#     if numb2 > lucky_number:
#         lucky_number = numb2
#     if numb3 > lucky_number:
#         lucky_number = numb3
#     return lucky_number

# print("Congrats!!! Your lucky number is ", maximum(numb1, numb2, numb3))


# user_color1 = str(input('Enter your first colour\n')).lower()
# user_color2 = str(input('Enter your second colour\n')).lower()
# user_color3 = str(input('Enter your third colour\n')).lower()
#
# def maximum(user_color1, user_color2, user_color3):
#     fav_colour = user_color1
#     if user_color2 > fav_colour:
#         fav_colour = user_color2
#     if user_color3 > fav_colour:
#         fav_colour = user_color3
#     return fav_colour
#
# print('Your favourite colour is', maximum(user_color1, user_color2, user_color3))


# '''CLONING 23A DICE GAME'''
# import random
#
#
# def roll_dice():
#     die1 = random.randrange(1, 7)
#     die2 = random.randrange(1, 7)
#     return die1, die2
#
#
# def display_dice(dice):
#     die1, die2 = dice
#     print(f'Player 1 rolled {die1} + {die2} = {sum(dice)}')
#
#
# dice_values = roll_dice()
# display_dice(dice_values)  # First roll
#
# sum_of_dice = sum(dice_values)
#
# if sum_of_dice in (7, 11):
#     game_status = 'WON'
# elif sum_of_dice in (2, 3, 12):
#     game_status = 'LOST'
# else:
#     game_status = 'CONTINUE'
#
# player_point = sum_of_dice
# print('Your point is ', player_point)
#
# while game_status == 'CONTINUE':
#     dice_values = roll_dice()
#     display_dice(dice_values)
#     sum_of_dice = sum(dice_values)
#
#     if sum_of_dice == player_point:
#         game_status = 'WON'
#     elif sum_of_dice == 7:
#         game_status = 'LOST'
#
# if game_status == 'WON':
#     print('Player 1 wins!! 😍😍')
# else:
#     print('Player 1 loses!! 🥴🥴')


# passenger_name = input('What is your name\n').lower()
#
#
# def destination():
#     distance_traveled = float(input('Enter the distance you want to travel in meters\n'))
#     distance_time = float(input('Enter the probable time you could spend in minutes\n'))
#     fuel_price = float(input('Enter the amount you bought your last fuel\n'))
#     payment = (distance_traveled + distance_time) % fuel_price
#     return payment
#
#
# print(f'Dear, {passenger_name}. Your transport payment is #{destination()}.\n '
#       f'Thanks for your patronage.')
#
# destination()


# number_of_trip = int(input('How many trip did you go?\n'))
# earned_salary = int(input('How much did you earn per month?\n'))
# trip_counters = 0
#
# while trip_counters < number_of_trip:
#     trip_amount = int(input('How much did you pay the rider?\n'))
#     total_trip_amount = (trip_amount * number_of_trip) % earned_salary
#     trip_counters += 1
#
# print(f'You spent #{total_trip_amount} on transport in this month')


# from random import randint
#
# player_live = 5
# def kid_guess_game():
#     kid_num = randint(1, 50)
#     while player_live > 0:
#         kid_guess = int(input('Hey, genius! Enter your guessed number\n'))
#         if kid_guess == kid_num:
#             print('Hurray, champ!! You guessed it right.😍😍😍')
#             return
#         elif kid_guess > kid_num:
#             print('Ouch! Your guessed number is greater than the number. 🤷‍♂️🤷‍♂️')
#         else:
#             print('Ouch! Your guessed is less than the number. 👌👌')
#
#         player_live -= 1
#         print('You have ', player_live, '❤️ left')
#
#     print('Game over 👺. The hidden number is', kid_num)

# kid_guess_game()


# for x in range(5):
#     for y in range(5):
#         if y > 1:
#             break
#     print(f"({x}, {y})")

# counter = 0
# for odd in range(10):
#     while odd < counter:
#         counter += 1
#     if not odd % 2:
#         continue
#     print(odd)

# selling_price = float(input('Enter the price\n'))
# discount_offered = float(input('How much discount offered?\n'))
#
# def get_net_price(price, discount):
#     return price * (1 - discount)
# net_price = get_net_price(selling_price, discount_offered)
#
# print(net_price)


# letters = []
# letters += 'Alhamdulilah'
#
# for alph in range(len(letters)):
#     print(f'{alph}: {letters[alph]}')
#


# alphabets = 'abcdefghijklmnopqrstuvwxyz'
# cipher_key = 'xznlnwedbkilmuoptciasr'
#
# encryption = str(input('Enter your message\n')).lower()
# for encrypt in encryption:
#     if encrypt.isalpha():
#         print(cipher_key[alphabets.index(encrypt)], end = '')
#     else:
#         print(encrypt, end = '')


# def cipher_encryption(text, shift):
#     result = ''
#     for char in text:
#         if char.isalpha():
#             if char.isupper():
#                 result = chr((ord(char) - 65 + shift) % 26 + 65)
#             else:
#                 result += chr((ord(char) - 97 + shift) % 26 + 97)
#         else:
#             result += char
#     return result
#
#
# message = str(input('Enter your message\n'))
# shift_value = 3
# encrypted_text = cipher_encryption(message, shift_value)
# print(f'Encrypted message: {encrypted_text}')
#
# decrypted_text = cipher_encryption(encrypted_text, -shift_value)
# print(f'Decrypted text: {decrypted_text}')
#
# list_items = [1, 4, 10, 3, 2, 5]
# new_list = list_items[:]
# list_items.insert(2, 80)
# print(new_list)

# quiz_questions = ['Who is the president of Nigeria?\n',
#                   'What is the name of the nearest star to the earth?\n']
# quiz_answers = ['Ahmad Tinubu', 'Alpha Centauri']
# time_counter = 0
#
# for i in range(len(quiz_questions)):
#     reply = input(quiz_questions[i])
#     if reply.lower() == quiz_answers[i].lower():
#         print('Correct')
#         time_counter += 1
#     else:
#         print(f'Wrong answer! The correct answer is {quiz_answers[i]}')
#     print(f'You scored {time_counter} out of {i + 1} questions.')

# added_num = [4, 5, 6]
# given_list = [8, 9, 10]
# given_list[1] = 17
# new_list = given_list + added_num
# new_list.remove(8)
# new_list.sort()
# doubled_list = new_list + new_list
# doubled_list[3] = 25
# print(doubled_list)

# user_number = eval(input('Enter numbers between 1 to 12: '))
# for i in range(12):
#     if user_number[i] > 10:
#         user_number[i] = 10
#     print(user_number[i])

from random import shuffle

players = ['Abeeb', 'Dolapo', 'Sade', 'Yusuff']
team = []
shuffle(players)
for i in range(0, len(players), 2):
    team.append([players[i], players[i + 1]])
print(team)