import time
import sys
from itertools import combinations

t0 = time.time()

def has_vowells(word):
    return 'a' in word or 'e' in word or 'i' in word or 'o' in word or 'u' in word or 'y' in word

def make_dictionary():
    mapp = set()
    for line in open('/Users/chris/Downloads/dictionary.txt').readlines():
        mapp.add(line.strip())
    return mapp

def anagrams(s):
    if s == "":
        return [s]
    else:
        ans = []
        for an in anagrams(s[1:]):
            for pos in range(len(an)+1):
                ans.append(an[:pos]+s[0]+an[pos:])
        return ans

letters = sys.argv[1]

# generate all cominations of words for any size
combos = set()
for x in range(1, len(letters)+1): # one loop per letter
    these_combos = combinations(letters, x)
    [combos.add(''.join(z)) for z in these_combos] # coerce each to string

# generate all anagrams for each combinations (try to skip duplicates)
words = set()
for combo in combos:
    for w in anagrams(combo):
        words.add(w)

# remove words that have no vowells
words = [word for word in words if has_vowells(word)]

print "checking %s words against dictionary..." % len(words)

# check each word against the dictionary (takes a long time)
matches = []
dictionary = make_dictionary()
for word in words:
    if dictionary.issuperset([word]):
        matches.append(word)

# sort matches and print onto screen
for word in sorted(matches):
    print word

print "took %.3f seconds" % (time.time() - t0)