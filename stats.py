def count_words(content):
    num_words = len(content.split())
    print(f"{num_words} words found in the document")

def get_character_stats(content):
    dict = {}
    list = content.split()

    for word in list:
        for char in word:
            element = char.lower()
            if element not in dict:
                dict[element] = {"char": element, "amount": 1}
            elif element in dict:
                dict[element]["amount"] += 1

    return dict


def sort_on(items):
    return items["amount"]


def sort_characters(dict):
    result = []

    for element in dict:
        result.append(dict[element])

    result.sort(reverse=True, key=sort_on)

    return result

def print_report(dict):
    sorted_chars = sort_characters(dict)

    print("""
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------""")

    for char_data in sorted_chars:
        if char_data["char"].isalpha():  # Only print alphabetic characters
            print(f"{char_data['char']}: {char_data['amount']}")

    print("============= END ===============")
