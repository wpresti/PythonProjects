import sys

# takes in list data, returns number of words
def count_words(data):
    words = data.split(" ")
    num_words = len(words)
    return num_words

#count lines with white space lines removed
def count_lines(data):
    lines = data.split("\n") #split based off of new line -- store to list
    for l in lines:
        if len(l) == 0: #if blank, remove
        #if not l:
            lines.remove(l)

    return len(lines)

#only run code below if i ran this file from command line
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python word_count.py <file>")
        exit(1)

    filename = sys.argv[1]

    f = open(filename, "r")
    data = f.read()
    f.close()

    num_words = count_words(data)
    num_lines = count_lines(data)

    print("The number of words: ", num_words)
    print("The number of lines: ", num_lines)
