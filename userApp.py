continue1 =input('press 1 to continue and 0 to stop')

while continue1 == '1':
    name = str(input('What is your name?'))
    age = int(input('How old are you?'))
    hobby = str(input('What is your hobby?'))

    remark = 'Dear, {}. You were born in the year {}. Your hobby is {}.\n Glad to tell you that it is one of the hobbies of success people.'
    print(remark.format(name, 2023 - age, hobby))

