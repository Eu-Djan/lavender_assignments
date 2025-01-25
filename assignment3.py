user = input("Please enter a sentence: ") #input sentence and store in a variable

print(len(user)) #dispay total number of characters in the sentence including spaces

splitting = user.split(" ") #display total number of words in the sentence using split() to separate the words
print(len(splitting))

print(splitting[0],splitting[-1]) #Display the first and last word from the sentence

#Indexing and Slicing

print(user[0:3]) #Display the first 3 characters of the sentence

print(user[-3:]) #Display the last three characters of the sentence

print(user[::-1]) #Display the sentence in reverse order

#Modify the Sentence

print(user.upper()) # convert the entire sentence to uppercase and print

print(user.lower()) # convert the entire sentence to lowercase and print

print(user.replace(" ","-")) #Replace all spaces in the sentence with hyphens and print


