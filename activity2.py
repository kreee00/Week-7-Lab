'''Question 1'''
#a
if 12<12:
    print('Less')
else:
    print('Not Less')
#b
Var1,Var2=25.12,15.00
if Var1 <= Var2:
    print('Less or equal')
else:
    print('Greater than')

'''Question 2'''
#a
Y,X=15.0,25.0
if Y != (X - 10.0):
    X = X -10
else:
    X = X /2.0
print(X)
#b
Y=10.0
X = 25.0
if Y != (X - 10.0):
    X= X -10
else:
    X = X /2.0
print(X)
#c
Y=15.0
if (Y < 15.0) and (Y >= 0.0):
    X = 5 * Y
else:
    X = 2 * Y
print(X)
#d
Y=10.0
if (Y < 15.0) and (Y >= 0.0):
    X = 5 * Y
else:
    X = 2 * Y
print(X)
#e
Y=36.0
if (Y < 15.0) and (Y >= 0.0):
    X = 5 * Y
elif Y >20 :
    X = 4 * Y
else:
    X = 2 * Y
print(X)
#f
Y=-5
if (Y < 15.0) and (Y >= 0.0):
    X = 5 * Y
elif Y >20 :
    X = 4 * Y
else:
    X = 2 * Y
print(X)
#g
Y=67
if (Y < 15.0) and (Y >= 0.0):
    X = 5 * Y
elif Y >20 :
    if Y<30:
        X = 4 * Y
    else:
        X = 0 * Y
else:
    X = 2 * Y
print(X)