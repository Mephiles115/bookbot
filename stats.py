def get_num_words(text):
    return len(text.split())

def get_num_chars_sorted(text):
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    # Sortierte Liste nach Häufigkeit (absteigend)
    sorted_char_list = sorted(char_counts.items(), key=lambda pair: pair[1], reverse=True)
    return sorted_char_list

