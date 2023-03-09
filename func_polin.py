def polin (str):
     '''
        Print True if argument is palindrome, or False if it isn't palindrome.
        Argument: "радар"
        Invert str and compare.
    '''    
     return str == str[::-1]
print(polin("радар"))