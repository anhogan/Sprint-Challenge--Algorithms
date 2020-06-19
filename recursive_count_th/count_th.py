'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # If length of the word is less than two, no possible occurrences so return 0
    if len(word) < 2:
        return 0
    
    # Look at the first and second elements - if they match th, return 1 + recursive call two elements in
    if word[0] == 't' and word[1] == 'h':
        return 1 + count_th(word[2:])

    # Otherwise, recurse through the remainder of the string starting one element in
    else:
        return count_th(word[1:])