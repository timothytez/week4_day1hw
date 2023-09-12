def number_of_pairs(gloves):
    colors={}
    result= 0
    for i in gloves:
        if i not in colors:# O(N)
            colors[i] = 1
        elif i in colors:#O(N)
            colors[i] += 1
    for i in colors.values():# O(N)
            pair = i//2
            result += pair
    return result #O(1)
    pass