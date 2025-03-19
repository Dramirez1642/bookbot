def get_book_text(file_path):
    """Given a file path to a book gather all the content as a string and return it.
    """
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def word_count(str):
    """Given a string determine and return the word count.
    """
    words = str.split()
    return len(words)

def character_count(str):
    """Given a string determine and return the number of characters in the string.
    """
    counts = {}
    for character in str:
        current_char = character.lower()
        if current_char in counts:
            counts[current_char] += 1
        else:
            if not current_char.isalpha():
                continue
            else:
                counts[current_char] = 1
    return counts

def sort_on(dict):
    return dict["count"]

def report_results(char_dict):
    """Given a dictionary of characters and their count generate and return a 
    sorted list of dictionaries representing the character counts.
    """
    sorted_list = []
    for key in char_dict:
        sorted_list.append({"character": key, "count":char_dict[key]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
