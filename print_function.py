#!/usr/bin/python

#Python program to discover print function

#print without any parameters
print()

#Print a static message
print( "Welcome to discover python3 print function" )

#Print value stored in variable
string1 = "This is a simple line to print"
print( string1 )

#Print two variables
#The default parameters for sep is ' ', end is '\n'
string2 = "Printing another line adjacent to first line"
print( string1, string2 )

#printing two variables by modifying default sep, end parameters
string3 = "This is the another line printing using separator '. '"
print( string1, string3, sep = '. ',end = '\n' )

print('\n#Printing static message along with variables')
name = "Ram"
print( "Howdy", name, "!! How are you doing" )
print( "All the best " + name + '!' )
