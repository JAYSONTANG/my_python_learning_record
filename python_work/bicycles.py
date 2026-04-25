bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].upper())
print(bicycles[3])
print(bicycles[-2])
message = f"My first bicycle was a {bicycles[1].upper()}"
print(message)
friends_names = ['zhang', 'xu', 'chen']
print(friends_names[0].title())
print(friends_names[-1].title())
friends_names[1] = "Xu Weiyu"
print(friends_names[1].title())
message = "Have a good day"
print(f"{message},{friends_names[0]}")
commuting = ['walking' , 'bicycle' , 'taxi' , 'subway' , 'bus']
my_favorite = "my favorite commuting way is"
reason = "healthy"
print(f"{my_favorite.capitalize()} {commuting[0].removesuffix("ing")},because it is {reason}.")
