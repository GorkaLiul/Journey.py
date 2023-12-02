#logical operators (and,or,not)
#not operator -> if smth = True, then flip to False

temp = int(input("What's the weather outside?"))
if temp >= 0 and temp <=30:
    print('Ideal conditions')
elif temp < 0 or temp > 30:
    print("Extreme conditions")
else:
    print('idk, look outside')



#lets use not:

temp1 = float(input("Weather 2:"))

if not(temp1 >=0 and temp1 <=30):
    print('Not ideal conditions')
elif not(temp < 0 or temp > 30):
    print('Good Conditions')