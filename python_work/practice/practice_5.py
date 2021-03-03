# 5-2
if 'banana' == 'banana':
    print('yes')
if 'banana' == 'apple':
    print('no')
name = 'ToYota'
if name.lower() == 'toyota':
    print('yes')
# 5-3
color = 'green'
if color == 'green':
    print("You get 5 scores.")
color = 'red'
if color == 'green':
    print("You get 5 scores.")
# 5-4
color = 'green'
if color == 'green':
    print("You get 5 scores.")
else:
    print("You get 10 scores.")
color = 'red'
if color == 'green':
    print("You get 5 scores.")
else:
    print("You get 10 scores.")
# 5-5
if color == 'green':
    print("You get 5 scores.")
elif color == 'yellow':
    print("You get 10 scores.")
else:
    print("You get 15 scores.")
# 5-6
age = 32
if age < 2:
    print("He is a baby.")
elif age < 4:
    print("He is a child.")
elif age < 13:
    print("He is a kid.")
elif age < 20:
    print("He is a teenager.")
elif age < 65:
    print("He is an adult.")
else:
    print("He is an old man.")
# 5-8,5-9
# accounts = []
accounts = ['admin', '4c4a4a', 'gamma', 'new_bee', 'god']
if accounts:
    for account in accounts:
        if account == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {account}, thank you for logging in again.")
else:
    print("We need to find some users!")
# 5-10
current_users = ['John', 'jAck', 'Gamma', 'XXX', 'god']
new_users = ['JOHN', 'may', 'horse', 'xXx', 'NONE']
current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"'{new_user}' is used.")
    else:
        print(f"'{new_user}' is unused.")
# 5-11
numbers = list(range(1, 10))
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")








