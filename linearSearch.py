testString = ""
searchChar = ""
lastPosition = -1
replaceChar = ""

while testString == "": #Request a string input to be used through the program
    testString = input("Please enter some text to search: ")

while len(searchChar) != 1: #Request a character that is to be replaced in the string
    searchChar = input("Enter a character replace: ")

while len(replaceChar) != 1: #Request a character to replace the chosen character with
    replaceChar = input("Enter a character to replace {0} with: ".format(searchChar))

for x in range(len(testString)):
    if testString[x] == searchChar: #Search through the string for the chosen character
        testString.replace(searchChar,replaceChar) # This isn't working
        #Should replace the character with the character chosen, but doesn't
        lastPosition = x

print(testString)
