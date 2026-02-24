#-----------------------
#Prime Number Program
#-----------------------
num = int(input("Enter number: "))

if num <= 1:
    print("Not Prime")
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime")
    else:
        print("Not Prime")


#-----------------------
#Factorial Program
#-----------------------
num = int(input("Enter number: "))

factorial = 1

if num < 0:
    print("Factorial not possible")
else:
    for i in range(1, num + 1):
        factorial *= i
    print("Factorial =", factorial)


#-----------------------
#Fibonacci Series Program
#-----------------------
n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


#-----------------------
#Palindrome Program
#-----------------------
num = int(input("Enter number: "))
original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")


#-----------------------
#Armstrong Program
#-----------------------
num = int(input("Enter number: "))
original = num
sum = 0
digits = len(str(num))

while num > 0:
    digit = num % 10
    sum += digit ** digits
    num = num // 10

if sum == original:
    print("Armstrong")
else:
    print("Not Armstrong")
