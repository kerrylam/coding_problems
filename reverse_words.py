"""Write a function reverse_words() that takes a message as a list of characters
and reverses the order of the words in place.

Example:

message = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]

reverse_words(message)
#prints 'steal pound cake'
print("".join(message))
"""


def reverse_characters(letters, left_index, right_index):
    """take in a list of characters and reverse them in place."""

    while left_index < right_index:
        letters[left_index], letters[right_index] = letters[right_index], \
        letters[left_index]
        left_index += 1
        right_index -= 1


def reverse_words(message):
    """take in a message as a list of characters and reverse it in place."""
    reverse_characters(message, 0, len(message) - 1)
    current_word_start_index = 0
    for i in range(len(message) + 1):
        if (i == len(message)) or (message[i] == ' '):
            reverse_characters(message, current_word_start_index, i - 1)
            current_word_start_index = i + 1


print(reverse_words([ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]))

