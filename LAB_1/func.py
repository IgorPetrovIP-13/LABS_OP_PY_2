def write_file(path):
    fout = open(path, 'w')
    line = input("Enter your strings. To finish entering go to a new line and press <Ctrl + S>.\n")
    while line != chr(19):
        fout.write(line + '\n')
        line = input()
    fout.close()


def read_file(path):
    print(f"Reading file: {path}\n")
    fin=open(path,'rt')
    for string in fin:
        print(string,end='')
    print('\n')
    fin.close()


def format_file(first_path, second_path, number):
    fin = open(first_path, 'r')
    fout = open(second_path, 'w')
    list = []
    perfect = []
    for line in fin:
        string = line.split()
        for word in string:
            list.append(word)
    for i in list:
        if list.count(i) < number:
            perfect.append(i)
    perfect = sorted(perfect, key=len, reverse=True)
    new_line = ' '.join(perfect)
    fout.write(new_line)
    fin.close()
    fout.close()
