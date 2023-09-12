def solution(number):
    if number < 0:
        return 0
    total = 0
    for i in range(number): # O(N)
        if i % 3 == 0 or i % 5 == 0: # O(Nlog(N))  increases at a multiple of a constant
            total += i #O(1)
    return total #O(1)