#Function to count the words in a string
def get_num_words(text):
    #split the text into words seperated by commas
    words = text.split()
    #return the count of the words
    return len(words)

#Function to take the text from book as string and return the num of times a char appears
def get_num_char(text):
    #We don't want dupes, so we will run the text through .lower
    input_string = text.lower()

    #create empty dictionary
    char_count = {}

    #loop through the text and count each character, add tally to dict
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

#Function to take a dictionary and return the value "num" key
#This is how the .sort method knows how to sort the list of dictionaries
def sort_results(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_results)
    return sorted_list
