def prime_num(number):
    if number < 2:
        return 0;
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return 0
    return 1
 
primeNumbers = []
for numb in range(1, 251):
    if prime_num(numb):
        primeNumbers.append(numb)
 
with open('results.txt', 'w') as f:
    for primeNum in primeNumbers:
        f.write(f"Prime number {primeNum}")
