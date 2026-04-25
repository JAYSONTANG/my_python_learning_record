guests = ['hegel' , 'jiuwei' , 'haerin']
message = "welcome to have dinner with me"
time = "next sunday"
print(f"{guests}, {message} {time}.")

cannot_come_guest = guests.pop(1)
print(f"unfortunately, {cannot_come_guest} needs to finish his album, so he cannot come.")

guests.append('zhang letian')
print(f"\n{guests}, {message} {time}.")

new_message = "we get a bigger desk"
print(f"{new_message}, so there will be another three guests.")

guests.insert(1,'xu weiyu')
guests.insert(2,'chen ran')
guests.append('ji xinbo')
print(f"{guests}, {message} {time}.")
print(len(guests))

breaking_news = "the new desk cannot reach here today,so I can just invite two persons."
print(breaking_news)

cannot_be_invited_guest_1 = guests.pop(5)
print(f"sorry, {cannot_be_invited_guest_1.title()}.")
cannot_be_invited_guest_2 = guests.pop(4)
print(f"sorry, {cannot_be_invited_guest_2.title()}.")
cannot_be_invited_guest_3 = guests.pop(2)
print(f"sorry, {cannot_be_invited_guest_3.title()}.")
cannot_be_invited_guest_4 = guests.pop(1)
print(f"sorry, {cannot_be_invited_guest_4.title()}.")

print(f"\n{guests[0]},you can still have dinner with me.")
print(f"{guests[1]}, {message}, cat!")

del guests[0]
del guests[0]
print(guests)