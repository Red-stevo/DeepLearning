import numpy as np


# Neuro network, Perceptron neuro network.

# Sigmoid activation function.
def _sigmoid(inputs):
    return 1 / 1 + np.exp(-inputs)


class MLP:

    def __init__(self, input_neurons=2, hidden_layers=None, output_neurons=2):
        # initialize the default array of nodes in the hidden layers.
        if hidden_layers is None:
            hidden_layers = [1, 2, 3]

        self.input_neurons = input_neurons
        self.hidden_layers = hidden_layers
        self.output_neurons = output_neurons
        self.weights = []

        # Neurons in the perceptron
        self.layers = [self.input_neurons] + self.hidden_layers + [self.output_neurons]

        # initialize the list to store the weights for each layer

        for i in range(len(self.layers) - 1):
            self.weights.append(np.random.rand(self.layers[i], self.layers[i + 1]))

    def activation(self, inputs):

        # initial inputs.
        print(f"Initial inputs: {inputs}")

        for i in self.weights:
            inputs = np.dot(inputs, i)
            # perform the activation
            inputs = _sigmoid(inputs)
        return inputs


if __name__ == "__main__":
    mlp = MLP()
    out_put = mlp.activation(np.random.rand(mlp.input_neurons))

    print(f"The OutPut : {out_put}")
