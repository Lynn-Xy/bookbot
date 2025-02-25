def get_word_count(book_text):
    num_words = len(book_text.split())
    return num_words

def get_char_count(book_text):
    new_dict = {}
    for char in book_text.lower():
        if char not in new_dict:
            new_dict[char] = 1
        elif char in new_dict:
            new_dict[char] += 1
    return new_dict

def get_report(dict):
    new_dict = {}
    for key in dict:
        if key.isalpha():
            new_dict[key] = dict[key]
    dict_list = []
    for key in new_dict:
        dict_list.append({key:new_dict[key]})
    dict_list.sort(key=lambda x: list(x.values())[0], reverse=True)
    return dict_list