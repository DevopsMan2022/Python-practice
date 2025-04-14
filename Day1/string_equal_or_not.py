def string_equal_or_not(str1 : str , str2: str)-> str:
    if(str1 == str2):
        return str1 + ' is equal to ' + str2
    else:
        return str1 + ' is not equal to ' + str2
        
def main():
    print(string_equal_or_not('abc','abc'))
    print(string_equal_or_not('ac','non-ac'))


if __name__ == '__main__':
    main()