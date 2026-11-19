n = int(input ("Enter a number:"))
last = n % 10
print("last digit:", last)


m = int(input("Enter a number:"))
while m >= 10:
    n = n // 10
    print("first digit:", n)

s = int(input("Enter a number:"))
if n % 2 == 0:
    print("even number")
else:
    print("odd number")

d = int(input("Enter a number:"))
count = 0
while d > 0:
    d = d // 10
    count += 1
print("number of digits:", count)



j = int(input("enter a number:"))
rev = 0

while j > 0:
    digit = j % 10
    rev = rev * 10 + digit
    j = j // 10

print("Reverse:", rev)



i = int(input("enter a number:"))
temp = n
rev = 0

while i > 0:
    digit = i % 10
    rev = rev * 10 + digit
    n = n // 10

if temp == rev:
    print("palindrome")
else:
    print("not palindrome")



a = int(input("enter first number:"))
b = int(input("enter second number:"))

lcm = max(a, b)
while True:
    if lcm % a == 0 and lcm % b == 0:
        break
    lcm += 1
print("lcm:", lcm)4