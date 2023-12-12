x = int(input("Enter a number: "))
divisor = 1
prime = [x]
while divisor < x:
    if x%divisor == 0:
        divisor += 1
    divisor += 1
print(prime)