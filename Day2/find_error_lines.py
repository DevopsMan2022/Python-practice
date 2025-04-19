def find_error_lines(file_object):
    error_lines = []
    has_logs = False

    for line in file_object:
        stripped_line = line.strip()
        if stripped_line:
            has_logs = True
            if(stripped_line.lower().find('error')!= -1):   
                error_lines.append(line.rstrip('\n'))
    
    if not has_logs:
        return 'There are no logs in the file'
    elif error_lines:
        return('\n'.join(error_lines))
    else:
        return 'There are no errors in the file'
        
def main():
    try:
        with open("config.txt", "r") as  file:
            result = find_error_lines(file)
            print(result)
    except FileNotFoundError:
        print("Error: config.txt not found in the current directory.")

if __name__ == '__main__':
    main()
