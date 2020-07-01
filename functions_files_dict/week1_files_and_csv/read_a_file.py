fileref = open("olympics.txt", 'r')
contents = fileref.read() # read the entire file, method 1, return a string
lines = fileref.readlines() # read the entire file, method 2, return a list, the element is line
for line in lines[:4]:
    print(line, end='')

# for line in fileref:
#     print(line.strip())
print(contents[:100])
fileref.close()

