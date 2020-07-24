'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    
    count = word.find('th')
    # Recursive case - one substring found; look for additional substrings in
    # what remains of the input string.
    if count != -1:
        return count_th(word[count + 2:]) + 1
    
    else:
        return 0
