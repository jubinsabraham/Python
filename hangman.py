import random
def select_word(fname = "/usr/share/dict/words"):
    words  = []
    with open(fname) as f:
        for i in f:
            i = i.strip()
            if i.isalpha() and i.islower() and len(i) > 6:
                words.append(i)
    return random.choice(words)
a = select_word()
def place_holder(a,guessed):
    print a
    message = ' '
    for i in a:
        if guessed == i:
           message = message.strip() + guessed
        else:
           message = message.strip() + "#"
    return message
count = 0
while count < 5:
    guessed = raw_input("enter a char:")
    hash_message = place_holder(a,guessed)
    
    print hash_message
    count = count + 1 
