def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)
    
    
import functools 
print(functools.reduce(lambda x, y: lcm(x, y), range(1,20+1)))