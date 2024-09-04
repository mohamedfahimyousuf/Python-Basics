def firstDigit(num):
    while num>=10:
        num=num/10
    print("First number: ",int(num))

def lastDigit(num):
    print("Last Number: ",num%10)

num =int(input("Enter a number: "))    

firstDigit(num)
lastDigit(num)

