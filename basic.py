from numpy import exp, array, random, dot
import numpy as np


class NeuralNetwork():
    def __init__(self):
        # Seed the random number generator, so it generates the same numbers
        # every time the program runs.
        random.seed(1)

        # We model a single neuron, with 3 input connections and 1 output connection.
        # We assign random weights to a 3 x 1 matrix, with values in the range -1 to 1
        # and mean 0.
        self.synaptic_weights = 2 * random.random((15, 2)) - 1

    # The Sigmoid function, which describes an S shaped curve.
    # We pass the weighted sum of the inputs through this function to
    # normalise them between 0 and 1.
    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))

    # The derivative of the Sigmoid function.
    # This is the gradient of the Sigmoid curve.
    # It indicates how confident we are about the existing weight.
    def __sigmoid_derivative(self, x):
        return x * (1 - x)

    # We train the neural network through a process of trial and error.
    # Adjusting the synaptic weights each time.
    def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
        for iteration in range(number_of_training_iterations):
            # Pass the training set through our neural network (a single neuron).
            output = self.think(training_set_inputs)

            # Calculate the error (The difference between the desired output
            # and the predicted output).
            print(training_set_outputs.shape,output.shape)
            error = training_set_outputs - output


            # Multiply the error by the input and again by the gradient of the Sigmoid curve.
            # This means less confident weights are adjusted more.
            # This means inputs, which are zero, do not cause changes to the weights.
            adjustment = dot(training_set_inputs.T, error * self.__sigmoid_derivative(output))

            # Adjust the weights.
            self.synaptic_weights += adjustment

    # The neural network thinks.
    def think(self, inputs):
        # Pass inputs through our neural network (our single neuron).
        return self.__sigmoid(dot(inputs, self.synaptic_weights))


if __name__ == "__main__":

    #Intialise a single neuron neural network.
    neural_network = NeuralNetwork()

    print ("Random starting synaptic weights: ")
    print (neural_network.synaptic_weights)

    # The training set. We have 4 examples, each consisting of 3 input values
    # and 1 output value.
    # training_set_inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
    # training_set_outputs = array([[0, 1, 1, 0]]).T
    word_set = ["crow","lion","sparrow","parrot","cheeta","rat","bat","rabbit",
    "peacock","dove","sparrow","goose","ostrich","pigeon","turkey","hawk","bald eagle",
    "raven","parrot","flamingo","seagull","swallow","blackbird","penguin","robin","swan",
    "owl","stork","woodpecker","dog","puppy","turtle","rabbit","parrot","cat","kitten","goldfish",
    "mouse","tropicalfish","hamster","cow","rabbit","ducks","shrimp","pig","goat","crab","deer",
    "bee","sheep","fish","turkey","dove","chicken","horse","squirrel","dog","chimpanzee",
    "ox","lion","panda","walrus","otter","mouse","kangaroo","goat","horse","monkey","cow",
    "koala","mole","elephant","leopard","hippopotamus","giraffe","fox","coyote","hedgehong",
    "sheep","deer"]
    # training_set_outputs= np.array((80,2))
    training_set_outputs = np.array([0,1,0,0,1,1,0,1,
    0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,
    0,0,0,1,1,1,1,0,1,1,1,
    1,1,1,1,1,0,1,1,1,1,1,
    0,1,1,0,0,0,1,1,1,1,
    1,1,1,1,1,1,1,1,1,1,1,
    1,1,1,1,1,1,1,1,1,
    1,1])

    print(len(word_set))
    print(len(training_set_outputs))

    training_set_inputs = np.zeros((80,15))
    test_set = np.zeros((10,15))
    print(len(word_set))
    print(len(training_set_outputs))
    for i  in range(0,len(word_set)):
        x = iter(word_set[i])

        arr1 = np.zeros((1,15))
        for j in range(0,len(word_set[i])):
            arr = next(x)
            arr1[0][j] = (ord(arr)/122)



        training_set_inputs[i]= arr1
    training_set_inputs =  np.array(training_set_inputs)
    training_set_outputs = np.array(training_set_outputs)

    for i  in range(0,10):
        x = iter(word_set[i])

        arr1 = np.zeros((1,15))
        for j in range(0,len(word_set[i])):
            arr = next(x)
            arr1[0][j] = (ord(arr)/122)

        test_set[i]= arr1
    print(training_set_inputs)
    print(training_set_outputs)
    print(test_set)


    # Train the neural network using a training set.
    # Do it 10,000 times and make small adjustments each time.
    neural_network.train(training_set_inputs, training_set_outputs, 10000)

    print ("New synaptic weights after training: ")
    print( neural_network.synaptic_weights)

    # Test the neural network with a new situation.
    print ("Considering new situation [1, 0, 0] -> ?: ")
    print( neural_network.think(test_set[0]))
