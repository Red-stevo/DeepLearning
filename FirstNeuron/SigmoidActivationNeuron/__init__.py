import math


def sigmoidActivation(add):
    return 1 / (1 + math.exp(-add))


def summation(actions, weights):
    addition = 0

    for action, weight in zip(actions, weights):
        addition += action * weight

    return sigmoidActivation(addition)


if __name__ == "__main__":
    # problem space.
    actions = [.4, .3, .3, .01]
    weights = [.43, .65, .15, .34]

    print(summation(actions, weights))
