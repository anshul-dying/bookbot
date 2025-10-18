def count_words(text: str):
    cont = text.strip().split()
    return len(cont)

def num_letters_in_text(text:str):
    text_lower = text.lower()
    letters = {}
    for letter in text_lower:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters

def sorted_dict(letter_dict: dict):
    sorted_letters_dict = dict(sorted(letter_dict.items(), key=lambda item : item[1], reverse=True))
    return sorted_letters_dict