
# while True:
#     age = int(input("how old are you?"))
#     if age <4:
#         print("your ticket is free")
#         break
#     elif age > 3 and age < 13:
#         print("your ticket is $15")
#         break
#     else:
#         print("your ticket is $15")
#         break

False

while True:
    age = int(input("how old are you?"))
    if age <4:
        print("your ticket is free")
    elif age > 3 and age < 13:
        print("your ticket is $15")
    else:
        print("your ticket is $15")
    ask = input("add another person Y/N")
    if ask.lower() == "n":
        break




