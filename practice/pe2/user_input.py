# run from terminal

sum = 0
while sum <= 25:
    num = int(input("Enter an integer: "))
    sum += num
    if sum > 25:
        print ("Sum is greater than 25. Exiting...")
        break
