import numpy as np
from collections import defaultdict
import os
import random
import pickle
import operator

def get_neighbours(training_set: list, instance: dict, k: int) -> list:
    """
    This functions computes and returns the distance between feature vectors and finds k neighbours

    :param training_set: The list used to compare the instance to
    :param instance: the instance for classification
    :param k: the number of neighbours
    :return: list neighbours
    """

    distances = []
    for x in range(len(training_set)):
        dist = distance(training_set[x], instance, k) + distance(instance, training_set[x], k)
        distances.append((training_set[x][2], dist))

    # experiment with what the key param does here
    distances.sort(key=operator.itemgetter(1))
    neighbours = []

    for x in range(k):
        neighbours.append(distances[x][0])

    return neighbours


def distance(first_instance: list, second_instance: list, k: int) -> float:
    """
    This fucntion calculates the distance between two points based on the cosine similarity calculation:
    cos(theta) = A dot product B / abs(A . B)

    :param first_instance: list containing mean matrix, covariance and folder index number
    :param second_instance: list containing mean matrix, covariance and folder index number
    :param k: the number of nearest neighbours
    :return: The distance between the two instances
    """

    distance = 0

    mm1 = first_instance[0]
    cm1 = first_instance[1]
    mm2 = second_instance[0]
    cm2 = second_instance[1]

    distance = np.trace(np.dot(np.linalg.inv(cm2), cm1))
    distance += (np.dot(np.dot((mm2 - mm1).transpose(), np.linalg.inv(cm2)), mm2 - mm1))
    distance += np.log(np.linalg.det(cm2)) - np.log(np.linalg.det(cm1))

    distance -= k
    return distance


