import numpy as np


# Neuro network, Perceptron neuro network.
class MLP:

    def __init__(self, input_neurons=3, hidden_layers=None, output_neurons=1):
        # initialize the default array of nodes in the hidden layers.
        if hidden_layers is None:
            hidden_layers = [3, 5, 2]

        self.input_neurons = input_neurons
        self.hidden_layers = hidden_layers
        self.output_neurons = output_neurons

        # Neurons in the perceptron
        self.layers = [self.input_neurons] + self.hidden_layers + [self.output_neurons]

        # initialize the list to store the weights for each layer
        self.weights = []

        for i in range(len(self.layers) - 1):
            self.weights.append(np.random.rand(self.layers[i], self.layers[i + 1]))
            print(i)
            print(self.weights)

    def matrix_multiplication(self, inputs):
        pass


if __name__ == "__main__":
    MLP()
