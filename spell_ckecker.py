import numpy as np
import tensorflow as tf
from tensorflow import keras as ks
from numpy import array

# word_set = [
# "hegiddeera","hegiddira","hegidira",
# "chennagide","chenagide",
# "nillisi","nilsi",
# "dhanyavaadagalu","dhanyavadagalu",
# "meenu","minu",
# "beyisu","beasiu",
# "haalu","halu",
# "ondu",
# "yeradu","eradu",
# "mooru","muru",
# "nalakku","nalaku",
# "aidu","idu",
# "aaru","aru",
# "yelu","elu",
# "yentu","entu",
# "ombathu","ombatu",
# "hathu","hattu",
# "uttara","uthara",
# "dakshina","dashina",
# "poorva","purva",
# "pashchima","paschima",
# "beligge","belagge",
# "madyana","madhyana",
# "sanje","sayankala","sanjhe",
# "ratri","rathri",
# "nenne","nene",
# "eevathu","ivattu",
# "naaddiddu","nadiddu",
# "amma","ammaa",
# "hegiddeera","hegiddira","hegidira",
# "chennagide","chenagide",
# "nillisi","nilsi",
# "dhanyavaadagalu","dhanyavadagalu",
# "meenu","minu",
# "beyisu","beasiu",
# "haalu","halu",
# "ondu",
# "yeradu","eradu",
# "mooru","muru",
# "nalakku","nalaku",
# "aidu","idu",
# "aaru","aru",
# "yelu","elu",
# "yentu","entu",
# "ombathu","ombatu",
# "hathu","hattu",
# "uttara","uthara",
# "dakshina","dashina",
# "poorva","purva",
# "pashchima","paschima",
# "beligge","belagge",
# "madyana","madhyana",
# "sanje","sayankala","sanjhe",
# "ratri","rathri",
# "nenne","nene",
# "eevathu","ivattu",
# "naaddiddu","nadiddu",
# "amma","ammaa"
#
# ]
# train_labels = np.array([
# 0,0,0,
# 1,1,
# 2,2,
# 3,3,
# 4,4,
# 5,5,
# 6,6,
# 7,
# 8,8,
# 9,9,
# 10,10,
# 11,11,
# 12,12,
# 13,13,
# 14,14,
# 15,15,
# 16,16,
# 17,17,
# 18,18,
# 19,19,
# 20,20,
# 21,21,
# 22,22,
# 23,23,23,
# 24,24,
# 25,25,
# 26,26,
# 27,27,
# 28,28,
# 0,0,0,
# 1,1,
# 2,2,
# 3,3,
# 4,4,
# 5,5,
# 6,6,
# 7,
# 8,8,
# 9,9,
# 10,10,
# 11,11,
# 12,12,
# 13,13,
# 14,14,
# 15,15,
# 16,16,
# 17,17,
# 18,18,
# 19,19,
# 20,20,
# 21,21,
# 22,22,
# 23,23,23,
# 24,24,
# 25,25,
# 26,26,
# 27,27,
# 28,28
# ])
# train_labels_set = [
# "hegiddeera","hegiddeera","hegiddeera",
# "chennagide","chennagide",
# "nillisi","nillisi",
# "dhanyavaadagalu","dhanyavaadagalu",
# "meenu","meenu",
# "beyisu","beyisu",
# "haalu","haalu",
# "ondu",
# "yeradu","yeradu",
# "mooru","mooru",
# "nalakku","nalakku",
# "aidu","aidu",
# "aaru","aaru",
# "yelu","yelu",
# "yentu","yentu",
# "ombathu","ombathu",
# "hathu","hathu",
# "uttara","uttara",
# "dakshina","dakshina",
# "poorva","poorva",
# "pashchima","pashchima",
# "beligge","beligge",
# "madyana","madyana",
# "sanje","sanje","sanje",
# "ratri","ratri",
# "nenne","nenne",
# "eevathu","eevathu",
# "naaddiddu","naaddiddu",
# "amma","amma"
# ]

# input_word = input()
# word = list(input_word)
kannada_word_set = []
with open("converted_word.txt","r") as cv_file:
    # print(cv_file)
    stripped = (line for line in cv_file)
    # t = stripped.split(",")
    # print(t)
    for k in stripped:
        # print(k.strip("\n"))
        kannada_word_set.append(k.strip("\n"))
        # print(type(word))
        # print()
        # word_set.append(word)
    # for i in cv_file:
    #     print(i)
    #     word_set.append(i)

# print(word_set[1])
# print("hello")
word_set = []
train_labels = []
num =0
for w in kannada_word_set:
    word = list(w)
    # print(word)
    # print(num)
    k=0
    for i in word:

        if i == word[k-1]:
            if(i=="o" ):
                new = word.copy()
                new.pop(k-1)

                new.pop(k-1)

                new.insert(k-1,"u")
                new = ''.join(map(str,new))
                word_set.append(new)
                train_labels.append(num)

            k = k+1
        elif((k<len(word)-1 ) and i+i ==  word[k+1]+i   ):
            new = word.copy()
            new.pop(k)
            new1 = ''.join(map(str,new))
            word_set.append(new1)
            train_labels.append(num)

            if (i=='a'or i == 'e'  or  i == 'o'   ):


                new1 = new.copy()
                new1.insert(k+1,i)

                new1 = ''.join(map(str,new1))

                word_set.append(new1)
                train_labels.append(num)

            if (k<(len(word)-1) and k<(len(word)-1) and  word[k+1]=="a")    :

                new1 = new.copy()

                new1.insert(k+1,'h')

                new1 = ''.join(map(str,new1))

                word_set.append(new1)
                train_labels.append(num)

            if (k<(len(word)-1) and i == 'e'):

                new1 = new.copy()

                new1.pop(k)
                new1.insert(k,'i')

                new1 = ''.join(map(str,new1))

                word_set.append(new1)
                train_labels.append(num)




            if(i=="a" and (new[k-1]=='b' or new[k-1]=='c' or new[k-1]=='d'
            or new[k-1]=='f' or new[k-1]=='g' or new[k-1]=='j' or new[k-1]=='k' or
            new[k-1]=='l' or new[k-1]=='m' or new[k-1]=='n' or new[k-1]=='p' or new[k-1]=='q' or
            new[k-1]=='r' or new[k-1]=='s' or new[k-1]=='t' or new[k-1]=='v' or
            new[k-1]=='w' or new[k-1]=='x' or new[k-1]=='y' or new[k-1]=='z' ))    :

                new1 = new.copy()

                new1.insert(k,'ha')

                new1 = ''.join(map(str,new1))

                word_set.append(new1)
                train_labels.append(num)

            if(i == "e" and k<(len(word)-1) and new[k+1] == "y")    :

                new1 = new.copy()

                new1.pop(k+1)
                new1.insert(k+1,'a')

                new1 = ''.join(map(str,new1))

                word_set.append(new1)
                train_labels.append(num)

            if( i =="y"  and k<(len(word)-1) and  new[k+1] == "e")    :

                new1 = new.copy()

                new1.pop(k)


                new1 = ''.join(map(str,new1))

                word_set.append(new1)
                train_labels.append(num)


            if(i == "h" and k<(len(word)-1)and  new[k+1]=="r")    :

                new1 = new.copy()

                new1.pop(k)


                new1 = ''.join(map(str,new1))

                word_set.append(new1)
                train_labels.append(num)


            if(i == "h" and k<(len(word)-1) and  new[k+1]=="a")    :

                new1 = new.copy()

                new1.pop(k)


                new1 = ''.join(map(str,new1))

                word_set.append(new1)
                train_labels.append(num)


            if(i == "a" and k<(len(word)-1) and  new[k+1]=="i")    :

                new1 = new.copy()

                new1.pop(k)


                new1 = ''.join(map(str,new1))

                word_set.append(new1)
                train_labels.append(num)


            if(i == "y")    :

                new1 = new.copy()

                new1.pop(k)
                new1.pop(k)
                new1.pop(k-1)

                new1.insert(k,"a")

                new1.insert(k,"i")

                new1.append("a")

                new1.append("h")

                new1 = ''.join(map(str,new1))

                word_set.append(new1)
                train_labels.append(num)


            if(k<len(word)):
                k = k+1
        else:

            if(k<(len(word)-1) and (i == 'b' or i=="c" or i == "d" or i =="f" or i == "g" or i == "j" or i == "k"   or   i == "p" or i == "q"  or i == "s" or i == "t" or   i == "w"  or i == "x"  or i == "z") and (word[k+1]!="h")):
                new = word.copy()

                new.insert(k+1,"h")

                new = ''.join(map(str,new))

                word_set.append(new)
                train_labels.append(num)



            if (i=='a'or i == 'e'   or i == 'o'  ):

                new = word.copy()

                new.insert(k+1,i)

                new = ''.join(map(str,new))

                word_set.append(new)
                train_labels.append(num)


            if (k<(len(word)-1) and word[k+1]=="a" and i != "h" and (i != "r" and i != "y" and i!="l" and  i!="v" ) )    :


                new = word.copy()

                new.insert(k+1,'h')

                new = ''.join(map(str,new))

                word_set.append(new)
                train_labels.append(num)


            if (k<(len(word)-1) and i == 'e'):

                new = word.copy()

                new.insert(k,'i')

                new = ''.join(map(str,new))

                word_set.append(new)
                train_labels.append(num)


            # if((word_set[len(word_set)]=='a'or new[k] == 'e'  or new[k]== 'i' or new[k]== 'o' or new[k] == 'u')and(k<(len(word)-1) or k<(len(word)-1) )and(i+i == new[k+1]+i or i+i == new[k-1]+i or i+i+i == new[k-1]+i+new[k+1]) ):
            #     print("5")
            #     new = word.copy()
            #     print("new",new)
            #     new.pop(k)
            #     print("after new",new)
            #     new = ''.join(map(str,new))
            #     print("new str",new)
            #     word_set.append(new)
            #     if(new[k]=='e'):
            #         new.insert(k,'i')
            #         print("after new",new)
            #         new = ''.join(map(str,new))
            #         print("new str",new)
            #         word_set.append(new)
            #     if(new[k]==a)    :
            #         new.insert(k,'ha')
            #         print("after new",new)
            #         new = ''.join(map(str,new))
            #         print("new str",new)
            #         word_set.append(new)


            if(i=="a" and (word[k-1]=='b' or word[k-1]=='c' or word[k-1]=='d'
            or word[k-1]=='f' or word[k-1]=='g' or word[k-1]=='j' or word[k-1]=='k' or
             word[k-1]=='m' or word[k-1]=='n' or word[k-1]=='p' or word[k-1]=='q' or
             word[k-1]=='s' or word[k-1]=='t'  or
            word[k-1]=='w' or word[k-1]=='x' or  word[k-1]=='z' ))    :


                new = word.copy()


                if(word[k-1]==word[k-2]):

                    new.pop(k)
                    new.pop(k-1)


                new.insert(k,'a')
                new.insert(k,'h')


                new = ''.join(map(str,new))

                word_set.append(new)
                train_labels.append(num)

            if(i == "e" and k<(len(word)-1) and word[k+1] == "y")    :

                new = word.copy()

                new.pop(k+1)
                new.insert(k+1,'a')

                new = ''.join(map(str,new))

                word_set.append(new)
                train_labels.append(num)


            if( i =="y"  and k<(len(word)-1) and  word[k+1] == "e")    :

                new = word.copy()

                new.pop(k)


                new = ''.join(map(str,new))

                word_set.append(new)
                train_labels.append(num)



            if(i == "h" and k<(len(word)-1) and  word[k+1]=="r")    :

                new = word.copy()

                new.pop(k)


                new = ''.join(map(str,new))

                word_set.append(new)
                train_labels.append(num)


            if(i == "h" and k<(len(word)-1) and word[k+1]=="a")    :

                new = word.copy()

                new.pop(k)



                new = ''.join(map(str,new))

                word_set.append(new)
                train_labels.append(num)


            if(i == "a" and k<(len(word)-1) and word[k+1]=="i")    :

                new = word.copy()

                new.pop(k)


                new = ''.join(map(str,new))

                word_set.append(new)
                train_labels.append(num)


            if(i == "i"    ):

                new = word.copy()

                new.pop(k)
                new.insert(k,'e')
                new.insert(k,"e")

                new = ''.join(map(str,new))

                word_set.append(new)
                train_labels.append(num)
                new = word.copy()

                new.pop(k)

                new.insert(k,"y")

                new = ''.join(map(str,new))

                word_set.append(new)
                train_labels.append(num)

            if(i == "y" and (word[k-1]=='b' or word[k-1]=='c' or word[k-1]=='d'or word[k-1]=='f' or word[k-1]=='g' or word[k-1]=='j' or word[k-1]=='k' or word[k-1]=='l' or word[k-1]=='m' or word[k-1]=='n' or word[k-1]=='p' or word[k-1]=='q' or word[k-1]=='r' or word[k-1]=='s' or word[k-1]=='t' or word[k-1]=='v' or word[k-1]=='w' or word[k-1]=='x' or word[k-1]=='y' or word[k-1]=='z' )   ):

                new = word.copy()

                new.pop(k)

                new.insert(k,"i")
                new.insert(k,"a")
                new = ''.join(map(str,new))

                word_set.append(new)
                train_labels.append(num)

            if(i == "a" and k<(len(word)-1) and word[k+1]=="u"):

                new = word.copy()

                new.pop(k)


                new.insert(k,"o")
                # new.insert(k,"a")
                new = ''.join(map(str,new))

                word_set.append(new)
                train_labels.append(num)

            if(k<len(word)):
                k = k+1

    num = num+1
    # print(num)
        # if (word[i])

# print(len(word_set))
t = 0
for k in word_set:
    print(train_labels[t])
    t = t+1
    print(k)

print(len(train_labels))
print(len(word_set))

train_labels = np.asarray(train_labels)
print(type(train_labels))
train_set = np.zeros((5300,25))
test_set = np.zeros((10,25))


for i in range(0,len(word_set)):
    x = iter(word_set[i])


    arr1 = np.zeros((1,25))
    for j in range(0,len(word_set[i])):
        arr = next(x)
        arr1[0][j] = (ord(arr)/122)
    train_set[i]= arr1


# print(train_set)
# print(train_labels)

# test_set
for i in range(21,22):
    x = iter(word_set[i])
    arr1 = np.zeros((1,25))
    for j in range(0,len(word_set[i])):
        arr = next(x)
        arr1[0][j] = (ord(arr)/122)



    test_set[0]= arr1

# print(test_set)


model = ks.Sequential()
model.add(ks.layers.Flatten(input_shape=(25,)))
model.add(ks.layers.Dense(20,activation="relu"))
model.add(ks.layers.Dense(5299))

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.fit(train_set,train_labels,epochs=30000)
model.save("spell3.h5")


# models = ks.models.load_model("spell2.h5")
prediction = model.predict(test_set)

for k in test_set[0]:
    k = int(k*122)
    print(chr(k))

print(prediction)
for i in range(0,1):
    print(np.argmax(prediction[i]))

for k in test_set[0]:
        k = int(k*122)
        print(chr(k))
