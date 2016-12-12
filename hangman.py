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
for i in a:
    print "#",
character = raw_input("enter a character")
if character in a:
    print "yes"
    
