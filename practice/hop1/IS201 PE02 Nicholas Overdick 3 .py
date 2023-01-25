first_number = input('what is the first number? ')
first_number = int(first_number)
second_number = input('what number would you like to add? ')
second_number = int(second_number)

count = first_number + second_number
count = int(count)
while count<25:
    print (count)
    new_number = input('what number would you like to add? ')
    new_number = int(new_number)

    count = count + new_number 

    if count>=25:
        break
