from sys import argv

file_name = "/Users/SuryaSteffia/Documents/pod/tech/pod1/dev/py/data_py/ip_text_sample.txt"
txt = open(file_name)

print("Here's your file %r" % file_name)
print(txt.read())


print("I'll also ask you to type it again:")

file_again = input(">")

txt_again = open(file_again)

print(txt_again.read())
