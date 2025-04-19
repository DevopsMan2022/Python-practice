def filter_regions(a:list)->str:
    """This function will take a list of regions as input and print those are starting with us"""
    b = [item for item in a if item.strip()]
    if len(b)!=0:
        for region in b:
            if region.startswith('us'):
                print(region)
            else:
                continue
    else:
        return print('There are no matching regions available')
    

def main():
    filter_regions(['us-east-1','eu-west-2','us-west-1'])
    filter_regions([''])
    filter_regions(['    ','    '])

if __name__=='__main__':
    main()