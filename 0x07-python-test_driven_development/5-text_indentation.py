#!/usr/bin/python3
def text_indentation(text):
    """
    Module that pritns a text with 2 new lines after each . , ? and :
    """
    buf = ''
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = list(text)
    for i in range(len(text)):
        if text[i] in [':', '?', '.']:
            text[i + 1] = '\n\n'
    for i in range(len(text)):
        buf += text[i]
    print(buf, end='')
