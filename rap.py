import random
from stemming.porter2 import stem
import string

def extract_insult(line):
    return line.split(',')[1].rstrip().translate(None, string.punctuation).lower()

def uniquify(items):
    return list(set(items))

def is_not_repetitive(line1,line2):
    end1 = stem(line1.split(' ')[-1])
    end2 = stem(line2.split(' ')[-1])
    return end1 != end2 and end1 not in end2 and end2 not in end1

rapmap = {}
def init():
    with open('insults_cleaned.txt','r') as f:
        lines = f.readlines()
        predicates = [ extract_insult(line) for line in lines if len(line.split(',')) == 2 ]
        for predicate in predicates:
            last_word = predicate.split(' ')[-1]
            stemmed_last_word = stem(last_word)
            if len(stemmed_last_word) > 3:
                rhyme = stemmed_last_word[-3:]
                if rhyme in rapmap.keys():
                    rapmap[rhyme] = rapmap[rhyme] + [predicate]
                else:
                    rapmap[rhyme] = [predicate]

    for rhyme in rapmap.keys():
        rapmap[rhyme] = uniquify(rapmap[rhyme])
        if len(rapmap[rhyme]) < 2:
            del rapmap[rhyme]
        else:
            last_words = [ verse.split(' ')[-1] for verse in rapmap[rhyme] ]
            if len(uniquify(last_words)) < 2:
                del rapmap[rhyme]
            else:
                if not max([ is_not_repetitive(rapmap[rhyme][0],verse) for verse in rapmap[rhyme] ]):
                    del rapmap[rhyme]

def get_lines(num_lines):
    full_rap = ''    
    current_rhyme = random.choice(rapmap.keys())
    for i in range(num_lines/2):
        first = random.choice(rapmap[current_rhyme])
        rhyme_choices = [ verse for verse in rapmap[current_rhyme] if is_not_repetitive(verse,first) ]
        second = random.choice(rhyme_choices)
        full_rap += first + '<br/>'
        full_rap += second + '<br/>'
        current_rhyme = random.choice(rapmap.keys())
    return full_rap

if __name__ == '__main__':
    init()
    print get_lines(4)
