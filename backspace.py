"""Given two strings S and T, return if they are equal when both are typed into
empty text editors. # means a backspace character.

Example 1: 

    Input: S = "ab#c," T = "ad#c"
    Output: True
    Explanation: Both S and T become "ac".

Example 2: 

    Input: S = "ab##," T = "c#d#"
    Output: True
    Explanation: Both S and T become "".

Example 3: 

    Input: S = "a##c," T = "#a#c"
    Output: True
    Explanation: Both S and T become "c".

Example 4: 

    Input: S = "a#c," T = "b"
    Output: False
    Explanation: S becomes "c" while T becomes "b".

Note:
    1. 1 <= S.length <= 200
    2. 1 <= T.length <= 200
    3. S and T only contail lowercase letters and '#' characters
"""


1st solution:
_______________________________________________________________


def same_string_with_backspace(S, T):
    s_list = []
    t_list = []

    for letter in S:
        if s_list and letter == '#':
            s_list.pop()
        elif letter != '#':
            s_list.append(letter)

    for letter in T:
        if t_list and letter == '#':
            t_list.pop()
        elif letter != '#':
            t_list.append(letter)

    return "".join(s_list) == "".join(t_list)


2nd solution:
_______________________________________________________________



def same_string(S, T):

    return edit_text(S) == edit_text(T)


def edit_text(string):
    string_list = []

    for letter in string:
        if string_list and letter == '#':
            string_list.pop()
        elif letter != '#':
            string_list.append(letter)

    return "".join(string_list)


