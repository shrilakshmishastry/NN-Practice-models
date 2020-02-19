import  numpy as np
from numpy import array
import  tensorflow as tf
from tensorflow import keras as ks
# import matplotlib.pyplot as plt
#
#set of birds and animal names
word_set = ["crow","lion","sparrow","parrot","cheeta","rat","bat","rabbit",
"peacock","dove","sparrow","goose","ostrich","pigeon","turkey","hawk","bald eagle",
"raven","parrot","flamingo","seagull","swallow","blackbird","penguin","robin","swan",
"owl","stork","woodpecker","dog","puppy","turtle","rabbit","parrot","cat","kitten","goldfish",
"mouse","tropicalfish","hamster","cow","rabbit","ducks","shrimp","pig","goat","crab","deer",
"bee","sheep","fish","turkey","dove","chicken","horse","squirrel","dog","chimpanzee",
"ox","lion","panda","walrus","otter","mouse","kangaroo","goat","horse","monkey","cow",
"koala","mole","elephant","leopard","hippopotamus","giraffe","fox","coyote","hedgehong",
"sheep","deer",
"crow","lion","sparrow","parrot","cheeta","rat","bat","rabbit",
"peacock","dove","sparrow","goose","ostrich","pigeon","turkey","hawk","bald eagle",
"raven","parrot","flamingo","seagull","swallow","blackbird","penguin","robin","swan",
"owl","stork","woodpecker","dog","puppy","turtle","rabbit","parrot","cat","kitten","goldfish",
"mouse","tropicalfish","hamster","cow","rabbit","ducks","shrimp","pig","goat","crab","deer",
"bee","sheep","fish","turkey","dove","chicken","horse","squirrel","dog","chimpanzee",
"ox","lion","panda","walrus","otter","mouse","kangaroo","goat","horse","monkey","cow",
"koala","mole","elephant","leopard","hippopotamus","giraffe","fox","coyote","hedgehong",
"sheep","deer",
"crow","lion","sparrow","parrot","cheeta","rat","bat","rabbit",
"peacock","dove","sparrow","goose","ostrich","pigeon","turkey","hawk","bald eagle",
"raven","parrot","flamingo","seagull","swallow","blackbird","penguin","robin","swan",
"owl","stork","woodpecker","dog","puppy","turtle","rabbit","parrot","cat","kitten","goldfish",
"mouse","tropicalfish","hamster","cow","rabbit","ducks","shrimp","pig","goat","crab","deer",
"bee","sheep","fish","turkey","dove","chicken","horse","squirrel","dog","chimpanzee",
"ox","lion","panda","walrus","otter","mouse","kangaroo","goat","horse","monkey","cow",
"koala","mole","elephant","leopard","hippopotamus","giraffe","fox","coyote","hedgehong",
"sheep","deer",
"sheep","deer",
"crow","lion","sparrow","parrot","cheeta","rat","bat","rabbit",
"koala","mole","elephant","leopard","hippopotamus","giraffe","fox","coyote","hedgehong",
"peacock","dove","sparrow","goose","ostrich","pigeon","turkey","hawk","bald eagle",
"ox","lion","panda","walrus","otter","mouse","kangaroo","goat","horse","monkey","cow",
"raven","parrot","flamingo","seagull","swallow","blackbird","penguin","robin","swan",
"bee","sheep","fish","turkey","dove","chicken","horse","squirrel","dog","chimpanzee",
"owl","stork","woodpecker","dog","puppy","turtle","rabbit","parrot","cat","kitten","goldfish",
"mouse","tropicalfish","hamster","cow","rabbit","ducks","shrimp","pig","goat","crab","deer"]
# train labels 0 indicates a bird and 1 indicates an animal
train_labels = np.array([0,1,0,0,1,1,0,1,
0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,
0,0,0,1,1,1,1,0,1,1,1,
1,1,1,1,1,0,1,1,1,1,1,
0,1,1,0,0,0,1,1,1,1,
1,1,1,1,1,1,1,1,1,1,1,
1,1,1,1,1,1,1,1,1,
1,1,
0,1,0,0,1,1,0,1,
0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,
0,0,0,1,1,1,1,0,1,1,1,
1,1,1,1,1,0,1,1,1,1,1,
0,1,1,0,0,0,1,1,1,1,
1,1,1,1,1,1,1,1,1,1,1,
1,1,1,1,1,1,1,1,1,
1,1,
0,1,0,0,1,1,0,1,
0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,
0,0,0,1,1,1,1,0,1,1,1,
1,1,1,1,1,0,1,1,1,1,1,
0,1,1,0,0,0,1,1,1,1,
1,1,1,1,1,1,1,1,1,1,1,
1,1,1,1,1,1,1,1,1,
1,1,
1,1,
0,1,0,0,1,1,0,1,
1,1,1,1,1,1,1,1,1,
0,0,0,0,0,0,0,0,0,
1,1,1,1,1,1,1,1,1,1,1,
0,0,0,0,0,0,0,0,0,
0,1,1,0,0,0,1,1,1,1,
0,0,0,1,1,1,1,0,1,1,1,
1,1,1,1,1,0,1,1,1,1,1])
print(len(word_set))
print(len(train_labels))

train_set = np.zeros((320,15))
test_set = np.zeros((10,15))
print(len(word_set))
print(len(train_labels))
for i  in range(0,len(word_set)):
    x = iter(word_set[i])

    arr1 = np.zeros((1,15))
    for j in range(0,len(word_set[i])):
        arr = next(x)
        arr1[0][j] = (ord(arr)/122)



    train_set[i]= arr1
# train_set1 =  np.array(train_set)
# train_labels1 = np.array(train_labels)

for i  in range(0,10):
    x = iter(word_set[i+10])

    arr1 = np.zeros((1,15))
    for j in range(0,len(word_set[i+10])):
        arr = next(x)
        arr1[0][j] = (ord(arr)/122)

    test_set[i]= arr1
print(train_set[0])
print(train_labels)
print(test_set)

# model structure
# models = ks.Sequential()
# models.add(ks.layers.Flatten(input_shape=(15,)))
# # models.add(ks.layers.Dense(50,activation="relu",input_shape=(15,)))
# # models.add(ks.layers.Dense(10,activation="sigmoid"))
# models.add(ks.layers.Dense(20,activation="relu"))
# models.add(ks.layers.Dense(2))
# models.summary()
# models.compile(optimizer="adam",
# loss=ks.losses.SparseCategoricalCrossentropy(from_logits=True),
# metrics=['accuracy']
# )
#
#
# models.fit(train_set,train_labels,epochs=50000)
models.save("model17.h5")
# for loading preloaded model
models = ks.models.load_model("model16.h5")
prediction = models.predict(test_set)

for k in test_set[1]:
    k = int(k*122)
    print(chr(k))

print(prediction)
print(np.argmax(prediction[1]))
