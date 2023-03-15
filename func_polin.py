def polin (word):
     '''
        Print True if argument is palindrome, or False if it isn't palindrome.
        Argument: "радар"
        Invert str and compare.
    '''    
     return word == word[::-1]
print(polin("радар"))