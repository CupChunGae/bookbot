def num_of_words(text):
    words_to_count = text.split()
    print(f"Found {len(words_to_count)} total words")
    
def character_count(text):
    from collections import Counter
    returning_dict = {}
    for character in text.lower():
        if character not in returning_dict:
            returning_dict[character] = 1
        else:
            returning_dict[character] += 1
    return returning_dict

def sorting_dict(text_dict):
    #take in the dictionary and turn it into a list of dictionaries
    def sort_on(list_of_dicts):
        return list_of_dicts["num"]
    returning_arr = []
    for item in text_dict:
        returning_arr.append({"char":item, "num": text_dict[item]})
    returning_arr.sort(reverse=True, key = sort_on)
    return returning_arr