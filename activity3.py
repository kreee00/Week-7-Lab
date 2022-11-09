minuteSpent = eval(input('How many minutes do you spent on the internet daily?\n'))
hourSpent = minuteSpent/60
counterY = 0

if hourSpent >= 2:
    print('You might be addicted to the Net')
    q1 = input('Do you stay online longer than you intended? (y/n)\n')
    if q1 == 'y':
        counterY += 1
    q2 = input('Do you hear other people in your life complain about how much time you spend online? (y/n))\n')
    if q2 == 'y':
        counterY +=1
    q3 = input('Do you say or think, “Just a few more minutes” when online? (y/n)\n')
    if q3 == 'y':
        counterY += 1
    q4 = input('Do you try and fail to cut down on how much time you spend online? (y/n)\n')
    if q4 == 'y':
        counterY += 1
    q5 = input('Do you hide how long you’ve been online? (y/n)\n')
    if q5 == 'y':
        counterY += 1
    if counterY >= 3:
        print('You are an INTERNET ADDICT')
    else:
        print('Control your Internet usage. You might become an ADDICT')
else:
    print('Keep up the good habit')