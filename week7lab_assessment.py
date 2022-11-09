#BMI Calculator

option = 1

while option == 1:
    heightCM = eval(input('Enter your height in CM: '))
    weight = eval(input('Enter your weight in KG: '))
    heightM = heightCM*0.01
    BMI = weight/(heightM**2)
    if BMI < 18.5:
        print('BMI : Underweight')
        option = eval(input('Press [1] to restart calculation and press [0] to exit the program. '))
    elif 18.5 <= BMI <= 24.9:
        print('BMI : Normal weight')
        option = eval(input('Press [1] to restart calculation and press [0] to exit the program. '))
    elif 25 <= BMI <= 29.9:
        print('BMI : Overweight')
        option = eval(input('Press [1] to restart calculation and press [0] to exit the program. '))
    else:
        print('BMI : Obesity')
        option = eval(input('Press [1] to restart calculation and press [0] to exit the program. '))
else:
    print('Thank you for using the BMI calculator.')