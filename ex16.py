input_file = "/Users/SuryaSteffia/Documents/pod/tech/pod1/dev/py/data_py/ip_text_sample.txt"

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())


current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kid of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line =1

print_a_line(current_line, current_file)

current_line += 1

print_a_line(current_line, current_file)

current_line += 1

print_a_line(current_line, current_file)