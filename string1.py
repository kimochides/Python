str=input("Enter a string:")

#string length
print("Length of string is:",len(str))

#convert to uppercase
print("Upper Case:",str.upper())
print(str.isupper()) #here, isupper checks for the input string, str

#convert to lowercase
print("Lower Case:",str.lower())
print(str.islower()) #here, islower checks for the input string, str

#capitalise the string
print("Capitalised:",str.capitalize())
#capitalize every word in the string
print("Capitalized every word:",str.title())

#count occurances of a substring
sub=input("Enter a substring to count it's occurances:")
print("Occurances of",sub,"is",str.count(sub))

#check if the string starts with a specific substring
prefix=input("Enter a prefix to check if the string starts with it:")
print("Starts with",prefix,":",str.startswith(prefix))

#check if the string ends with a specific substring
suffix=input("Enter a sufffix to check if the string ends with it:")
print("Ends with",suffix,":",str.endswith(suffix))

#replace a substring with another substring
old_sub=input("Enter the sub-string to be replaced:")
new_sub=input("Enter a replacement string:")
print("After replacement:",str.replace(old_sub,new_sub))

#split the string into a list of substrings
delim=input("Enter a delimiter to split the string:")
print("Split string:",str.split(delim))

#join a list of substrings into a single string
substr=input("Enter substrings to join (separated by space)").split()
print("Split string:",substr)
join_delim=input("Enter a delimiter to join the substrings:")
print("Joined string:",join_delim.join(substr))

#strip method removes any white space from the beginning or the end
print(str.strip())
#print(str.lstrip()) #left whitespace strip
#print(str.rstrip()) #right whitespace strip
#print(str.rjust())
print(str.rfind("l"))
print(str.rindex("l"))

age=36
name=input("Enter your name")
print(f"My name is {name}, and I am {age} years old")