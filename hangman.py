import random
count = 9
guessed_word = ''
def select_word(fname = "/usr/share/dict/words"):
    words  = []
    with open(fname) as f:
        for i in f:
            i = i.strip()
            if i.isalpha() and i.islower() and len(i) > 6:
                words.append(i)
    return random.choice(words)

def wrong_guess(guess,a,count):
    if guess not in wrong_list:
            if  guess not in a:
                wrong_list.append(guess)
                wrong_list.append(",")
    else:
        count = count + 1
        print "enter something different"
    return count,wrong_list

a = select_word()
#print a
wrong_list =[]
hash_list = []
for i in range(len(a)):
     hash_list.append("#")
print ('').join(hash_list)
print "Wrong Guesses:"
print "Turns Remsining:10"
while count >= 0:
    guessed = raw_input("enter your guess:")
    count,wrong_guess_list = wrong_guess(guessed,a,count)
    print "Wrong Guesses:",''.join(wrong_guess_list)
    print "Turns remaining:",count
    indices = [i for i, x in enumerate(a) if x == guessed]
    if  indices:
        print "Secret Word Contains:",guessed
    else:
        print "Secret Word doesnt contain",guessed
    for i in range(len(indices)):
        pos = indices[i]
        hash_list[pos] = guessed
    guessed_word = ''.join(hash_list)
    print guessed_word
    if guessed_word == a:
        print "Congratulations! The Secret Word was",a
        break
    if count == 0:
        print "You fail"
    if count == 0 and guessed_word == a:
        print "Congratulations! The Secret Word was",a
    count = count - 1
    
