#imports argv from system
from sys import argv

#takes the variables from the comandline and stores them to the varibles script and filename
script, filename = argv

#set variable txt to open the file you called for on lauch
txt = open(filename)

#print out here is your first file... and the filename
print "here is your file %r:" % filename
#read the content of txt
print txt.read()

#prints type your file name again
print "Type your filename again:"

#set the variable fileagain to raw input 
file_again = raw_input("> ")

#set txt_again to open the file again
txt_again = open(file_again)

#print text again
print txt_again.read()