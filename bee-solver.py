import pickle

FILENAME = "dictionary.pkl"

letters = list(input("Please enter all 7 letters without spaces: ").lower())
gold_letter = input("Please enter the center (gold) letter: ").lower()

# load set from dictionary.pkl
with open(FILENAME, "rb") as file:
    word_dictionary = pickle.load(file)
    
def prefix_contains(prefix_str):
    for word in word_dictionary:
        loc = word.index(prefix_str) if prefix_str in word else -1
        if loc == 0:
            return True
    return False
    
    

def find_words(word):
    # base case 1: we find a word in the dictionary that contains the gold letter
    # we've already pruned words < length of 4 so don't have to check word length
    if word in word_dictionary and gold_letter in word:
        print(word)
    
    if prefix_contains(word):
        for letter in letters:
            find_words(word + letter)
        
    else:
        return
    
find_words("")