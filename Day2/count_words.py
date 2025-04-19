import re

def count_words(a:str) -> int :
    cleaned_string = re.sub(r"[^a-zA-z0-9\s]", "",a)
    if len(cleaned_string)==0:
        return ' The input string has no words'
    else:
        return len(cleaned_string.split())

def main():
    print(count_words('Iam a Devops engineer'))
    print(count_words(''))
    print(count_words('Iam a Devops engineer!!!!   !  !!'))

if __name__ == '__main__':
    main()