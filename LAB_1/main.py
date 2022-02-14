from func import *
first_path = "FirstFile.txt"
second_path = "SecondFile.txt"
write_file(first_path)
number = int(input("Max word count = "))
read_file(first_path)
format_file(first_path, second_path,number)
read_file(second_path)
