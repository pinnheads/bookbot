def get_num_words(content):
    """Returns the number of words in a string"""
    return len(content.split())


def count_char(content):
    """Returns the count of appearance of each character in a string"""
    counts = {}
    for char in content:
        lower_char = char.lower()
        if lower_char in counts:
            counts[lower_char] += 1
        else:
            counts[lower_char] = 1
    return counts


def sort_on(items):
    """Return sorting key"""
    return items["num"]


def sort_char_count(counts):
    """Returns sorted list of alphabetical character counts"""
    list_char_counts = [{"char": char, "num": count}
                        for char, count in counts.items() if char.isalpha()]
    list_char_counts.sort(key=sort_on, reverse=True)
    return list_char_counts
