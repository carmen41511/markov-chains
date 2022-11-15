"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    text = open(file_path).read()

    return text


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    ls = text_string.split()
    ls_tuple = []

#does the range need to be -2 instead? so that we don't have a possible pair of the double ams?
    for i in range(len(ls)-2):
        tu = (ls[i], ls[i+1])
        if i != len(ls)-2:
            val= [ls[i+2]]
        if tu not in chains:
            chains[tu] = val
        else:
            chains[tu] += val
            
            

    # for k,v in sorted(chains.items()):
    #     print(k,v)
    # for t in ls_tuple:
        # chains[t] = t

    return chains


def make_text(chains):
    """Return text from chains."""
    
    words = []
    random_key = choice(list(chains.keys())) 
    random_word = choice(chains[random_key]) #a randomw word from the random key we picked

#adds first 3 words  ex: ['a', 'mouse?', 'Would']
    for i in random_key:
        words.append(i)
    words.append(random_word) 
    
#keeps adding next words to first 3 words-getting keyerror on line 83
    while chains.get(random_key) != None:
        random_key = (random_key[1], random_word)
        try:
            random_word = choice(chains[random_key])
        except:
            break
        
        for i in random_key:
            words.append(i)
        words.append(random_word)
    
    # print(words)
    return ' '.join(words)


input_path = 'gettysburg.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)

# text = input_text
# chain = make_chains(text)
# make_text(chain)