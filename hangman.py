import random
count = 10
def select_word(fname = "/usr/share/dict/words"):
    words  = []
    with open(fname) as f:
        for i in f:
            i = i.strip()
            if i.isalpha() and i.islower() and len(i) > 6:
                words.append(i)
    return random.choice(words)

def wrong_guess(guess,a):
    if guess not in wrong_list:
            if  guess not in a:
                wrong_list.append(guess)
                wrong_list.append(",")
    else:
        print "enter something different"

    return wrong_list

a = select_word()
print a
#print len(a)
wrong_list =[]
hash_list = []
for i in range(len(a)):
     hash_list.append("#")
print hash_list
while count > 0:
    guessed = raw_input("enter your guess:")
    wrong_guess_list = wrong_guess(guessed,a)
    print "Wrong Guesses:",''.join(wrong_guess_list)
    print "Turns remaining:",count
    indices = [i for i, x in enumerate(a) if x == guessed]
    for i in range(len(indices)):
        pos = indices[i]
        hash_list[pos] = guessed
    print ''.join(hash_list)
    count = count - 1
