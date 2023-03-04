# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
        
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
# Loop through all 3-digit numbers starting with 5
for i in range(500, 600):
    # Check if the number is prime and print it if it is
    if is_prime(i):
       print(i)

    




