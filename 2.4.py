def isprime(nums): 
    if nums < 2: 
        return False 
    for i in range(2, nums): 
        if nums % i == 0: 
            return False 
    return True 
     
def filter_prime(nums): 
    primes = [] 
    for nums in numbers: 
        if isprime(nums): 
            primes.append(nums) 
    return primes 
numbers = [1, 2, 3, 13, 98, 57, 83, 5] 
print(filter_prime(numbers))

