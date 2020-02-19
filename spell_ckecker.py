import numpy as np
import tensorflow as tf
from tensorflow import keras as ks
from numpy import array

word_set = [
"hegiddeera","hegiddira","hegidira",
"chennagide","chenagide",
"nillisi","nilsi",
"dhanyavaadagalu","dhanyavadagalu",
"meenu","minu",
"beyisu","beasiu",
"haalu","halu",
"ondu",
"yeradu","eradu",
"mooru","muru",
"nalakku","nalaku",
"aidu","idu",
"aaru","aru",
"yelu","elu",
"yentu","entu",
"ombathu","ombatu",
"hathu","hattu",
"uttara","uthara",
"dakshina","dashina",
"poorva","purva",
"pashchima","paschima",
"beligge","belagge",
"madyana","madhyana",
"sanje","sayankala","sanjhe",
"ratri","rathri",
"nenne","nene",
"eevathu","ivattu",
"naaddiddu","nadiddu",
"amma","ammaa",
"hegiddeera","hegiddira","hegidira",
"chennagide","chenagide",
"nillisi","nilsi",
"dhanyavaadagalu","dhanyavadagalu",
"meenu","minu",
"beyisu","beasiu",
"haalu","halu",
"ondu",
"yeradu","eradu",
"mooru","muru",
"nalakku","nalaku",
"aidu","idu",
"aaru","aru",
"yelu","elu",
"yentu","entu",
"ombathu","ombatu",
"hathu","hattu",
"uttara","uthara",
"dakshina","dashina",
"poorva","purva",
"pashchima","paschima",
"beligge","belagge",
"madyana","madhyana",
"sanje","sayankala","sanjhe",
"ratri","rathri",
"nenne","nene",
"eevathu","ivattu",
"naaddiddu","nadiddu",
"amma","ammaa"

]
train_labels = np.array([
0,0,0,
1,1,
2,2,
3,3,
4,4,
5,5,
6,6,
7,
8,8,
9,9,
10,10,
11,11,
12,12,
13,13,
14,14,
15,15,
16,16,
17,17,
18,18,
19,19,
20,20,
21,21,
22,22,
23,23,23,
24,24,
25,25,
26,26,
27,27,
28,28,
0,0,0,
1,1,
2,2,
3,3,
4,4,
5,5,
6,6,
7,
8,8,
9,9,
10,10,
11,11,
12,12,
13,13,
14,14,
15,15,
16,16,
17,17,
18,18,
19,19,
20,20,
21,21,
22,22,
23,23,23,
24,24,
25,25,
26,26,
27,27,
28,28
])
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
print(len(train_labels))
print(len(word_set))

train_set = np.zeros((118,15))
test_set = np.zeros((1,15))


for i in range(0,len(word_set)):
    x = iter(word_set[i])


    arr1 = np.zeros((1,15))
    for j in range(0,len(word_set[i])):
        arr = next(x)
        arr1[0][j] = (ord(arr)/122)
    train_set[i]= arr1


# print(train_set[0])
# print(train_labels)

# test_set
for i in range(21,22):
    x = iter(word_set[i])
    arr1 = np.zeros((1,15))
    for j in range(0,len(word_set[i])):
        arr = next(x)
        arr1[0][j] = (ord(arr)/122)



    test_set[0]= arr1

# print(test_set)

#
# model = ks.Sequential()
# model.add(ks.layers.Flatten(input_shape=(15,)))
# model.add(ks.layers.Dense(20,activation="relu"))
# model.add(ks.layers.Dense(29))
#
# model.compile(optimizer='adam',
#               loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
#               metrics=['accuracy'])
#
# model.fit(train_set,train_labels,epochs=15000)
# model.save("spell2.h5")


models = ks.models.load_model("spell2.h5")
prediction = models.predict(test_set)

for k in test_set[0]:
    k = int(k*122)
    print(chr(k))

print(prediction)
for i in range(0,1):
    print(np.argmax(prediction[i]))

for k in test_set[0]:
        k = int(k*122)
        print(chr(k))
