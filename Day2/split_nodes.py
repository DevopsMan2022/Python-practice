def node_split(a: str) -> str:
    """
    This function will take a string input and prints a separate line for each node value
    """
    result = a.split(',')
    # print(result)
    for i in result :
        if (i ==''):
            continue
        else:
            print(i)
    

def main():
    node_split('node1,node2,node3')
    node_split('node1,,node2,node3')
    node_split('')

if __name__ == '__main__':
    main()
