def aws_region_check(region_name: str)-> str:
    """
    This function will take 1 input
    region_name : string 
    and will vaalidate whether it falls in EU , US or not
    """
    if (region_name[:2] == 'eu' or region_name[:2] == 'us'):
        return "The region " + region_name + " falls in eu or us region"
    else:
        return "The region " + region_name + " does not falls in eu or us region"
    
def main():
    print(aws_region_check('us-east-1'))
    print(aws_region_check('asia-east-1'))

if __name__ == '__main__':
    main()