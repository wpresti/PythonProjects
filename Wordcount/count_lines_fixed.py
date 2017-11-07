f = open("birds.txt", "r")
data = f.read()
f.close()


lines = data.split("\n")
print("Wrong: The number of lines is", len(lines))

#keyword not checks for emptiness
for l in lines:
    if not l:   #can also do this: if len(l) == 0
        lines.remove(l) #if line is emtpy, remove from list!

print("Right: The number of lines is", len(lines))
