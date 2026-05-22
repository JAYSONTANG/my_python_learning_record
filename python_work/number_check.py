number_input = input("Can you input a number?" \
"I can tell you if it is a multiple of 10. ")
number_input = int(number_input)

if number_input % 10 == 0:
    print(f"\nThe number {number_input} is a multiple of 10.")
else:
    print(f"\nThe number {number_input} is not a multiple of 10.")