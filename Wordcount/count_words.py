f = open("birds.txt", "r")
data = f.read()
f.close()

words = data.split(" ") #split on space and store to list: words

print("The words in the text are:")
print(words)
num_words = len(words) # count number of words in list
print("The number of words is ", num_words)

#find number of lines in text
lines = data.split("\n")
print("The lines in the text are:")
print(lines)
print("The number of lines is", len(lines))
