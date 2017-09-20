"""This module chooses the pairs and order of workout leaders to lead conditioning"""

import random
import sys


def open_leader_file(openfile):
    """
    Reads a file that contains names of workout leaders
    Passes it to function choose_pairs to get back the leader pairs
    """
    leader_list = list()
    
    for line in openfile:
        for word in line.split():
            leader_list.append(word)

    return leader_list


def choose_pairs(leader_list):
    """
    Returns pair of workout leaders from list
    """

    leader_pairs_list = list()
    number_of_pairs = len(leader_list) / 2

    while len(leader_pairs_list) != number_of_pairs:
        leader1 = random.choice(leader_list)
        leader_list.remove(leader1)
        leader2 = random.choice(leader_list)
        leader_list.remove(leader2)

        leader_pairs_list.append((leader1, leader2))

    return leader_pairs_list


if __name__ == '__main__':
    LEADERS_LIST = open_leader_file(open(sys.argv[1]))
    PAIRS_OF_LEADERS = choose_pairs(LEADERS_LIST)
    for pair in PAIRS_OF_LEADERS:
        print(pair)
