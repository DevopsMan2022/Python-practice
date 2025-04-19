def reverse_strings(a: str) ->str:
    """ 
    This function will take a string as input returns the reverse of that string
    """
    if (len(a)==0):
        return 'please enter a valid input'
    else:
        b = a[::-1]
        return b

def main():
    print(reverse_strings('abc'))
    print(reverse_strings('abc!0'))
    print(reverse_strings(''))

if __name__ == '__main__':
    main()