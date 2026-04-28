admins = ['lebron', 'mike', 'admin' ,'messi', 'cristiano']

if admins:
    for admin in admins:
        if admin == 'admin':
            print("Hello admin,would you like to see a status report?")
        else:
            print(f"Hello {admin},thank you for logging in again.")

admins =[]

if admins:
    for admin in admins:
        if admin == admins:
            print("Hello admin,would you like to see a status report?")
else:
    print(f"Hello {admins},bye.")

current_users = ['Zhang', 'Chen', 'Wang', 'Austin', 'Luka']
new_users = ['austin', 'luka', 'macus', 'kyrie', 'washington']

current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("The username has been used.")
    else:
        print("The username can be used.")