# using permutation of words and soundex algorithm
#combination with  similar value of soundex algorithm of word set
 # is treated phonetically same
 # problem here is it doesn't work with kannada words

from itertools import permutations
import phonetics





word_set =  [
"amma",
"meenu",


"nillisi",


"beyisu",
"haalu",
"ondu",
"yeradu",
"mooru",
"nalakku",
"aidu",
"aaru",
"yelu",
"yentu",
"ombathu",
"hathu",
"uttara",
"dakshina",
"poorva",
"pashchima",
"beligge",
"madyana",
"sanje",
"ratri",
"nenne",
"eevathu",
"hegiddeera",
"chennagide",
"dhanyavaadagalu",
"naaddiddu"
]



train_labels = []
train_sets = []
print("hello")
permutation = permutations('abcdefghijklmnopqrstuvwxyz',len(word_set[0]))
for i in permutation:

    if(phonetics.soundex(word_set[0])== phonetics.soundex(i)):
        # print("yes")
        # print(i,word_set[0])


for x in range(0,len(word_set)):
    print(x)
    permutation = permutations('abcdefghijklmnopqrstuvwxyz',len(word_set[x]))
    print(word_set[x])
    for i in permutation:

        if(phonetics.soundex(word_set[x])== phonetics.soundex(i)):
            train_sets.append(i)
            train_labels.append(x)
            # print(i,x)
            print(i,x)
    permutation = permutations('abcdefghijklmnopqrstuvwxyz',len(word_set[x])-1)
    for j in permutation:
        if(phonetics.soundex(word_set[x])==phonetics.soundex(j)):
            train_sets.append(j)
            train_labels.append(x)
            print(j,x)
print(train_labels,train_sets)
