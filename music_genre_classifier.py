import numpy as np


def distance(first_instance, second_instance, k):
    """

    :param first_instance:
    :param second_instance:
    :param k:
    :return:
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


