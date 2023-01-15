# Parse dictionary.json into python set, then dump into dictionary.pkl

import json
import pickle

# with open("dict.txt", "r") as file:
#     list = []
#     for line in file:
#         list.append(line.strip().lower())
            
#     with open("dictionary.json", "w") as json_file:
#         json.dump(list, json_file)

FILENAME = "dictionary.json"
PKL_FILENAME = "dictionary.pkl"

with open(FILENAME, 'r') as file:
    # Read from json file, parse to set (only words >= length of 4)
    dictionary_array = json.load(file)
    dictionary_set = set(dictionary_array)
    dictionary_set = {word for word in dictionary_set if len(word) >= 4}
        
    # dump set into pickle file
    pkl_file = open(PKL_FILENAME, 'wb')
    pickle.dump(dictionary_set, pkl_file)
    pkl_file.close()