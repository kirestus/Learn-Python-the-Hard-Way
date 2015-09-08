#imports sys argv to call arguments on start
from sys import argv

#set the files to call when python starts to the name of the script and the second file to be the name of the input file
script, input_file = argv

#defines a function that that prints the whole contents of file (f)
def print_all(f):
	print f.read()

#rewind (f) by resetting its spot to 0 on the file, think of it as an array
def rewind(f):
	f.seek(0)
	
#tell the funtion to read line (linecount) in file (f) using the readline() function
def print_a_line(line_count, f):
	print line_count, f.readline()

#set a variable named current file to be the opend file we called for on boot	
current_file = open(input_file)

print "First let's print the whole file:\n"
#prints the whole contents of the file
print_all(current_file)

print "now lets rewind this like a tape"
#sets the file to start printing from the begining again
rewind(current_file)

print("lets print three lines:")
#just print the 3 lines
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
