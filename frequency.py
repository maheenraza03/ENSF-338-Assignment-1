
import collections
import string
import matplotlib.pyplot as plt

def count_letters(filename):
    with open(filename, "r", errors="ignore") as inF:  ##reads the file name and opens it in read mode
        text = inF.read()

    alphabet = list(string.ascii_lowercase) ## makes a list of all the alphabets in lowercase

    letter_counts = collections.defaultdict(int) ## a dictionary in order to save the letter and the corresponding number of occurences

    i = 0 ## used so it starts at alphabet[0] (aka the letter 'a')

    for i in range(len(alphabet)): ## goes from a[0] to a[26]
        for letter in text: ## looks at each letter in the text file
            if letter.isalpha(): ## if the letter is an uppercase letter, it will be turned into lowercase
                letter.lower()
            if alphabet[i] == letter.lower(): ## compares the letter in the list and the letter in the gile
                letter_counts[letter.lower()] += 1 ## saves the occruences in the dict

    for letter, count in letter_counts.items(): ## prints out each letter and the corresponding number
        print(letter, count)


    ## used to display the bar/histogram
    plt.bar(letter_counts.keys(), letter_counts.values())
    plt.xlabel("Letter")
    plt.ylabel("Occurrences")
    plt.title("Letter Occurences in the text file for The Project Gutenberg")
    plt.show()
    
count_letters("TheProjectGutenberg.txt")


