# Winter is almost here, and you're gearing up for an exciting ski vacation. As a coding enthusiast, you love a good challenge. Here's a fun one for you: let's calculate the number of pairs of gloves you can create from your collection.

# Problem Description:

# You're given an array that describes the color of each glove in your collection. Your task is to write a function that calculates how many pairs of gloves you can form. Remember, a pair consists of two gloves of the same color.

# Function Signature:


# def count_glove_pairs(glove_colors):
#     # Your code here


# Input:

# - `glove_colors` (List of Strings): An array of glove colors. The length of the array (n) will be between 1 and 1000.

# Output:

# - An integer representing the number of pairs you can create from the given gloves.

# Examples:

# Example 1:

# glove_colors = ["red", "green", "red", "blue", "blue"]
# count_glove_pairs(glove_colors)
# Output: 2
# Explanation:You can form 1 pair of red gloves and 1 pair of blue gloves. 2 pairs of gloves.


# Example 2:

# glove_colors = ["red", "red", "red", "red", "red", "red"]
# count_glove_pairs(glove_colors)
# Output: 3
#Explanation: You can form 3 pairs of red gloves.

def count_glove_pairs(glove_colors):
    colors={}
    result= 0
    for i in glove_colors:
        if i not in colors:
            colors[i] = 1
        elif i in colors:
            colors[i] += 1
    for i in colors.values():
            pair = i//2
            result += pair
    return result
print(count_glove_pairs(['red', 'green', 'red', 'blue', 'blue']))
