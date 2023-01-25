#1)Basic - Print all integers from 0 to 150.
for basic in range(100):
    print(basic)

#2)Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for multiples in range(5, 1005, 5):
    print(multiples)

# 3)Counting, the Dojo Way - Print integers 1 to 100. 
# If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".

for counting in range(101):
    if counting % 10 == 0:
        print("coding dojo")
    elif counting % 5 == 0:
        print("dojo")
    else:
        print(counting)

#4)
#Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
total = 0
for whoa in range(0, 51,):
    if whoa % 2 == 1:
        print(whoa)

total = 0
for number in range(0, 500000):
    if number % 2 == 1:
        print(number)
    total = total + number
print(f"The Sum of Odd Numbers from 1 to 499999 = {total}")

#5) Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for countdown in range(2018,0,-4):
    print(countdown)


#6) Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum,
#print only the integers that are a multiple of mult. For example,
#if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)


lowNum = 4
highNum = 20
mult = 2
for num in range(lowNum, highNum + 1):
    if num % mult == 0:
        print(num)

