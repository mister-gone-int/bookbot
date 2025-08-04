
def get_num_words(book_text):
    words = []
    words = book_text.split()
    num_words = len(words)
    print(f"Found {num_words} total words")


def get_char_count(text_string):
    character_count = {}
    
    for current_character in text_string.lower(): 
        if current_character in character_count:
            character_count[current_character] += 1
        else:
            character_count[current_character] = 1
    

    char_list = []
    for char, num in character_count.items():
        char_list.append({'char': char, 'num': num})
    sort_characters(char_list)


def sort_on(items):
    return items["num"]

def sort_characters(character_count):

    character_count.sort(reverse=False, key=sort_on)
    for current_character in character_count:
        if current_character["char"].isalpha():
            print(f"{current_character["char"]}: {current_character["num"]}")
