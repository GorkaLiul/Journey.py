#conditionals:

age = int(input('Whats your age'))

if age > 13 and age <18:
    print("you're a teen")
elif age == 13:
    print("you're almost a teen")
elif age < 13:
    print("you're a child")
else:
    print("you're an adult")