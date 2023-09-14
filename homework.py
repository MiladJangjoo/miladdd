# Exercise 1: Simple Memoization
def mem(num):
    if num <= 1:
        return 1
    return mem(num-1) + mem(num-2)


def memoize (num):
    milad = {}
    if num <= 1 :
        return 1
    if num not in milad:
        milad[num] = memoize(num  - 1) + memoize(num  - 2)
    return milad[num]

print(mem(10))
print(memoize(10))

# Exercise 2: Count Function Calls

def count_calls(num):
    times = 0
    if num <= 1:
        times += 1
        return 1 
    times += 2
    return mem(num-1) + mem(num-2) 

print(count_calls(5))
