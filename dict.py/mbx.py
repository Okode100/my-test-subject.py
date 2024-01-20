in_file = input("Enter the name of the file:")
try:
    op_file = open(in_file)
except Exception as e:
    print("File does not exist:")



for line in op_file:
    if line.startswith('From:'):
        #max_line = line.max()
        print(line)

op_file.close()
