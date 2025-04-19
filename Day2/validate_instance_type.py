import re

def validate_instance_type(a:str)->str:
    """
    This function will take a string input and check whether it will belong to a valid aws ec2 family or not
    and returns a string
    """
    if a != '':
        b= re.match(r"[t3|t2|m5|m4|T3|T2|M5|M4]",a)
        if b:
            return "The Given instance belongs to proper aws ec2 family"
        else:
            return "The given instance not belongs to proper aws ec2 family"
    else:
        return "The given instance is not a valid aws instance family"

def main():
    print(validate_instance_type('T3a.large'))
    print(validate_instance_type('m5.large'))
    print(validate_instance_type(''))

if __name__=='__main__':
    main()