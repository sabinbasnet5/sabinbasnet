
def is_prime_number(n):
    if (n==0 or n==1): #0 and 1 are not prime number so it returns false
        return False
    for i in range (2, n): #running loop from 2 to n number
        if(n%i==0): #if n is divisible by i then n is not a prime number
            return False
    return True

num = 20
if is_prime_number(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")