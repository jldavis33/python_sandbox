# Write a function called censor that takes two strings, text and word, as input.
# It should return the text with the word you chose replaced with asterisks.


def censor(text, word):
    # take 'word' and convert to asterisk
    word_censored = ''
    text_censored = []

    for _ in word:
        word_censored += '*'

    # split 'text' sentence by spaces, convert to list
    # loop through list
    for wrd in text.split(' '):
        # replace 'word' with 'censored' word
        if wrd == word:
            text_censored.append(word_censored)
        else:
            text_censored.append(wrd)

    # returned joined list by a space and reconvert into a sentence string
    print(' '.join(text_censored))
    return ' '.join(text_censored)

censor('I\'m a goofy goober', 'goofy')
