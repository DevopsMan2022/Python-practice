import os
def file_exists_or_not(file_name: str) -> str:
    if(os.path.exists(file_name)):
        return 'file exists'
    else:
        return 'file does not exists'
    
def main():
    print(os.getcwd())
    print(file_exists_or_not('comfig.yaml'))
    print(file_exists_or_not('/Users/madhu/OneDrive/Desktop/Python-practice/Python-practice/Day1'))


if __name__ == '__main__':
    main()