def join_services(a:list)->str:
    """This function will take a list as input 
    and will combine all those words and returns a string
    """

    if len(a) != 0:
        for word in a:
            b = ('/'.join(a))
            return b
    else:
        return 'There are no services present in the given list'
    
def main():
    print(join_services(['ec2','s3','eks','cloudfront']))
    print(join_services([]))
    print(join_services(['cloudfront']))

if __name__ == '__main__':
    main()